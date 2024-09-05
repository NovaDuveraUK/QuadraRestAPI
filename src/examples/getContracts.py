import asyncio
from src.quadra.public import PublicRoutes
from decouple import config


# base_url = 'http://localhost:3000'
base_url = 'https://dev-execution-api.quadra.trade'
api_key = config('API_KEY')
secret_key = config('SECRET_KEY')
exchange = 'binance_spot,binance_usdm'  # or comma seperated list


async def get_contracts():
    # Public Routes Class
    client = PublicRoutes(base_url, api_key, secret_key)
    # Get contracts
    params = {"exchange": exchange}
    contracts_response = await client.contracts(params)
    contracts_data = contracts_response['data']
    return contracts_data


# Example main gutter script below
if __name__ == '__main__':
    contracts = asyncio.run(get_contracts())
