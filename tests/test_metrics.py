from mandroobi.models.metrics import ClosingBalance, Metric


def test_metric():
    metric = Metric()
    metric.account_id = '50000'
    metric.accounting_period_id = '19991231'
    metric.business_unit_id = 'NORTH'
    metric.driver_id = 'SALES_VOLUME'
    metric.currency_id = 'NO_CURRENCY'
    metric.scenario_id = 'PLAN'


def test_closing_balance():
    closing_balance = ClosingBalance()
    closing_balance.closing_balance = 1000.50
