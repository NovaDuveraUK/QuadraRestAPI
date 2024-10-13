import asyncio
from decouple import config
from src.ws.client.wsClient import WsClient

base_url = config('WS_API_URL')
api_key = config('API_KEY')
secret_key = config('SECRET_KEY')


async def listen_orderbooks():
    # Listen payload
    payload = {
        'op': 'subscribe',
        'topic_id': 'orderbooks', # Add suffix #<depth> for snapshot
        'params': [{
            'exchange_id': 'binance_spot',
            'market_quadra': 'BTC_USDT_SPOT'
        }]
    }

    ws_client = WsClient(base_url, api_key, secret_key, payload)
    await ws_client.connect()


if __name__ == '__main__':
    asyncio.run(listen_orderbooks())
