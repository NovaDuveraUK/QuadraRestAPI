import asyncio
from src.quadra.account import AccountRoutes
from decouple import config


base_url = 'https://dev-execution-api.quadra.trade'
api_key = config('API_KEY')
secret_key = config('SECRET_KEY')
exchange = 'binance_spot'
company_exchange_id = '8291f3e9-5b20-4973-b1c2-2f44bedb8c33'


async def get_balances():
    # Public Routes Class
    client = AccountRoutes(base_url, api_key, secret_key)
    # Get contracts
    params = {"exchange": exchange, "company_exchange_id": company_exchange_id}
    contracts_response = await client.balances(params)
    print(contracts_response)
    contracts_data = contracts_response['data']
    return contracts_data


# Example main gutter script below
if __name__ == '__main__':
    contracts = asyncio.run(get_balances())