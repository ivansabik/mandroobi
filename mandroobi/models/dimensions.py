from __future__ import absolute_import

from sqlalchemy import Column, Date, Enum, event, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import ActiveRecordMixin

from ..db import session

Base = declarative_base()


class Dimension(Base, ActiveRecordMixin):
    __abstract__ = True

    id = Column('id', String(length=50), primary_key=True)
    description = Column('description', Text)
    parent_id = Column('parent_id', String(length=50))


Dimension.set_session(session)


class Account(Dimension):
    __tablename__ = 'accounts'
    __mapper_args__ = {'concrete': True}

    type = Column('type', Enum('asset', 'liability', 'equity', 'income', 'expense'))


class AccountingPeriod(Dimension):
    __tablename__ = 'accounting_periods'
    __mapper_args__ = {'concrete': True}

    date = Column('date', Date)
    day = Column('day', Integer)
    month = Column('month', Integer)
    quarter = Column('quarter', Integer)
    year = Column('year', Integer)

# TODO: validate if date or month, year
# TODO: set_month, year if date exists


@event.listens_for(AccountingPeriod, 'before_insert')
def set_quarter(mapper, connection, accounting_period):
    '''
    Sets the quarter attribute based on the given month (1 to 3: 1, 4 to 6: 2, etc)
    '''
    accounting_period.quarter = int(accounting_period.month) // 4 + 1


class BusinessUnit(Dimension):
    __tablename__ = 'business_units'
    __mapper_args__ = {'concrete': True}

    local_currency = Column('local_currency', String(length=30))


class Currency(Dimension):
    __tablename__ = 'currencies'
    __mapper_args__ = {'concrete': True}


class Driver(Dimension):
    __tablename__ = 'drivers'
    __mapper_args__ = {'concrete': True}


class Scenario(Dimension):
    __tablename__ = 'scenarios'
    __mapper_args__ = {'concrete': True}
