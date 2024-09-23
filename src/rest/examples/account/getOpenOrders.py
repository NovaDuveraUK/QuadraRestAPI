import asyncio
from src.rest.client.account import AccountRoutes
from decouple import config

base_url = config('REST_API_URL')
api_key = config('API_KEY')
secret_key = config('SECRET_KEY')
company_exchange_id = config('COMPANY_EXCHANGE_ID')


async def get_open_orders():
    # Account Routes Class
    client = AccountRoutes(base_url, api_key, secret_key)
    # Get open order params
    params = {"company_exchange_id": company_exchange_id}
    response = await client.open_orders(params)
    data = response['data']
    return data


if __name__ == '__main__':
    open_orders = asyncio.run(get_open_orders())
    print(open_orders)