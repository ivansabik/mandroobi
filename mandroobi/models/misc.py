from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ExchangeRate(Base):
    __tablename__ = 'exchange_rates'

    iso_code = Column('iso_code', String(length=3), primary_key=True)
    scenario_id = Column('id', String(length=50), ForeignKey('scenarios.id'),)
    type = Column('type', String(length=3))
