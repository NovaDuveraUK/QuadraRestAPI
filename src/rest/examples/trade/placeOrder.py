import asyncio
from src.rest.client.trade import TradeRoutes
from decouple import config

base_url = config('REST_API_URL_LOCAL')
api_key = config('API_KEY')
secret_key = config('SECRET_KEY')

# Note symbol will be changing to 'market_quadra' in the future

example_order = {
  "company_exchange_id": "8366fee8-1177-4d82-b6eb-42a20d1448a4",
  "exchange_id": "binance_coinm",
  "exchange_format": 0,
  "data": {
    "market_quadra": "DOT_USD_PERP_COINM",
    "order_type": "limit",
    "side": "buy",
    "qty": 20,
    "qty_ccy": "USD",
    "price": 0.2,
    "time_in_force": "GTC",
    "post_only": True
  }
}


async def place_order():
    # Trade Routes Class
    client = TradeRoutes(base_url, api_key, secret_key)
    response = await client.place_order(example_order)
    data = response['data']
    return data


if __name__ == '__main__':
    order = asyncio.run(place_order())
    print(order)
