from typing import Dict

from src.base_gateway import BaseGateway
from src.config import ALPHA_URL, ALPHA_API_KEY

class AlphaVantageGateway(BaseGateway):
    _BASE_URL = f'{ALPHA_URL}query?'
    _API_KEY = ALPHA_API_KEY

    @classmethod
    async def get_intra_day_values_for_symbol(cls, symbol: str) -> Dict:
        """Get intra day request for a specific symbol

        Args:
            symbol (str): string representing the active symbol excamples
            'FB', 'AAPL', 'MSFT', 'GOOGL', 'AMZN'

        Returns:
            requests.Response: Response with the data for the symbol
        """
        params = dict(
            function='TIME_SERIES_INTRADAY',
            symbol=symbol,
            interval='5min',
            outputsize='compact',
            apikey=cls._API_KEY,
        )
        # TODO: manage error, response code and do proper logging
        status_code, json_response = await cls.get(cls._BASE_URL, params=params)
        return json_response