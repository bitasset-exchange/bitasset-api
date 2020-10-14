Chinese Documents [click here](https://github.com/bitasset-exchange/bitasset-api/wiki/rest-api_CN)
# Public API for BitAsset 

* Specific error codes and messages：please refer to "errors.md"
* Return format：{"code":0,"msg":"success","data": null} code=Error code，0=Correct，others are unauthorized，msg=Error message，data=Return data
* Signature verification：
Verify the URL parameters in below APIs,according to the ascending order, array the URL parameters. 
Limit：2s each time for signature verification
Example:

Format：apiAccessKey=Your_apiAccessKey&apiTimeStamp=Current time 

* Encrypt your secretkey by SHA, 
* Encrypt the secretkey and the above-mentioned URL string to apiSign by HmacSHA256 

Request

api domin(/apiAccessKey=your_apiAccessKey&apiTimeStamp=Current time&apiSign=Request Encrypted Signature String&apiSign


* apiAccessKey：AccessKey
* apiTimeStamp：Current timestamp(Keep the same as server time, or within 30s)

# BitAsset API （2018-07-18）

## 1.1 Rest API，No Authorization Required

### 1.1.1 Get Currency Pair

#### Request

GET /v1/cash/public/symbols

#### Response

{
    "code": 0,
    "data": [
        {
            "amountDecimal": 6,
            "baseCurrency": "BTC",
            "id": 1,
            "makerFeeRatio": 0.001,
            "name": "ETH-BTC",
            "priceDecimal": 3,
            "quoteCurrency": "ETH",
            "takerFeeRatio": 0.002
        },
        {
            "amountDecimal": 6,
            "baseCurrency": "BTC",
            "id": 2,
            "makerFeeRatio": 0.001,
            "name": "EOS-BTC",
            "priceDecimal": 3,
            "quoteCurrency": "EOS",
            "takerFeeRatio": 0.002
        },
        {
            "amountDecimal": 6,
            "baseCurrency": "BTC",
            "id": 3,
            "makerFeeRatio": 0.001,
            "name": "NEO-BTC",
            "priceDecimal": 3,
            "quoteCurrency": "NEO",
            "takerFeeRatio": 0.002
        }
    ],
    "msg": "success"
}

* amountDecimal:AmountDecimal
* priceDecimal：PriceDecimal
* baseCurrency：BaseCurrency
* quoteCurrency：QuoteCurrency
* id：Currency pair ID
* name：Currency pair name
* takerFeeRatio：Taker fee
* makerFeeRatio：Maker fee

### 1.1.2 Get Currency Info

#### Request

GET /v1/cash/public/currencies

#### Response

{
    "code": 0,
    "data": [
        {
            "id": 1,
            "name": "ETH"
        },
        {
            "id": 2,
            "name": "BTC"
        },
        {
            "id": 3,
            "name": "EOS"
        },
        {
            "id": 4,
            "name": "NEO"
        },
        {
            "id": 5,
            "name": "ETC"
        },
        {
            "id": 6,
            "name": "BCH"
        }
    ],
    "msg": "success"
}

* id：Currency ID
* name：Currency name

### 1.1.3 Server Time

#### Request

GET /v1/cash/public/server-time

#### Response

{"code":0,"msg":"success","data":1531897504513}

### 1.1.4 Market Depth

#### Request

GET /v1/cash/public/query-depth?contractId=1

* contractId: Currency pair id

#### Response

{
    "code": 0,
    "data": {
        "asks": [
            {
                "price": "1.2",
                "quantity": "0.1"
            },
            {
                "price": "1.3",
                "quantity": "0.1"
            }
        ],
        "bids": [
            {
                "price": "1",
                "quantity": "0.06"
            },
            {
                "price": "0.9",
                "quantity": "0.5"
            },
            {
                "price": "0.8",
                "quantity": "0.3"
            },
            {
                "price": "0.7",
                "quantity": "0.1"
            }
        ],
        "contractId": 1,
        "lastPrice": "1",
        "timestamp": 1531986746968
    },
    "msg": "success"
}

* contractId：Currency pair ID
* timestamp：Timestamp
* lastPrice：LastPrice
* bids：Maximum 10 bids 
* price，quantity；Price and quantity of bid 1 to bid 10     
* asks：Maximum 10 asks  
* price，quantity；Price and quantity of ask 1 to ask 10

## 1.2 Rest API， Authorization Required

### 1.2.1 SIGNED

* 【apiAccessKey】：Your AccessKey of apiKey.
* 【apiTimeStamp】：Current timestamp(Keep the same as server time, or within 30s).
* 【apiSign】：The calculated value of signature that ensures the signature is valid and is not tampered.

### 1.2.1 Get User's Balance 

#### Request

GET /v1/cash/accounts/balance

##### URL parameters

* 【apiAccessKey】：Your AccessKey of apiKey
* 【apiTimeStamp】：Current timestamp(Keep the same as server time, or within 30s)
* 【apiSign】：The calculated value of signature that ensures the signature is valid and is not tampered.

#### Response

{
    "code": 0,
    "data": [
        {
            "available": "10000000000",
            "balance": "10000000000",
            "currency": "ETH",
            "frozen": "0"
        },
        {
            "available": "9999961151.90906",
            "balance": "9999999883.92238",
            "currency": "BTC",
            "frozen": "38732.01332"
        }
    ],
    "msg": "success"
}

* available：Available assets
* balance：Total assets
* currency：Currency name
* frozen：Frozen assets

### 1.2.2 Get Order

#### Request

GET /v1/cash/accounts/order/active

##### URL parameters

* 【apiAccessKey】：Your AccessKey of apiKey.
* 【apiTimeStamp】：Current timestamp(Keep the same as server time, or within 30s).
* 【contractId】: Currency pair Id.
* 【apiSign】：The calculated value of signature that ensures the signature is valid and is not tampered.
* 【contractId】:symbol id.

#### Response

{
    "code": 0,
    "data": [
        {
            "clientOrderId": "f75302fc-58d1-400f-ba63-dc84bd9f1b8c",
            "contractId": 1,
            "filled": false,
            "leftQuantity": "0.1",
            "orderId": "1531965808308622",
            "orderType": "1",
            "placeTimestamp": 1531972801851103,
            "price": "0.8",
            "quantity": "0.1",
            "side": "1",
            "timeInForce": "1"
        },
        {
            "clientOrderId": "b2f07cf2-af6c-4b08-a5f7-410c28d8f28f",
            "contractId": 1,
            "filled": false,
            "leftQuantity": "0.1",
            "orderId": "1531965808308621",
            "orderType": "1",
            "placeTimestamp": 1531972746623,
            "price": "0.8",
            "quantity": "0.1",
            "side": "1",
            "timeInForce": "1"
        }
    ],
    "msg": "success"
}

* contractId：Currency pair Id
* filled: Full transaction, no(False),yes(true)
* leftQuantity：Left quantity
* orderId：Order Id
* timeInForce：1(GTC),2(IOC)，default GTC
* orderType：1(Limited price) 3(Market price)
* placeTimestamp：Order Timestamp
* price：Order price 
* quantity：Order quantity
* side：buy:1 sell:-1

### 1.2.3 Order

#### Request

POST /v1/cash/trade/order

##### URL parameters

* 【apiAccessKey】：Your AccessKey of apiKey.
* 【apiTimeStamp】：Current timestamp(Keep the same as server time, or within 30s).
* 【apiSign】：The calculated value of signature that ensures the signature is valid and is not tampered.

##### Body parameters PlaceOrderVo placeOrderVo

* contractId：Currency pair id
* side：buy:1 sell:-1
* price：Order price
* quantity：Order quantity
* orderType：1(Limited price) 3(Market price)

#### Response

{"code":0,"msg":"1531899974669469","data":""}

* msg：success--Order Id,error--error Message

### 1.2.4 Cancel Order

#### Request

POST /v1/cash/trade/order/cancel

##### URL parameters

* 【apiAccessKey】：Your AccessKey of apiKey
* 【apiTimeStamp】：Current timestamp(Keep the same as server time, or within 30s)
* 【orderId】：Cancel Order ID
* 【apiSign】：The calculated value of signature that ensures the signature is valid and is not tampered.

##### Body parameter CancelOrderVo cancelOrderVo

* contractId：Currency pair id
* originalOrderId：Order Id

#### Response

{"code":0,"msg":"success","data": null}

#### 1.2.5 Get Order Info

#### Request

GET /v1/cash/accounts/order/get

##### URL parameters

* 【apiAccessKey】：Your AccessKey of apiKey
* 【apiTimeStamp】：Current timestamp(Keep the same as server time, or within 30s)
* 【orderId】：Order ID
* 【apiSign】：The calculated value of signature that ensures the signature is valid and is not tampered.

#### Response

{
    "code": 0,
    "data": {
        "canceledQuantity": 0.200000000000000000,
        "clientOrderId": "e5cd3ed5-d711-4104-8e6f-035b0d2548da",
        "contractId": 1,
        "filledCurrency": 0E-18,
        "filledQuantity": 0E-18,
        "makerFeeRatio": 0.001000000000000000,
        "minimalQuantity": 0E-18,
        "orderType": 1,
        "price": 0.780000000000000000,
        "quantity": 0.200000000000000000,
        "side": 1,
        "status": 3,
        "stopCondition": 0,
        "stopPrice": 0E-18,
        "takerFeeRatio": 0.002000000000000000,
        "timeInForce": 1,
        "timestamp": 1531979000752,
        "userId": 6,
        "uuid": "1531965808308623"
    },
    "msg": "success"
}

* filledCurrency：Transaction amount
* filledQuantity：Transaction quantity
* canceledQuantity：Canceled quantity
* contractId：Currency pair id
* takerFeeRatio：TakerFee
* makerFeeRatio：MakerFee
* timeInForce：1(GTC),2(IOC)，default GTC
* price：Order Price
* quantity：Order quantity
* side：buy:1 sell:-1
* status：0-No transaction，1-Part transaction，2-Full transaction，3-Cancel order
* uuid：OrderId
* userId：Userid
* timestamp：Timestamp
* orderType: 1(Limited price) 3(Market price)

### 1.2.6 Get multiple orders

#### Request

POST /v1/cash/accounts/orders/get

##### URL parameters

* 【apiAccessKey】：Your AccessKey of apiKey.
* 【apiTimeStamp】：Current timestamp(Keep the same as server time, or within 30s)
* 【apiSign】：The calculated value of signature that ensures the signature is valid and is not tampered.

##### Body parameter List<String> orderList


#### Response

{
    "code": 0,
    "data": [
        {
            "canceledQuantity": 0E-18,
            "clientOrderId": "0bf9b194-1003-4849-88ab-187fc5435c0d",
            "contractId": 1,
            "filledCurrency": 0E-18,
            "filledQuantity": 0E-18,
            "makerFeeRatio": 0.001000000000000000,
            "minimalQuantity": 0E-18,
            "orderType": 1,
            "price": 1.100000000000000000,
            "quantity": 0.200000000000000000,
            "side": 1,
            "status": 0,
            "stopCondition": 0,
            "stopPrice": 0E-18,
            "takerFeeRatio": 0.002000000000000000,
            "timeInForce": 1,
            "timestamp": 1532482918468,
            "userId": 10086,
            "uuid": "1532446623381025"
        }
    ],
    "msg": "success"
}

* filledCurrency：Transaction amount
* filledQuantity：Transaction quantity
* canceledQuantity：Canceled Quantity
* contractId：Currency pair ID
* takerFeeRatio：Taker fee
* makerFeeRatio：Maker fee
* timeInForce：1(GTC),2(IOC)，default GTC
* price：Order Price
* quantity：Order quantity
* side：buy:1 sell:-1
* status：0-No transaction，1-Part transaction，2-Full transaction，3-Cancel order
* uuid：Order Id
* userId：User Id
* timestamp：Timestamp
* orderType:1(Limited price) 3(Market price)

### 1.2.7 Get User HistoryMatch

#### Request

GET 1/cash/accounts/orders/match

##### URL parameters

* 【apiAccessKey】：Your AccessKey of apiKey.
* 【apiTimeStamp】：Current timestamp(Keep the same as server time, or within 30s)
* 【contractId】：Currency pair ID
* 【startTime】：start timestamp (13)
* 【endTime】：end timestamp (13)（You need to ensure that the start time and end time are within 48 hours）   
* 【limit】：The number of queries should not be greater than 1000
* 【apiSign】：The calculated value of signature that ensures the signature is valid and is not tampered.

#### Response

`
{
    "code": 0,
    "data": [
        {
            "id": 1547466568019273
            "contract": "",   
            "contractId": 1,  
            "orderId": "1531965808308623",    
            "price": 0E-18,  
            "qty": 0E-18,     
            "commission": 0.001000000000000000,
            "commissionCurrency": "USDT",      
            "matchTime": ,                     
            "isBuyer": 1,                      
            "isMaker": 1                      
        }
    ],
    "msg": "success"
}
`

* id：match unique ID
* contract：Currency pair Name
* contractId：Currency pair ID
* orderId：Order ID
* price: match price
* qty: match quantity
* commission: fee quantity
* commissionCurrency: fee unit
* matchTime: match time
* isBuyer: is buyer? 1=is,0=no
* isMaker: is maker? 1=is,0=no

### 1.2.8 Get User HistoryMatch by orderId

#### Request

GET 1/cash/accounts/orders/matchByOrder

##### URL parameters

* 【apiAccessKey】：Your AccessKey of apiKey.
* 【apiTimeStamp】：Current timestamp(Keep the same as server time, or within 30s)
* 【orderId】：order Id
* 【apiSign】：The calculated value of signature that ensures the signature is valid and is not tampered.

#### Response

`
{
    "code": 0,
    "data": [
        {
            "id": 1547466568019273
            "contract": "",   
            "contractId": 1,  
            "orderId": "1531965808308623",    
            "price": 0E-18,  
            "qty": 0E-18,     
            "commission": 0.001000000000000000,
            "commissionCurrency": "USDT",      
            "matchTime": ,                     
            "isBuyer": 1,                      
            "isMaker": 1                      
        }
    ],
    "msg": "success"
}
`

* id：match unique ID
* contract：Currency pair Name
* contractId：Currency pair ID
* orderId：Order ID
* price: match price
* qty: match quantity
* commission: fee quantity
* commissionCurrency: fee unit
* matchTime: match time
* isBuyer: is buyer? 1=is,0=no
* isMaker: is maker? 1=is,0=no

## Public api related interface description

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
