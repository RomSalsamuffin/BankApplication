from unittest.mock import Mock, patch

from src.external_api import get_amount_rub


def test_get_amount_rub_for_rub():
    transaction = {'operationAmount': {'amount': '31957.58', 'currency': {'code': 'RUB'}}}
    assert get_amount_rub(transaction) == 31957.58


@patch('requests.get')
def test_get_amount_rub_for_usd(mocked_get):
    transaction = {'operationAmount': {'amount': '100', 'currency': {'code': 'USD'}}}
    api_response = {'result': 10294.5608}

    mocked_response = Mock()
    mocked_response.status_code = 200
    mocked_response.json.return_value = api_response

    mocked_get.return_value = mocked_response

    assert get_amount_rub(transaction) == 10294.5608
