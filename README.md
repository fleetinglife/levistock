## A股或量化交流（纸✈️）：[https://t.me/+KkSvBB_Utaw5ZmJl](https://t.me/+zkl2FrWMF8pkYjg1)

# levistock

A股市场数据 SDK，封装东方财富、财联社、同花顺、开盘红、i问财常用接口。

## 安装

```bash
pip install levistock
```

或从 GitHub 安装最新版：

```bash
pip install git+https://github.com/fleetinglife/levistock.git
```

## 快速开始

```python
import levistock as lk

# 大盘指数
lk.market_index_em()

# 涨停池
lk.stock_zt_pool_em()

# 行业板块
lk.sector_em()
```

---

## 接口文档

### 目录

| 数据源 | 接口 | 说明 | 模块 |
|--------|------|------|------|
| 东方财富 | [market_index_em](#market_index_em) | 常用6个大盘指数 | 大盘 |
| 东方财富 | [market_index_all_em](#market_index_all_em) | 全部大盘指数 | 大盘 |
| 东方财富 | [sector_em](#sector_em) | 行业/概念板块列表 | 板块 |
| 东方财富 | [sector_stocks_em](#sector_stocks_em) | 板块成分股 | 板块 |
| 东方财富 | [sector_stock_belong_em](#sector_stock_belong_em) | 股票所属板块 | 板块 |
| 东方财富 | [stocks_all_em](#stocks_all_em) | 全量A股实时行情 | 股票 |
| 东方财富 | [stocks_em](#stocks_em) | 指定股票实时行情 | 股票 |
| 东方财富 | [stock_zt_pool_em](#stock_zt_pool_em) | 涨停板股票池 | 股票 |
| 东方财富 | [stock_dt_pool_em](#stock_dt_pool_em) | 跌停板股票池 | 股票 |
| 东方财富 | [stock_yesterday_zt_em](#stock_yesterday_zt_em) | 昨日涨停今日表现 | 股票 |
| 东方财富 | [stock_changes_em](#stock_changes_em) | 盘口异动列表 | 股票 |
| 东方财富 | [stock_changes_detail_em](#stock_changes_detail_em) | 个股异动明细 | 股票 |
| 财联社 | [market_emotion_cls](#market_emotion_cls) | 市场情绪数据 | 大盘 |
| 财联社 | [market_wind_cls](#market_wind_cls) | 今日风口板块 | 大盘 |
| 财联社 | [market_wind_stocks_cls](#market_wind_stocks_cls) | 风口板块龙头股 | 大盘 |
| 财联社 | [market_mainline_cls](#market_mainline_cls) | 今日主线机会 | 大盘 |
| 财联社 | [sector_industry_cls](#sector_industry_cls) | 行业板块实时行情 | 板块 |
| 财联社 | [get_sector_heat](#get_sector_heat) | 板块热度排行 | 板块 |
| 财联社 | [get_sector_rotation](#get_sector_rotation) | 板块轮动（近N日top10） | 板块 |
| 财联社 | [stock_zt_pool_cls](#stock_zt_pool_cls) | 涨停池（含涨停原因） | 股票 |
| 财联社 | [stock_timeline_cls](#stock_timeline_cls) | 个股分时数据 | 股票 |
| 财联社 | [stock_kline_cls](#stock_kline_cls) | 个股K线数据 | 股票 |
| 财联社 | [news_telegraph_cls](#news_telegraph_cls) | 电报快讯 | 资讯 |
| 同花顺 | [stock_hot_rank_ths](#stock_hot_rank_ths) | 人气股排行榜 | 股票 |
| 开盘红 | [market_emotion_kph](#market_emotion_kph) | 市场情绪数据（实时/历史） | 大盘 |
| 开盘红 | [sector_ranking_kph](#sector_ranking_kph) | 精选/行业/地区板块排行 | 板块 |
| 开盘红 | [sector_stocks_his_kph](#sector_stocks_his_kph) | 历史板块成分股 | 板块 |
| 开盘红 | [limit_up_his_kph](#limit_up_his_kph) | 历史涨停股列表 | 股票 |
| 开盘红 | [limit_down_his_kph](#limit_down_his_kph) | 历史跌停股列表 | 股票 |
| 开盘红 | [wind_vane_his_kph](#wind_vane_his_kph) | 历史风向标列表 | 股票 |
| 开盘红 | [get_zttt](#get_zttt) | 涨停天梯 | 复盘 |
| 开盘红 | [get_pmsl](#get_pmsl) | 盘面梳理（板块事件流） | 复盘 |
| 开盘红 | [get_his_limit_resumption](#get_his_limit_resumption) | 历史涨停复盘（含涨停原因） | 复盘 |
| i问财 | [stock_strategy_wencai](#stock_strategy_wencai) | 自然语言策略查询 | 股票 |
| 自有服务器 | [is_trade_day](#is_trade_day) | 判断今天是否为交易日 | 工具 |
| 自有服务器 | [get_trade_days](#get_trade_days) | 获取近N个交易日 | 工具 |

---

### 大盘 market

#### 东方财富

##### `market_index_em`

获取A股常用大盘指数实时行情，返回上证指数、深证成指、创业板指、科创50、沪深300、中证500。

```python
data = lk.market_index_em()
for item in data:
    print(f"{item['name']}: {item['price']} ({item['change_pct']}%)")
```

| 字段 | 说明 |
|------|------|
| name | 指数名称 |
| code | 指数代码 |
| price | 最新价 |
| change_pct | 涨跌幅(%) |
| change_amt | 涨跌额 |
| volume | 成交量 |
| amount | 成交额(元) |
| high | 最高价 |
| low | 最低价 |
| open | 开盘价 |
| pre_close | 昨收价 |

---

##### `market_index_all_em`

获取全部大盘指数，字段同 `market_index_em`。

```python
data = lk.market_index_all_em()
print(f"共 {len(data)} 个指数")
```

---

#### 财联社

##### `market_emotion_cls`

获取A股市场情绪数据，包含涨跌分布、封板率、连板梯队等。

```python
data = lk.market_emotion_cls()
print(f"市场热度: {data['market_degree']}")
print(f"涨停家数: {data['up_down_dis']['up_num']}")
print(f"封板率: {data['up_ratio']}")
```

| 字段 | 说明 |
|------|------|
| market_degree | 市场热度(0-100) |
| shsz_balance | 两市成交额 |
| shsz_balance_change_px | 较上日成交额变化 |
| up_ratio | 封板率 |
| up_ratio_num | 封板数量 |
| up_open_num | 炸板数量 |
| performance | 昨涨停今表现 |
| up_open_ratio | 高开率 |
| profit_ratio | 获利率 |
| up_down_dis | 涨跌分布(dict) |
| limit_up_board | 连板梯队(dict) |

---

##### `market_wind_cls`

获取今日风口板块列表。

```python
data = lk.market_wind_cls()
for item in data:
    print(f"{item['plate_name']}: {item['catalyst'][:30]}...")
```

| 字段 | 说明 |
|------|------|
| plate_code | 板块代码 |
| plate_name | 板块名称 |
| catalyst | 催化剂描述 |

---

##### `market_wind_stocks_cls`

获取风口板块龙头股。

| 参数 | 说明 |
|------|------|
| plate_code | 板块代码，通过 `market_wind_cls()` 获取 |

```python
wind = lk.market_wind_cls()
stocks = lk.market_wind_stocks_cls(wind[0]["plate_code"])
```

| 字段 | 说明 |
|------|------|
| secu_code | 股票代码（含市场前缀） |
| secu_name | 股票名称 |
| last_px | 现价 |
| change | 涨跌幅 |
| continuous | 连板次数 |

---

##### `market_mainline_cls`

获取今日主线机会，返回主线题材、板块及龙头股。

```python
data = lk.market_mainline_cls()
print(data)
```

---

#### 开盘红

##### `market_emotion_kph`

获取A股市场情绪数据。不传日期查今天实时，传历史日期查历史。

| 参数 | 说明 |
|------|------|
| date | 交易日期，格式 `"YYYY-MM-DD"`，不传默认今天 |

```python
data = lk.market_emotion_kph()
data = lk.market_emotion_kph(date="2026-05-13")
print(f"涨停: {data['zt']}只  跌停: {data['dt']}只  市场人气: {data['sign']}")
```

| 字段 | 说明 |
|------|------|
| zt | 涨停总数 |
| dt | 跌停总数 |
| sjzt | 实际涨停（非ST） |
| sjdt | 实际跌停（非ST） |
| stzt | ST涨停 |
| stdt | ST跌停 |
| rise_num | 上涨家数 |
| fall_num | 下跌家数 |
| flat | 平盘家数 |
| sign | 市场人气判断文字 |
| rise_dist | 各涨幅区间股票数 {1:xx ... 10:xx} |
| fall_dist | 各跌幅区间股票数 {-1:xx ... -10:xx} |
| szln | 沪市成交额(元) |
| qscln | 全市成交额(元) |
| s_zrcs | 昨日沪市成交额(元) |
| q_zrcs | 昨日全市成交额(元) |

---

### 板块 sector

#### 东方财富

##### `sector_em`

获取A股板块列表，支持行业板块（全量/分级）和概念板块。

| 参数 | 说明 |
|------|------|
| sector_type | 板块类型，默认 `"industry"` |

| 类型值 | 说明 |
|--------|------|
| `"industry"` | 全部行业板块（默认） |
| `"concept"` | 概念板块 |
| `"industry_l1"` | 东财一级行业（31个） |
| `"industry_l2"` | 东财二级行业（128个） |
| `"industry_l3"` | 东财三级行业（337个） |

```python
industry = lk.sector_em()
concept  = lk.sector_em(sector_type="concept")
l1       = lk.sector_em(sector_type="industry_l1")
```

| 字段 | 说明 |
|------|------|
| sector_code | 板块代码 |
| sector_name | 板块名称 |
| change_pct | 涨跌幅(%) |
| amount | 成交额(元) |
| main_inflow | 主力净流入(元) |
| lead_stock_name | 领涨股名称 |
| lead_stock_code | 领涨股代码 |
| lead_stock_chg | 领涨股涨跌幅(%) |
| up_count | 上涨家数 |
| down_count | 下跌家数 |

---

##### `sector_stocks_em`

获取板块成分股，行业板块和概念板块通用。

| 参数 | 说明 |
|------|------|
| sector_code | 板块代码，如 `"BK1033"` |

```python
stocks = lk.sector_stocks_em("BK1033")
```

| 字段 | 说明 |
|------|------|
| stock_code | 股票代码 |
| stock_name | 股票名称 |

---

##### `sector_stock_belong_em`

批量查询股票所属行业板块。

| 参数 | 说明 |
|------|------|
| stock_codes | 股票代码列表，如 `["000001", "600001"]` |

```python
data = lk.sector_stock_belong_em(["000001", "600001", "300001"])
for item in data:
    print(f"{item['stock_name']} → {item['sector_name']}")
```

| 字段 | 说明 |
|------|------|
| stock_code | 股票代码 |
| stock_name | 股票名称 |
| sector_name | 所属行业板块 |

---

#### 财联社

##### `sector_industry_cls`

获取A股行业板块实时行情，按涨跌幅从高到低排序。

```python
data = lk.sector_industry_cls()
```

| 字段 | 说明 |
|------|------|
| secu_name | 板块名称 |
| secu_code | 板块代码 |
| change | 涨跌幅 |
| main_fund_diff | 主力净流入(元) |
| limit_up | 上涨家数 |
| limit_down | 下跌家数 |
| limit_up_num | 涨停家数 |
| limit_down_num | 跌停家数 |
| first_stock | 领涨股信息(dict) |

---

##### `get_sector_heat`

获取板块热度排行（实时）。

```python
data = lk.get_sector_heat()
for item in data[:10]:
    print(f"{item['rank']}. {item['plate_name']} 热度:{item['cur_heat']:.1f}")
```

| 字段 | 说明 |
|------|------|
| plate_code | 板块代码 |
| plate_name | 板块名称 |
| rank | 当前热度排名 |
| cur_heat | 当前热度值 |
| rank_change | 排名变化（正=上升，负=下降） |
| is_new | 是否新上榜（1=是，0=否） |

---

##### `get_sector_rotation`

获取板块轮动，近N个交易日每日top10板块涨跌幅。

| 参数 | 说明 |
|------|------|
| days | 查询天数，默认4 |

```python
data = lk.get_sector_rotation(days=4)
for day in data:
    print(f"{day['trade_date']}: {[p['plate_name'] for p in day['plates']]}")
```

| 字段 | 说明 |
|------|------|
| trade_date | 交易日期 |
| plates | 当日top10板块列表 |
| plates[].plate_code | 板块代码 |
| plates[].plate_name | 板块名称 |
| plates[].change | 当日涨跌幅(%) |

---

#### 开盘红

##### `sector_ranking_kph`

获取精选/行业/地区板块排行。传今天日期查实时，传历史日期查历史。

| 常量 | 值 | 说明 |
|------|----|------|
| `SECTOR_SELECTED` | `"7"` | 精选板块 |
| `SECTOR_INDUSTRY` | `"4"` | 行业板块 |
| `SECTOR_REGION` | `"6"` | 地区板块 |

| 参数 | 说明 |
|------|------|
| date | 交易日期，格式 `"YYYY-MM-DD"`，必填 |
| zs_type | 板块类型，必填，使用上方常量 |
| fetch_all | 是否获取全量，默认 `False`（前50条） |

```python
data = lk.sector_ranking_kph(date="2026-05-14", zs_type=lk.SECTOR_SELECTED)
data = lk.sector_ranking_kph(date="2026-05-13", zs_type=lk.SECTOR_INDUSTRY, fetch_all=True)
```

| 字段 | 说明 |
|------|------|
| plate_id | 板块ID |
| plate_name | 板块名称 |
| change_pct | 涨跌幅(%) |
| amount | 成交额(元) |
| net_inflow | 净流入(元) |
| net_inflow_5d | 5日净流入(元) |
| buy_amount | 主买金额(元) |
| sell_amount | 主卖金额(元) |
| turnover_rate | 换手率(%) |
| market_cap | 总市值(元) |
| avg_change | 平均涨幅(%) |
| stock_count | 成分股数量 |

---

##### `sector_stocks_his_kph`

获取历史板块成分股，日期必须小于今天。

| 参数 | 说明 |
|------|------|
| plate_id | 板块ID，通过 `sector_ranking_kph()` 获取，必填 |
| date | 交易日期，格式 `"YYYY-MM-DD"`，必须小于今天 |

```python
plates = lk.sector_ranking_kph(date="2026-05-13", zs_type=lk.SECTOR_SELECTED)
stocks = lk.sector_stocks_his_kph(plate_id=plates[0]["plate_id"], date="2026-05-13")
```

| 字段 | 说明 |
|------|------|
| code | 股票代码 |
| name | 股票名称 |
| price | 现价(元) |
| change_pct | 涨跌幅(%) |
| amount | 成交额(元) |
| turnover_rate | 换手率(%) |
| float_amount | 流通市值(元) |
| main_buy | 主力买入(元) |
| main_sell | 主力卖出(元) |
| main_net | 主力净额(元) |
| buy_ratio | 主买占比(%) |
| sell_ratio | 主卖占比(%) |
| net_ratio | 净额占比(%) |
| tags | 概念标签 |
| limit_tag | 连板标签 |
| rank_tag | 龙虎榜标签 |
| recent_chg | 近期涨幅(%) |
| limit_count | 近期涨停次数 |
| chg_1d | 1日涨幅(%) |
| chg_5d | 5日涨幅(%) |
| chg_20d | 20日涨幅(%) |

---

### 股票 stock

#### 东方财富

##### `stocks_all_em`

获取A股全量实时行情。

| 参数 | 说明 |
|------|------|
| filter_st | 是否过滤ST股，默认 `True` |

```python
data = lk.stocks_all_em()
print(f"股票数: {len(data)}")
```

| 字段 | 说明 |
|------|------|
| stock_code | 股票代码 |
| stock_name | 股票名称 |
| price | 现价 |
| change_pct | 涨跌幅(%) |
| change_amt | 涨跌额 |
| volume | 成交量(手) |
| amount | 成交额(元) |
| turnover_rate | 换手率(%) |
| pe_ttm | 市盈率TTM |
| volume_ratio | 量比 |
| high | 最高价 |
| low | 最低价 |
| open | 开盘价 |
| pre_close | 昨收价 |
| total_market | 总市值(元) |
| circ_market | 流通市值(元) |
| pb | 市净率PB |

---

##### `stocks_em`

获取指定股票实时行情，最多支持100只，字段同 `stocks_all_em()`。

| 参数 | 说明 |
|------|------|
| stock_codes | 股票代码列表，最多100只 |

```python
data = lk.stocks_em(["000001", "600519", "300750"])
```

---

##### `stock_zt_pool_em`

获取涨停板股票池，支持历史日期查询。

| 参数 | 说明 |
|------|------|
| date | 交易日期，格式 `"YYYYMMDD"`，默认今天 |

```python
data = lk.stock_zt_pool_em()
data = lk.stock_zt_pool_em(date="20260513")
```

| 字段 | 说明 |
|------|------|
| stock_code | 股票代码 |
| stock_name | 股票名称 |
| price | 现价(元) |
| change_pct | 涨跌幅(%) |
| continuous | 连板次数 |
| first_zt_time | 首次涨停时间 |
| last_zt_time | 最后涨停时间 |
| open_times | 炸板次数 |
| amount | 成交额(元) |
| turnover_rate | 换手率(%) |
| main_inflow | 主力净流入(元) |
| sector | 所属行业板块 |

---

##### `stock_dt_pool_em`

获取跌停板股票池，支持历史日期查询。

| 参数 | 说明 |
|------|------|
| date | 交易日期，格式 `"YYYYMMDD"`，默认今天 |

```python
data = lk.stock_dt_pool_em()
data = lk.stock_dt_pool_em(date="20260513")
```

| 字段 | 说明 |
|------|------|
| stock_code | 股票代码 |
| stock_name | 股票名称 |
| price | 现价(元) |
| change_pct | 涨跌幅(%) |
| days | 连续跌停天数 |
| last_dt_time | 最后跌停时间 |
| seal_amount | 封单金额(元) |
| amount | 成交额(元) |
| turnover_rate | 换手率(%) |
| main_inflow | 主力净流入(元) |
| sector | 所属行业板块 |

---

##### `stock_yesterday_zt_em`

获取昨日涨停今日表现。

| 参数 | 说明 |
|------|------|
| date | 交易日期，格式 `"YYYYMMDD"`，默认今天 |

```python
data = lk.stock_yesterday_zt_em()
for item in data[:5]:
    print(f"{item['stock_name']} 今日:{item['change_pct']}% 高开:{item['open_ratio']}%")
```

| 字段 | 说明 |
|------|------|
| stock_code | 股票代码 |
| stock_name | 股票名称 |
| price | 现价(元) |
| zt_price | 涨停价(元) |
| change_pct | 今日涨跌幅(%) |
| amount | 成交额(元) |
| turnover_rate | 换手率(%) |
| amplitude | 振幅(%) |
| open_ratio | 高开比(%) |
| yesterday_time | 昨日涨停时间 |
| yesterday_cont | 昨日连板数 |
| sector | 所属行业板块 |
| zt_days | 近期涨停天数 |
| zt_count | 近期涨停次数 |

---

##### `stock_changes_em`

获取实时盘口异动股票列表。

| 参数 | 说明 |
|------|------|
| change_type | 异动类型，默认 `"8201"` 火箭发射 |
| filter_st | 是否过滤ST及三板，默认 `True` |

| 类型值 | 说明 |
|--------|------|
| `"8201"` | 火箭发射 |
| `"8202"` | 快速反弹 |
| `"8193"` | 大笔买入 |
| `"8205"` | 封涨停板 |
| `"64"` | 有大买盘 |

```python
data = lk.stock_changes_em()
data = lk.stock_changes_em(change_type="8193")
```

---

##### `stock_changes_detail_em`

获取个股盘口异动明细。

| 参数 | 说明 |
|------|------|
| stock_code | 股票代码，如 `"000001"` |
| market | 市场，`"0"` 深市，`"1"` 沪市 |
| date | 日期，格式 `"YYYYMMDD"`，默认今天 |

```python
data = lk.stock_changes_detail_em(stock_code="000001", market="0")
```

---

#### 财联社

##### `stock_zt_pool_cls`

获取当日涨停池，含涨停原因，仅支持当天。

```python
data = lk.stock_zt_pool_cls()
for item in data:
    print(f"{item['secu_name']}: {item['up_reason']}")
```

| 字段 | 说明 |
|------|------|
| secu_code | 股票代码（含市场前缀） |
| secu_name | 股票名称 |
| last_px | 现价(元) |
| change | 涨跌幅 |
| up_reason | 涨停原因 |

---

##### `stock_timeline_cls`

获取个股分时数据。

| 参数 | 说明 |
|------|------|
| stock_code | 股票代码，支持 `"002664"` 或 `"sz002664"` 格式 |

```python
data = lk.stock_timeline_cls("002664")
```

| 字段 | 说明 |
|------|------|
| date | 交易日期 |
| minute | 分钟时间 |
| last_px | 最新价 |
| business_balance | 成交额 |
| business_amount | 成交量 |
| open_px | 开盘价 |
| preclose_px | 昨收价 |
| av_px | 均价 |

---

##### `stock_kline_cls`

获取个股K线数据。

| 参数 | 说明 |
|------|------|
| stock_code | 股票代码，支持 `"002664"` 或 `"sz002664"` 格式 |
| kline_type | K线类型，默认 `"daily"` |
| limit | 返回条数，默认50 |
| offset | 偏移量，默认0 |

| 类型值 | 说明 |
|--------|------|
| `"daily"` | 日K（默认） |
| `"weekly"` | 周K |
| `"monthly"` | 月K |
| `"yearly"` | 年K |

```python
data = lk.stock_kline_cls("002664")
data = lk.stock_kline_cls("002664", kline_type="weekly", limit=100)
```

---

#### 同花顺

##### `stock_hot_rank_ths`

获取A股人气股排行榜。

| 参数 | 说明 |
|------|------|
| limit | 返回条数，默认100 |

```python
data = lk.stock_hot_rank_ths()
for item in data[:5]:
    print(f"{item['rank']}. {item['name']} {item['change_pct']}%")
```

| 字段 | 说明 |
|------|------|
| rank | 排名 |
| code | 股票代码 |
| name | 股票名称 |
| price | 现价(元) |
| change_pct | 涨跌幅(%) |
| change_amt | 涨跌额 |
| tag | 标签信息(dict) |

---

#### 开盘红

##### `limit_up_his_kph`

获取历史涨停股列表，日期必须小于今天。

| 参数 | 说明 |
|------|------|
| date | 交易日期，格式 `"YYYY-MM-DD"`，必须小于今天 |

```python
data = lk.limit_up_his_kph(date="2026-05-13")
for item in data:
    print(f"{item['name']} 原因:{item['reason']} 连板:{item['limit_count']}")
```

| 字段 | 说明 |
|------|------|
| code | 股票代码 |
| name | 股票名称 |
| reason | 涨停原因 |
| themes | 题材 |
| industry_id | 行业ID |
| industry_zt | 同行业涨停数 |
| limit_tag | 连板标签（首板/二板...） |
| limit_count | 连板数 |
| limit_time | 最后涨停时间戳 |
| open_time | 开板时间戳（0=未开板） |
| seal_amount | 封单量 |
| seal_money | 封单金额(元) |
| turnover | 成交额(元) |
| turnover_rate | 换手率(%) |
| net_inflow | 净流入(元) |
| market_cap | 流通市值(元) |

---

##### `limit_down_his_kph`

获取历史跌停股列表，日期必须小于今天。

| 参数 | 说明 |
|------|------|
| date | 交易日期，格式 `"YYYY-MM-DD"`，必须小于今天 |

```python
data = lk.limit_down_his_kph(date="2026-05-13")
for item in data:
    print(f"{item['name']} 换手:{item['turnover_rate']}%")
```

| 字段 | 说明 |
|------|------|
| code | 股票代码 |
| name | 股票名称 |
| themes | 题材 |
| industry_id | 行业ID |
| limit_time | 跌停时间戳 |
| open_time | 开板时间戳（0=未开板） |
| seal_amount | 封单量 |
| seal_money | 封单金额(元) |
| turnover | 成交额(元) |
| turnover_rate | 换手率(%) |
| net_inflow | 净流入(元) |
| market_cap | 流通市值(元) |

---

##### `wind_vane_his_kph`

获取历史风向标列表，字段同 `limit_up_his_kph()`。

| 参数 | 说明 |
|------|------|
| date | 交易日期，格式 `"YYYY-MM-DD"`，必须小于今天 |

```python
data = lk.wind_vane_his_kph(date="2026-05-13")
```

---

### 复盘 fupanla

#### 开盘红

##### `get_zttt`

涨停天梯，不传日期默认今天，支持历史日期查询。

| 参数 | 说明 |
|------|------|
| date | 交易日期，格式 `"YYYY-MM-DD"`，默认今天 |

```python
data = lk.get_zttt()
data = lk.get_zttt(date="2026-05-21")
stock_list = data.get("StockList", [])
for s in stock_list:
    print(f"{s[1]} {s[2]}连板 板块:{s[5]}")
```

| StockList索引 | 说明 |
|---------------|------|
| [0] | 股票代码 |
| [1] | 股票名称 |
| [2] | 连板数 |
| [3] | 涨停时间戳(秒) |
| [4] | 所属板块代码 |
| [5] | 所属板块名称 |
| [6] | 是否大单一字（1=是） |
| [7] | 是否有人气（1=是） |
| [8] | 板块涨停股数量 |
| [9] | 个股成交额(元) |
| [10] | 板块成交额(元) |

---

##### `get_pmsl`

盘面梳理，板块事件流，不传日期默认今天，支持历史日期查询。

| 参数 | 说明 |
|------|------|
| date | 交易日期，格式 `"YYYY-MM-DD"`，默认今天 |
| st | 返回条数，默认30 |
| index | 分页起始，默认0 |

```python
data = lk.get_pmsl()
data = lk.get_pmsl(date="2026-05-21")
for item in data.get("List", []):
    print(f"[{item['TagName']}] {item['Detail']}")
```

| 字段 | 说明 |
|------|------|
| TimeMin | 事件时间戳(秒) |
| TagID | 事件类型ID |
| TagName | 事件类型（大单一字/直线拉升/权重拉升/趋势新高/人气股杀跌/...） |
| TagShuXing | 事件属性（2=正面，0=负面，1=中性） |
| ZSCode | 板块代码 |
| ZSName | 板块名称 |
| Detail | 事件描述文字 |
| StockList | 相关股票列表 [[代码, 名称], ...] |

---

##### `get_his_limit_resumption`

历史涨停复盘，含涨停原因详细文字，支持历史日期查询。

| 参数 | 说明 |
|------|------|
| date | 交易日期，格式 `"YYYY-MM-DD"`，默认今天 |
| st | 返回条数，默认100 |
| index | 分页起始，默认0 |

```python
data = lk.get_his_limit_resumption(date="2026-05-21")
nums = data.get("nums", {})
print(f"涨停:{nums['ZT']} 跌停:{nums['DT']} 占比:{nums['ZBL']}%")
for plate in data.get("list", []):
    print(f"\n板块: {plate['ZSName']}")
    for s in plate.get("StockList", []):
        print(f"  {s[1]} {s[9]} 原因:{s[16]}")
        print(f"  {s[17][:60]}...")
```

| nums字段 | 说明 |
|----------|------|
| ZT | 涨停总数 |
| DT | 跌停总数 |
| ZBL | 涨停占比(%) |
| SZJS | 上涨家数 |
| XDJS | 下跌家数 |
| yestRase | 昨日涨跌幅 |

| StockList索引 | 说明 |
|---------------|------|
| [0] | 股票代码 |
| [1] | 股票名称 |
| [9] | 连板描述（首板/2连板/...） |
| [10] | 连板数 |
| [11] | 所属概念 |
| [16] | 涨停原因简短标签 |
| [17] | 涨停原因详细文字 |

---

### 资讯 news

#### 财联社

##### `news_telegraph_cls`

获取财联社电报快讯，数据超过20条时自动显示进度条。

| 参数 | 说明 |
|------|------|
| date | 日期，格式 `"YYYY-MM-DD"`，默认今天 |
| category | 消息类型，默认 `"important"` |

| 类型值 | 说明 |
|--------|------|
| `"all"` | 全部电报 |
| `"important"` | 加红重要消息（默认） |
| `"company"` | 公司公告 |

```python
data = lk.news_telegraph_cls()
data = lk.news_telegraph_cls(category="all")
data = lk.news_telegraph_cls(date="2026-05-07", category="company")
for item in data:
    print(f"{item['time']} | {item['title']}")
```

| 字段 | 说明 |
|------|------|
| title | 标题 |
| content | 正文内容 |
| time | 发布时间，格式 `"YYYY-MM-DD HH:MM:SS"` |

---

### 工具 utils

#### 自有服务器

##### `is_trade_day`

判断今天是否为A股交易日。

```python
if lk.is_trade_day():
    print("今天是交易日")
```

| 返回值 | 说明 |
|--------|------|
| `bool` | True=交易日，False=非交易日 |

---

##### `get_trade_days`

获取近N个交易日列表。

| 参数 | 说明 |
|------|------|
| n | 查询数量，默认10，范围1-30 |

```python
days = lk.get_trade_days()
days = lk.get_trade_days(n=5)
```

| 返回值 | 说明 |
|--------|------|
| `list[str]` | 交易日列表，格式 `"YYYYMMDD"`，从近到远排列 |

---

## License

MIT
