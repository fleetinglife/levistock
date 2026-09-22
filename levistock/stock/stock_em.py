"""
东方财富 - 个股行情模块

数据源: 东方财富 (eastmoney.com)
模块说明: 提供A股实时行情数据接口，包括全量行情和指定股票行情查询
"""

import re
import json
import math
import random
import time
import requests
from tqdm import tqdm

_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Referer": "https://quote.eastmoney.com/",
}

_BASE_URL = "http://push2delay.eastmoney.com/api/qt/clist/get"

# fltt=2 表示价格字段不需要除以100，直接使用原始值
_SPOT_BASE_URL = (
    "http://push2delay.eastmoney.com/api/qt/ulist.np/get"
    "?fields=f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f14,f15,f16,f17,f18,f20,f21,f23"
    "&fltt=2"
    "&invt=2"
    "&cb=jQuery1124020910551869614946_1654180748613"
    "&ut=fa5fd1943c7b386f172d6893dbfba10b"
    "&wbp2u=%7C0%7C0%7C0%7Cweb"
    "&secids="
)

_MAX_STOCKS = 100

# 请求间随机延迟范围（秒），降低被风控/封IP的概率
_REQUEST_DELAY_RANGE = (1, 3)


def _delay():
    """请求前随机延迟"""
    time.sleep(random.uniform(*_REQUEST_DELAY_RANGE))


def _build_secid(code: str) -> str:
    """根据股票代码生成东财 secid（市场前缀.代码）"""
    if code.startswith("6"):
        return f"1.{code}"
    elif code.startswith("0") or code.startswith("3"):
        return f"0.{code}"
    elif code.startswith("920"):
        return f"0.{code}"
    return ""


def stocks_all_em(filter_st: bool = True) -> list:
    """
    获取A股全量实时行情数据（东方财富）

    数据源: 东方财富
    接口地址: http://push2delay.eastmoney.com/api/qt/clist/get
    更新频率: 交易日实时更新
    数据范围: 沪深京全市场A股

    Args:
        filter_st (bool): 是否过滤ST、*ST及退市股（现价≤1元），默认为 True
                          - True:  过滤，只返回正常交易股票
                          - False: 不过滤，返回全部股票

    Returns:
        list[dict]: 个股行情列表，每条数据包含以下字段：

        ============= ====================== ====================
        字段名         说明                    示例
        ============= ====================== ====================
        stock_code     股票代码               "000001"
        stock_name     股票名称               "平安银行"
        price          现价/收盘价             11.50
        change_pct     涨跌幅(%)              0.35
        change_amt     涨跌额                 0.04
        volume         成交量(手)             1234567
        amount         成交额(元)             1234567890.0
        amplitude      振幅(%)                1.20
        turnover_rate  换手率(%)              0.21
        pe_ttm         市盈率TTM              12.50
        volume_ratio   量比                   1.05
        high           最高价                 11.60
        low            最低价                 11.40
        open           开盘价                 11.45
        pre_close      昨收价                 11.46
        total_market   总市值(元)             223000000000.0
        circ_market    流通市值(元)            220000000000.0
        pb             市净率PB               0.85
        ============= ====================== ====================

    Raises:
        RuntimeError: 接口返回异常时抛出
        requests.exceptions.RequestException: 网络请求异常时抛出

    Example:
        >>> import levistock as lk
        >>> # 获取全量A股行情（默认过滤ST）
        >>> data = lk.stocks_all_em()
        >>> print(len(data))
        >>> print(data[0])
        >>>
        >>> # 获取全量A股行情（包含ST股）
        >>> data_all = lk.stocks_all_em(filter_st=False)
        >>> print(len(data_all))
    """
    params = {
        "pn": 1,
        "pz": 200,
        "po": 1,
        "np": 1,
        "ut": "bd1d9ddb04089700cf9c27f6f7426281",
        "fltt": 2,
        "invt": 2,
        "fid": "f3",
        "fs": "m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048",
        "fields": "f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f14,f15,f16,f17,f18,f20,f21,f23",
    }

    # 先请求第一页，拿到总数和总页数
    resp = requests.get(_BASE_URL, params=params, headers=_HEADERS, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    if data.get("rc") != 0:
        raise RuntimeError(f"接口返回异常，rc={data.get('rc')}")

    body = data["data"]
    total = body["total"]
    total_pages = math.ceil(total / 200)
    raw = body.get("diff", [])

    # 翻页请求剩余数据，带进度条
    with tqdm(total=total_pages, desc="获取A股行情", unit="页") as pbar:
        pbar.update(1)  # 第一页已完成
        while len(raw) < total:
            params["pn"] += 1
            _delay()
            resp = requests.get(_BASE_URL, params=params, headers=_HEADERS, timeout=10)
            resp.raise_for_status()
            body = resp.json()["data"]
            raw.extend(body.get("diff", []))
            pbar.update(1)

    result = []
    seen = set()  # 用于去重

    for item in raw:
        code = str(item.get("f12", ""))
        name = str(item.get("f14", ""))
        price = item.get("f2", 0)

        # 去重
        if code in seen:
            continue
        seen.add(code)

        # 过滤 ST、*ST 及退市股（现价 ≤ 1元）
        if filter_st:
            if name.startswith("ST") or name.startswith("*ST"):
                continue
            try:
                if float(price) <= 1.0:
                    continue
            except (ValueError, TypeError):
                continue

        result.append({
            "stock_code":    code,
            "stock_name":    name,
            "price":         price,
            "change_pct":    item.get("f3",  "-"),
            "change_amt":    item.get("f4",  "-"),
            "volume":        item.get("f5",  "-"),
            "amount":        item.get("f6",  "-"),
            "amplitude":     item.get("f7",  "-"),
            "turnover_rate": item.get("f8",  "-"),
            "pe_ttm":        item.get("f9",  "-"),
            "volume_ratio":  item.get("f10", "-"),
            "high":          item.get("f15", "-"),
            "low":           item.get("f16", "-"),
            "open":          item.get("f17", "-"),
            "pre_close":     item.get("f18", "-"),
            "total_market":  item.get("f20", "-"),
            "circ_market":   item.get("f21", "-"),
            "pb":            item.get("f23", "-"),
        })

    return result


def stocks_em(stock_codes: list) -> list:
    """
    获取指定股票实时行情（东方财富）

    数据源: 东方财富
    接口地址: http://push2delay.eastmoney.com/api/qt/ulist.np/get
    更新频率: 交易日实时更新
    限制: 最多支持100只股票，超出部分自动截断

    Args:
        stock_codes (list): 股票代码列表，如 ["000001", "600001", "300001"]
                            支持沪深京全市场，最多100只

    Returns:
        list[dict]: 实时行情列表，字段同 stocks_all_em()

        ============= ====================== ====================
        字段名         说明                    示例
        ============= ====================== ====================
        stock_code     股票代码               "000001"
        stock_name     股票名称               "平安银行"
        price          现价/收盘价             11.50
        change_pct     涨跌幅(%)              0.35
        change_amt     涨跌额                 0.04
        volume         成交量(手)             1234567
        amount         成交额(元)             1234567890.0
        amplitude      振幅(%)                1.20
        turnover_rate  换手率(%)              0.21
        pe_ttm         市盈率TTM              12.50
        volume_ratio   量比                   1.05
        high           最高价                 11.60
        low            最低价                 11.40
        open           开盘价                 11.45
        pre_close      昨收价                 11.46
        total_market   总市值(元)             223000000000.0
        circ_market    流通市值(元)            220000000000.0
        pb             市净率PB               0.85
        ============= ====================== ====================

    Raises:
        ValueError: stock_codes 为空时抛出
        RuntimeError: 接口返回异常时抛出
        requests.exceptions.RequestException: 网络请求异常时抛出

    Example:
        >>> import levistock as lk
        >>> data = lk.stocks_em(["000001", "600519", "300750"])
        >>> for item in data:
        ...     print(f"{item['stock_name']}: {item['price']} ({item['change_pct']}%)")
    """
    if not stock_codes:
        raise ValueError("stock_codes 不能为空")

    # 最多100只
    codes = stock_codes[:_MAX_STOCKS]

    # 拼接 secids
    secids = []
    for code in codes:
        secid = _build_secid(str(code))
        if secid:
            secids.append(secid)

    if not secids:
        return []

    url = _SPOT_BASE_URL + ",".join(secids)
    resp = requests.get(url, headers=_HEADERS, timeout=10)
    resp.raise_for_status()

    # 接口返回 JSONP 格式，去掉回调函数包装
    text = resp.text
    match = re.search(r'\((.*)\)', text, re.DOTALL)
    if not match:
        raise RuntimeError("接口返回格式异常，无法解析 JSONP 数据")

    data = json.loads(match.group(1))
    if data.get("rc") != 0:
        raise RuntimeError(f"接口返回异常，rc={data.get('rc')}")

    items = data.get("data", {}).get("diff", [])
    result = []

    for item in items:
        result.append({
            "stock_code":    str(item.get("f12", "")),
            "stock_name":    str(item.get("f14", "")),
            "price":         item.get("f2",  "-"),
            "change_pct":    item.get("f3",  "-"),
            "change_amt":    item.get("f4",  "-"),
            "volume":        item.get("f5",  "-"),
            "amount":        item.get("f6",  "-"),
            "amplitude":     item.get("f7",  "-"),
            "turnover_rate": item.get("f8",  "-"),
            "pe_ttm":        item.get("f9",  "-"),
            "volume_ratio":  item.get("f10", "-"),
            "high":          item.get("f15", "-"),
            "low":           item.get("f16", "-"),
            "open":          item.get("f17", "-"),
            "pre_close":     item.get("f18", "-"),
            "total_market":  item.get("f20", "-"),
            "circ_market":   item.get("f21", "-"),
            "pb":            item.get("f23", "-"),
        })

    return result