from __future__ import absolute_import

import json
import pytest

from .utils import create_test_db  # noqa
from mandroobi.api import api


@pytest.mark.usefixtures('create_test_db')
def test_account():
    app = api.app.test_client()
    response = app.get('/account/10000')
    response = json.loads(response.get_data())
    assert response == {'description': 'Cash & Banks', 'id': '10000', 'parent_id': None, 'type': 'asset'}


@pytest.mark.usefixtures('create_test_db')
def test_accounting_period():
    app = api.app.test_client()
    response = app.get('/accounting_period/20170101')
    response = json.loads(response.get_data())
    assert response == {'date': None, 'day': None, 'description': 'Jan 2017', 'id': '20170101', 'month': 1, 'quarter': 1, 'year': 2017}


@pytest.mark.usefixtures('create_test_db')
def test_business_unit():
    app = api.app.test_client()
    response = app.get('/business_unit/TESTINO_LLC')
    response = json.loads(response.get_data())
    assert response == {'description': 'Testino, LLC', 'id': 'TESTINO_LLC', 'local_currency': 'USD'}


@pytest.mark.usefixtures('create_test_db')
def test_currency():
    app = api.app.test_client()
    response = app.get('/currency/USD')
    response = json.loads(response.get_data())
    assert response == {'description': 'US Dollar', 'id': 'USD'}


@pytest.mark.usefixtures('create_test_db')
def test_driver():
    app = api.app.test_client()
    response = app.get('/driver/NO_DRIVER')
    response = json.loads(response.get_data())
    assert response == {'description': 'No Planning Driver', 'id': 'NO_DRIVER'}


@pytest.mark.usefixtures('create_test_db')
def test_scenario():
    app = api.app.test_client()
    response = app.get('/scenario/ACTUAL')
    response = json.loads(response.get_data())
    assert response == {'description': 'Actual', 'id': 'ACTUAL'}
