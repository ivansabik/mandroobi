from __future__ import absolute_import

import pytest

from .utils import create_test_db  # noqa
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


@pytest.mark.usefixtures('create_test_db')
def test_closing_balance_inc_lia_equ_reverse_sign():
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
