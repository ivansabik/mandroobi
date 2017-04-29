from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# TODO: read from config, env var here and in alembic.ini
engine = create_engine('sqlite:////tmp/mandroobi.db', echo=True)
session = scoped_session(sessionmaker(bind=engine, autocommit=True))
