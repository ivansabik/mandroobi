from sqlalchemy import Column, Date, Enum, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Dimension(Base):
    __abstract__ = True

    id = Column('id', String(length=50), primary_key=True)
    description = Column('description', Text)
    parent_id = Column('parent_id', String(length=50))


class Account(Dimension):
    __tablename__ = 'accounts'
    __mapper_args__ = {'concrete': True}

    type = Column('type', Enum('asset', 'liablility', 'equity', 'income', 'expense'))


class AccountingPeriod(Dimension):
    __tablename__ = 'accounting_periods'
    __mapper_args__ = {'concrete': True}

    date = Column('date', Date)
    day = Column('day', Integer)
    month = Column('month', Integer)
    quarter = Column('quarter', Integer)
    year = Column('year', Integer)


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
