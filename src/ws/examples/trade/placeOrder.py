import asyncio
from decouple import config
from src.ws.client.wsClient import WsClient

<<<<<<< HEAD
base_url = config('WS_API_URL')
=======
base_url = config('WS_API_URL_LOCAL')
>>>>>>> 34970be815b0865a82da9c3712c9800515e4b9df
api_key = config('API_KEY')
secret_key = config('SECRET_KEY')
company_exchange_id = config('COMPANY_EXCHANGE_ID')


async def place_order():
    # Request place order payload
    payload = {
      "id": "a1b2c3d4",
      "op": "trade.place_order",
      "company_exchange_id": company_exchange_id,
      "exchange_id": "binance_spot",
      "data": {
        "market_quadra": "XRP_USDT_SPOT",
        "order_type": "limit",
        "side": "sell",
<<<<<<< HEAD
        "qty": 25,
        "qty_ccy": "XRP",
        "price": 1,
        "time_in_force": "FOK",
        # "client_order_id": "client_order_id_1234567",
=======
        "base_notional": 25,
        # "quote_notional": 100,
        "price": 0.58,
        "time_in_force": "IOC",
        # "client_order_id": "client_order_id_1234",
>>>>>>> 34970be815b0865a82da9c3712c9800515e4b9df
        # "reduce_only": false,
        # "isolated": false,
        # "position_mode": "ONE_WAY",
        # "trigger_price": 0,
        # "trigger_type": "index_price"
      }
    }

    ws_client = WsClient(base_url, api_key, secret_key, payload)
    await ws_client.connect()


if __name__ == '__main__':
    asyncio.run(place_order())
