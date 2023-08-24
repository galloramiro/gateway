import pytest

from src.base_gateway import BaseGateway


def test_asd1():
    v = ""
    pass

@pytest.mark.asyncio
async def test_asd():
    status_code, json_response = await BaseGateway.get(url='https://google.com')

    assert status_code ==  200
    assert json_response