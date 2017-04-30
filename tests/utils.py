import pytest

from mandroobi.db import engine
from mandroobi.models import dimensions, metrics, misc


@pytest.fixture()
def create_test_db():
    dimensions.Base.metadata.drop_all(engine)
    dimensions.Base.metadata.create_all(engine)

    metrics.Base.metadata.drop_all(engine)
    metrics.Base.metadata.create_all(engine)

    misc.Base.metadata.drop_all(engine)
    misc.Base.metadata.create_all(engine)
