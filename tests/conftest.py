import pytest

import views
from views import app


@pytest.fixture
def client():
    views = app({"TESTING": True})
    with views.test_client() as client:
        yield client