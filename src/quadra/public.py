from src.quadra.apiClient import ApiClient


class PublicRoutes(ApiClient):
    async def index_prices(self, params):
        return await self.get('/api/v1/public/index_prices', params)

    async def prices(self, params):
        return await self.get('/api/v1/public/prices', params)

    async def contracts(self, params):
        return await self.get('/api/v1/public/contracts', params)

