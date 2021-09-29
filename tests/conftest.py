## Basic configuration of test
## Will be used to test every api endpoint per blueprint
## Note: every

import pytest

from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()