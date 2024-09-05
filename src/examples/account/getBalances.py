import asyncio
from src.quadra.account import AccountRoutes
from decouple import config

base_url = config('REST_API_URL')
api_key = config('API_KEY')
secret_key = config('SECRET_KEY')
company_exchange_id = config('COMPANY_EXCHANGE_ID')


async def get_balances():
    # Account Routes Class
    client = AccountRoutes(base_url, api_key, secret_key)
    # Get balance params
    params = {"company_exchange_id": company_exchange_id}
    response = await client.balances(params)
    data = response['data']
    return data


if __name__ == '__main__':
    balances = asyncio.run(get_balances())
    print(balances)