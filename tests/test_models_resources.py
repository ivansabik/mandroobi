from __future__ import absolute_import

import pytest
from flask import Flask
from sqlalchemy_mixins import ModelNotFoundError
from werkzeug.exceptions import BadRequest, NotFound

from .utils import create_test_db  # noqa
from mandroobi.models.dimensions import Account, AccountingPeriod, BusinessUnit, Currency, Driver, Scenario
from mandroobi.models.resources import (AccountResource, AccountingPeriodResource, BusinessUnitResource,
                                        CurrencyResource, DriverResource, ScenarioResource)


@pytest.mark.usefixtures('create_test_db')
def test_get_account():
    resource = AccountResource()
    resource_dict = resource.get('10000').__dict__
    assert resource_dict['id'] == '10000'
    assert resource_dict['parent_id'] is None
    assert resource_dict['description'] == 'Cash & Banks'
    assert resource_dict['type'] == 'asset'


@pytest.mark.usefixtures('create_test_db')
def test_delete_accounting_period():
    assert AccountingPeriod.find('20170101')
    resource = AccountingPeriodResource()
    resource.delete('20170101')
    with pytest.raises(ModelNotFoundError):
        AccountingPeriod.find_or_fail('20170101')


@pytest.mark.usefixtures('create_test_db')
def test_put_business_unit():
    with pytest.raises(ModelNotFoundError):
        BusinessUnit.find_or_fail('TESTONI_LLC')
    resource = BusinessUnitResource()
    app = Flask(__name__)
    with app.test_request_context('?id=TESTONI_LLC&description=Testoni,LLC&parent_id=&local_currency=USD'):
        resource.put()
    resource = BusinessUnit.find('TESTONI_LLC')
    assert resource.id == 'TESTONI_LLC'
    assert resource.description == 'Testoni,LLC'
    assert resource.parent_id == ''
    assert resource.local_currency == 'USD'


@pytest.mark.usefixtures('create_test_db')
def test_put_account():
    resource = AccountResource()
    app = Flask(__name__)
    with app.test_request_context('?id=ID&description=NA&parent_id=&type=asset'):
        resource.put()
    assert resource


@pytest.mark.usefixtures('create_test_db')
def test_put_accounting_period():
    resource = AccountingPeriodResource()
    app = Flask(__name__)
    with app.test_request_context('?id=ID&description=NA&parent_id=&month=1&year=2002'):
        resource.put()
    assert resource


@pytest.mark.usefixtures('create_test_db')
def test_put_currency():
    resource = CurrencyResource()
    app = Flask(__name__)
    with app.test_request_context('?id=ID&description=NA&parent_id='):
        resource.put()
    assert resource


@pytest.mark.usefixtures('create_test_db')
def test_put_driver():
    resource = DriverResource()
    app = Flask(__name__)
    with app.test_request_context('?id=ID&description=NA&parent_id='):
        resource.put()
    assert resource


@pytest.mark.usefixtures('create_test_db')
def test_put_scenario():
    resource = ScenarioResource()
    app = Flask(__name__)
    with app.test_request_context('?id=ID&description=NA&parent_id='):
        resource.put()
    assert resource


@pytest.mark.usefixtures('create_test_db')
def test_patch_account():
    resource = AccountResource()
    app = Flask(__name__)
    with app.test_request_context('?description=Petty Cash'):
        resource.patch('10000')
    modified_resource = Account.find('10000')
    assert modified_resource.description == 'Petty Cash'


@pytest.mark.usefixtures('create_test_db')
def test_patch_accounting_period():
    resource = AccountingPeriodResource()
    app = Flask(__name__)
    with app.test_request_context('?description=January+2017'):
        resource.patch('20170101')
    modified_resource = AccountingPeriod.find('20170101')
    assert modified_resource.description == 'January 2017'


@pytest.mark.usefixtures('create_test_db')
def test_patch_business_unit():
    resource = BusinessUnitResource()
    app = Flask(__name__)
    with app.test_request_context('?description=Testino,Inc'):
        resource.patch('TESTINO_LLC')
    modified_resource = BusinessUnit.find('TESTINO_LLC')
    assert modified_resource.description == 'Testino,Inc'


@pytest.mark.usefixtures('create_test_db')
def test_patch_currency():
    resource = CurrencyResource()
    app = Flask(__name__)
    with app.test_request_context('?description=American+Dollars'):
        resource.patch('USD')
    modified_resource = Currency.find('USD')
    assert modified_resource.description == 'American Dollars'


@pytest.mark.usefixtures('create_test_db')
def test_patch_driver():
    resource = DriverResource()
    app = Flask(__name__)
    with app.test_request_context('?description=NA'):
        resource.patch('NO_DRIVER')
    modified_resource = Driver.find('NO_DRIVER')
    assert modified_resource.description == 'NA'


@pytest.mark.usefixtures('create_test_db')
def test_patch_scenario():
    resource = ScenarioResource()
    app = Flask(__name__)
    with app.test_request_context('?description=Real'):
        resource.patch('ACTUAL')
    modified_resource = Scenario.find('ACTUAL')
    assert modified_resource.description == 'Real'


@pytest.mark.usefixtures('create_test_db')
def test_get_non_existing_resoure():
    resource = AccountResource()
    with pytest.raises(NotFound):
        resource.get('IDONOTEXIST')


@pytest.mark.usefixtures('create_test_db')
def test_delete_non_existing_resoure():
    resource = DriverResource()
    with pytest.raises(NotFound):
        resource.delete('IDONOTEXIST')


@pytest.mark.usefixtures('create_test_db')
def test_patch_non_existing_resoure():
    resource = AccountResource()
    with pytest.raises(NotFound):
        resource.patch('IDONOTEXIST')


@pytest.mark.usefixtures('create_test_db')
def test_put_missing_param():
    resource = ScenarioResource()
    app = Flask(__name__)
    with app.test_request_context('?id=5_YEAR_PLAN_2018_01'):
        with pytest.raises(BadRequest):
            resource.put()
