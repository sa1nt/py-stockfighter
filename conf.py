
api_key = '4913bd4c8c2fee00cfadf26a59c66355648a1391'
api_url = 'https://api.stockfighter.io/ob/api/'


orders_url = api_url + '/venues/{venue}/stocks/{stock}/orders'

auth_header = {'X-Starfighter-Authorization': api_key}


def construct_orders_url(data_dict):
    """Expects a dict with keys 'venue' and 'stock' and returns a Starfighter API orders URL
    for stock / venue specified"""
    return orders_url.format(**data_dict)

