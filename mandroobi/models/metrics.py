from __future__ import absolute_import

from sqlalchemy import Column, event, Float, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_mixins import ActiveRecordMixin, SmartQueryMixin

from .dimensions import Account, AccountingPeriod, BusinessUnit, Currency, Driver, Scenario
from ..db import session

Base = declarative_base()


class Metric(Base, ActiveRecordMixin, SmartQueryMixin):
    __tablename__ = 'metrics'

    name = Column('name', String(length=50))
    __mapper_args__ = {'polymorphic_on': name}

    account_id = Column('account', String(length=50), ForeignKey(Account.id), primary_key=True)
    accounting_period_id = Column('accounting_period', String(length=50), ForeignKey(AccountingPeriod.id), primary_key=True)
    business_unit_id = Column('business_unit', String(length=50), ForeignKey(BusinessUnit.id), primary_key=True)
    driver_id = Column('driver', String(length=50), ForeignKey(Driver.id), primary_key=True)
    currency_id = Column('currency', String(length=50), ForeignKey(Currency.id), primary_key=True)
    scenario_id = Column('scenario', String(length=50), ForeignKey(Scenario.id), primary_key=True)
    amount = Column('amount', Float)

    account = relationship(Account, uselist=False)
    accounting_period = relationship(AccountingPeriod, uselist=False)
    business_unit = relationship(BusinessUnit, uselist=False)
    currency = relationship(Currency, uselist=False)
    driver = relationship(Driver, uselist=False)
    scenario = relationship(Scenario, uselist=False)


Metric.set_session(session)


class ClosingBalance(Metric):
    __mapper_args__ = {'polymorphic_identity': 'closing_balance'}


@event.listens_for(ClosingBalance, 'before_insert')
def add_sign(mapper, connection, target):
    account = Account.find_or_fail(target.account_id)
    if account.type in ('liability', 'equity', 'income'):
        target.amount *= -1
