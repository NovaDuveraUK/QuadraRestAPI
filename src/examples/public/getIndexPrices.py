import asyncio
from src.quadra.public import PublicRoutes
from decouple import config

base_url = config('REST_API_URL')
api_key = config('API_KEY')
secret_key = config('SECRET_KEY')


async def get_index_prices():
    # Public Routes Class
    client = PublicRoutes(base_url, api_key, secret_key)
    # Get index prices params, optional params: asset
    params = {}  # {"asset": "BTC"}
    response = await client.index_prices(params)
    data = response['data']
    return data


if __name__ == '__main__':
    index_prices = asyncio.run(get_index_prices())
    print(index_prices)
