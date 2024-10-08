import asyncio
from decouple import config
from src.ws.client.wsClient import WsClient

base_url = config('WS_API_URL_PROD')
api_key = config('API_KEY_PROD')
secret_key = config('SECRET_KEY_PROD')


async def listen_candles():
    # Listen child orders payload
    payload = {
        'op': 'subscribe',
        'topic_id': 'candles#1m',
        'params': [{
            'exchange_id': 'binance_usdm',
            'market_quadra': 'BTC_USDT_PERP_USDM'
        }]
    }

    ws_client = WsClient(base_url, api_key, secret_key, payload)
    await ws_client.connect()


if __name__ == '__main__':
    asyncio.run(listen_candles())
