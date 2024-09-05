import asyncio
from src.quadra.public import PublicRoutes
from decouple import config

base_url = config('REST_API_URL')
api_key = config('API_KEY')
secret_key = config('SECRET_KEY')
exchange_id = 'binance_spot'
market_quadra = 'BTC_USDT_SPOT'  # Get from getContracts.py


async def get_price():
    # Public Routes Class
    client = PublicRoutes(base_url, api_key, secret_key)
    # Get prices params
    params = {"exchange_id": exchange_id, "market_quadra": market_quadra}
    response = await client.prices(params)
    data = response['data']
    return data


if __name__ == '__main__':
    price = asyncio.run(get_price())
    print(price)
