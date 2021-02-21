import pytest

#FORCE DIRECTORY
import os
absoPath = ''
for folder in str(os.path.realpath(__file__)).split('/')[:-1]:
    absoPath += folder + '/'
absoPath += '../api/'
import sys
print(absoPath)
sys.path.append(absoPath)


from app import create_app
from config import TestingConfig


@pytest.fixture
def app():
    app = create_app(config_object=TestingConfig)

    with app.app_context():
        yield app


@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client
