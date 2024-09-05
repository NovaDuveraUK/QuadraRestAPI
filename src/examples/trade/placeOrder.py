import asyncio
from src.quadra.trade import TradeRoutes
from decouple import config

base_url = config('REST_API_URL')
api_key = config('API_KEY')
secret_key = config('SECRET_KEY')

# Note symbol will be changing to 'market_quadra' in the future

example_order = {
  "company_exchange_id": "1097f8ca-7819-41d7-8145-7b7e436d7c38",
  "exchange_id": "binance_usdm",
  "exchange_format": 0,
  "data": {
    "symbol": "XRP_USDT_PERP_USDM",
    "order_type": "limit",
    "side": "buy",
    "base_amount": 20,
    "price": 0.4,
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
