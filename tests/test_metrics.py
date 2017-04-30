from __future__ import absolute_import
import pytest

from .utils import create_test_db  # noqa
from mandroobi.models.dimensions import Account, AccountingPeriod, BusinessUnit, Currency, Driver, Scenario
from mandroobi.models.metrics import ClosingBalance, Metric


def _add_test_dimensions():
    Account.create(id='10000', description='Cash & Banks', parent_id=None, type='asset')
    Account.create(id='20000', description='Accounts Payable', parent_id=None, type='liability')
    Account.create(id='30000', description='Common Stock', parent_id=None, type='equity')
    Account.create(id='40000', description='Sales', parent_id=None, type='income')
    Account.create(id='50000', description='Cost of Sales', parent_id=None, type='expense')
    AccountingPeriod.create(id='20170101', description='Jan 2017', parent_id=None, month=1, quarter=1, year=2017)
    BusinessUnit.create(id='TESTINO_LLC', description='Testino, LLC', parent_id=None, local_currency='USD')
    Currency.create(id='USD', description='US Dollar', parent_id=None)
    Driver.create(id='NO_DRIVER', description='No Planning Driver', parent_id=None)
    Scenario.create(id='ACTUAL', description='Actual', parent_id=None)


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


@pytest.mark.usefixtures('create_test_db')
def test_closing_balance_inc_lia_equ_reverse_sign():
    _add_test_dimensions()
    closing_balance = ClosingBalance.create(
        account_id='20000',
        accounting_period_id='20170101',
        business_unit_id='TESTINO_LLC',
        driver_id='NO_DRIVER',
        currency_id='USD',
        scenario_id='ACTUAL',
        amount=100000.00
    )
    assert closing_balance.amount == -100000.00

    # Sign also gets persisted
    closing_balance = ClosingBalance.where(account_id='20000').first()
    assert closing_balance.amount == -100000.00
