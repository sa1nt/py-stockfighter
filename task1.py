import requests
import json
import conf

# curl https://api.stockfighter.io/ob/api/venues/WFDTEX/stocks/LOIM/quote
#  --header "X-Starfighter-Authorization:c837ddb76dd8d50bd23de9a4962d067698998aad"

# api_url = 'https://api.stockfighter.io/ob/api/'


account = 'PPB28750339'
venue = 'IBTHEX'
ticker = 'LML'

order_params = {
    "account": account,
    "venue": venue,
    "stock": ticker,
    "qty": 100,
    "direction": "buy",
    "orderType": "market",
    "price": 2800
}

order_url = conf.construct_orders_url({'venue': venue, 'stock': ticker})
print order_url

response = requests.post(order_url, None, order_params, headers = conf.auth_header)
print response.content
