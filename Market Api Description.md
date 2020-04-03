
## Docking api related interface description

* symbol：usdt_cnyt  The name of the transaction pair, the commodity currency on the left and the base currency on the right. Stitching with "_" in the middle

### market quotation interface

url： /api/v1/tickers

#### Response
```
{
    "ticker": [
        {
            "symbol": "usdt_cnyt", 
            "high": "6.9754", 
            "vol": "355542.7", 
            "last": "6.9666", 
            "low": "6.8781", 
            "buy": "6.93", 
            "sell": "7"
        }, 
        {
            "symbol": "btc_cnyt", 
            "high": "45591.89", 
            "vol": "586.4149", 
            "last": "43901.81", 
            "low": "43598.86", 
            "buy": "43433.58", 
            "sell": "44142.67"
        }, 
        {
            "symbol": "eth_cnyt", 
            "high": "1560.42", 
            "vol": "2543.02", 
            "last": "1401.97", 
            "low": "1367.66", 
            "buy": "1387.29", 
            "sell": "1415.59"
        }], 
    "timestamp": 1539239753401
}
```
#### Field description

timestamp: Server time when returning at server time 
symbol：Transaction pair     
buy: best bid price
high: 24H highest price
last: last price 
low: 24H lowest price
sell: best sell price  
vol:  24H vol

### depth interface

url： /api/v1/depth?symbol=usdt_cnyt&size=20

#### Response

```
{
    "asks": [
        [
            7, 
            5
        ], 
        [
            7.005, 
            29.1
        ], 
        [
            7.0346, 
            23.4
        ], 
        [
            7.0348, 
            1
        ]
    ], 
    "bids": [
        [
            6.93, 
            10
        ], 
        [
            6.9, 
            5
        ],
        [
            2, 
            20
        ]
    ]
}
```
#### Field description

asks :Seller depth[[price，Quantity],···]
bids :Buyer depth[[price，Quantity],···]

### Latest transaction record interface

url： /api/v1/trades?symbol=usdt_cnyt&size=20

#### Response

```
[
    [
        1539240188958808, 
        6.9654, 
        3.7, 
        1
    ], 
    [
        1539240188841064, 
        6.9654, 
        5, 
        -1
    ], 
    [
        1539240188722852, 
        6.966, 
        2.1, 
        -1
    ]
]
```

#### Field description

[[16-bit in units of 1 microseconds，price，Quantity，Buying and selling direction（-1 sell ，1 buy）]]

### Candlestick chart interface

url： /api/v1/kline?symbol=usdt_cnyt&size=100&range=60000

range: millisecond  （Currently supported 1 min：60000，5 min：300000 ...and 15 min，30 min，hours，day，week，month）

#### Response

```
[
    [
        1539154140000, 
        6.8813, 
        6.8813, 
        6.8793, 
        6.8804, 
        133.1
    ], 
    [
        1539154200000, 
        6.8802, 
        6.8805, 
        6.8793, 
        6.88, 
        145.2
    ], 
    [
        1539154260000, 
        6.8795, 
        6.8806, 
        6.8793, 
        6.8803, 
        259.1
    ], 
    [
        1539154320000, 
        6.88, 
        6.8811, 
        6.8794, 
        6.881, 
        271.5
    ], 
    [
        1539154380000, 
        6.881, 
        6.8813, 
        6.88, 
        6.8806, 
        98.4
    ], 
    [
        1539154440000, 
        6.8807, 
        6.8812, 
        6.8798, 
        6.8808, 
        156
    ], 
    [
        1539154500000, 
        6.8808, 
        6.8812, 
        6.8798, 
        6.8804, 
        135.8
    ], 
    [
        1539154560000, 
        6.8804, 
        6.8811, 
        6.88, 
        6.8802, 
        26.6
    ]
]
```

#### Field description

[[16-bit in units of 1 microseconds，Open，High，Low，Close，Volume]]

    [
        1539154560000,  16-bit in units of 1 microseconds
        6.8804,  Open
        6.8811,  High
        6.88,    Low
        6.8802,  Close
        26.6     Volume
    ]

### Trading Pair info interface

url： /api/v1/exchangeInfo

#### Response

```
[
    {
        "symbol": "usdt_cnyt", 
        "quoteAssetPrecision": 4, 
        "baseAsset": "usdt", 
        "baseAssetPrecision": 1, 
        "quoteAsset": "cnyt", 
        "status": "trading"
    }, 
    {
        "symbol": "btc_cnyt", 
        "quoteAssetPrecision": 2, 
        "baseAsset": "btc", 
        "baseAssetPrecision": 4, 
        "quoteAsset": "cnyt", 
        "status": "trading"
    }, 
    {
        "symbol": "eth_cnyt", 
        "quoteAssetPrecision": 2, 
        "baseAsset": "eth", 
        "baseAssetPrecision": 3, 
        "quoteAsset": "cnyt", 
        "status": "trading"
    }, 
    {
        "symbol": "bch_cnyt", 
        "quoteAssetPrecision": 2, 
        "baseAsset": "bch", 
        "baseAssetPrecision": 3, 
        "quoteAsset": "cnyt", 
        "status": "trading"
    }, 
    {
        "symbol": "ltc_cnyt", 
        "quoteAssetPrecision": 2, 
        "baseAsset": "ltc", 
        "baseAssetPrecision": 3, 
        "quoteAsset": "cnyt", 
        "status": "trading"
    }
]
```

#### Field description

symbol:Transaction pair
status: Transaction pair status
baseAsset: base currency
baseAssetPrecision: Base currency precision
quoteAsset：Valuation currency
quoteAssetPrecision：Valuation currency precision
