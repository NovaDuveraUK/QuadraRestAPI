import aiohttp
import asyncio
import hmac
import hashlib
import time
import json
from urllib.parse import urlencode


class ApiClient:
    def __init__(self, base_url, api_key, secret_key):
        self.base_url = base_url
        self.api_key = api_key
        self.secret_key = secret_key

    def _generate_signature(self, method, endpoint, params=None, body=''):
        timestamp = str(int(time.time() * 1000))
        if params:
            query_string = urlencode(params)
            endpoint_with_params = f"{endpoint}?{query_string}"
        else:
            endpoint_with_params = endpoint

        message = f"{timestamp}{method}{endpoint_with_params}{body}"
        signature = hmac.new(self.secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()
        # print("message", message)
        # print(signature)
        return timestamp, signature

    async def _request(self, method, endpoint, params=None, data=None):
        url = f"{self.base_url}{endpoint}"
        body_string = '' if not data else json.dumps(data, separators=(',', ':'))  # separators=(',', ':') removes whitespaces
        timestamp, signature = self._generate_signature(method, endpoint, params, body_string)

        headers = {
            'x-api-key': self.api_key,
            'x-signature': signature,
            'x-timestamp': timestamp,
            'Content-Type': 'application/json'
        }

        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, headers=headers, params=params, data=body_string) as response:
                response.raise_for_status()
                if response.content_type == 'application/json':
                    return await response.json()
                else:
                    return await response.text()

    async def get(self, endpoint, params=None):
        return await self._request('GET', endpoint, params=params)

    async def post(self, endpoint, params=None, data=None):
        return await self._request('POST', endpoint, params=params, data=data)

    async def put(self, endpoint, params=None, data=None):
        return await self._request('PUT', endpoint, params=params, data=data)

    async def delete(self, endpoint, params=None, data=None):
        return await self._request('DELETE', endpoint, params=params, data=data)
