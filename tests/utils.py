import pytest

from mandroobi.db import engine
from mandroobi.models import dimensions, metrics, misc
from mandroobi.models.dimensions import Account, AccountingPeriod, BusinessUnit, Currency, Driver, Scenario


@pytest.fixture()
def create_test_db():
    dimensions.Base.metadata.drop_all(engine)
    dimensions.Base.metadata.create_all(engine)

    metrics.Base.metadata.drop_all(engine)
    metrics.Base.metadata.create_all(engine)

    misc.Base.metadata.drop_all(engine)
    misc.Base.metadata.create_all(engine)

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
