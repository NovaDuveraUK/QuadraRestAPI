import asyncio
from src.quadra.account import AccountRoutes
from decouple import config


# base_url = 'http://localhost:3000'
base_url = 'https://dev-execution-api.quadra.trade'
api_key = config('API_KEY')
secret_key = config('SECRET_KEY')
exchange = 'binance_usdm'
company_exchange_id = 'fe4b84aa-b306-4e0d-bd3b-1ea9374ddd80'


async def get_positions():
    # Public Routes Class
    client = AccountRoutes(base_url, api_key, secret_key)
    # Get contracts
    params = {"exchange": exchange, "company_exchange_id": company_exchange_id}
    contracts_response = await client.positions(params)
    print(contracts_response)
    contracts_data = contracts_response['data']
    return contracts_data


# Example main gutter script below
if __name__ == '__main__':
    contracts = asyncio.run(get_positions())