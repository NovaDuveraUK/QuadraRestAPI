import asyncio
from src.quadra.trade import TradeRoutes
from decouple import config
import json

# base_url = 'http://localhost:3000'
base_url = 'https://dev-execution-api.quadra.trade'
api_key = config('API_KEY')
secret_key = config('SECRET_KEY')
exchange = 'binance_spot'


example_order = {
  "company_exchange_id": "8291f3e9-5b20-4973-b1c2-2f44bedb8c33",
  "exchange_id": "binance_spot",
  "exchange_format": 0,
  "data": {
    "symbol": "XRP_USDT_SPOT",
    "order_type": "limit",
    "side": "buy",
    "base_amount": 20,
    "price": 0.4,
    "time_in_force": "GTC",
    "post_only": True
  }
}


async def place_order():
    # Public Routes Class
    client = TradeRoutes(base_url, api_key, secret_key)
    # Get contracts
    contracts_response = await client.place_order(example_order)
    print(contracts_response)
    contracts_data = contracts_response['data']
    return contracts_data


# Example main gutter script below
if __name__ == '__main__':
    order = asyncio.run(place_order())