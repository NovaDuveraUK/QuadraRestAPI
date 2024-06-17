import asyncio
from src.quadra.account import AccountRoutes
from decouple import config


base_url = 'https://dev-execution-api.quadra.trade'
api_key = config('API_KEY')
secret_key = config('SECRET_KEY')


async def get_venues():
    # Public Routes Class
    client = AccountRoutes(base_url, api_key, secret_key)
    # Get contracts
    response = await client.venues()
    data = response['data']
    return data


# Example main gutter script below
if __name__ == '__main__':
    venues = asyncio.run(get_venues())
