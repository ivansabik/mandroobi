from mandroobi.models.misc import ExchangeRate


def test_exchange_rate():
    fx_rate = ExchangeRate()
    fx_rate.iso_code = 'EUR'
    fx_rate.type = 'closing'
    fx_rate.scenario = 'ACTUAL'
