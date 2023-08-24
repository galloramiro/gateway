import pytest

from src.alpha_vantage_gateway import AlphaVantageGateway


@pytest.mark.asyncio
async def test_alpha_vantage_contract_with_correct_symbol():
    json_response = await AlphaVantageGateway.get_intra_day_values_for_symbol(symbol='AMZN')

    time_series_key = 'Time Series (5min)'
    expected_keys = ['Meta Data', time_series_key]
    assert  list(json_response.keys()) == expected_keys

    first_time_series_key = list(json_response[time_series_key].keys())[0]
    first_time_series = json_response[time_series_key][first_time_series_key]
    expected_time_series_keys = ['1. open', '2. high', '3. low', '4. close', '5. volume']

    assert list(first_time_series.keys()) == expected_time_series_keys


@pytest.mark.asyncio
async def test_alpha_vantage_contract_with_wrong_symbol():
    json_response = await AlphaVantageGateway.get_intra_day_values_for_symbol(symbol='WRONG_SYMBOL')

    expected_error_key = 'Error Message'
    assert expected_error_key in list(json_response.keys())

    expected_error = 'Invalid API call'
    assert expected_error in json_response['Error Message']
