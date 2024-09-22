# Quadra Unified REST API Examples

## Prerequisites
- Python 3.10 or higher
- pip
- Quadra API Keys
- Quadra API URL
- Quadra API Documentation: https://unified-api.quadra.trade/docs

## Installation
```bash
pip install python-decouple aiohttp asyncio pandas
```

## General Usage

### Public Endpoints
1. Get supported venues from `src/examples/public/getVenues.py`.
2. Get supported contracts from `src/examples/public/getContracts.py`.
3. Use `exchange_id` and `market_quadra` fields generally to query the public endpoints.

### Account Endpoints
1. Get your own venues from `src/examples/account/getVenues.py`.
2. Use `company_exchange_id` (and `vault_id`) fields to query the account endpoints.

