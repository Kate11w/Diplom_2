import requests
import random
import pytest

from urls import Urls
from helpers import generate_user_data, api_create_user, api_login_user, api_delete_user


@pytest.fixture
def new_user_data():
    return generate_user_data()


@pytest.fixture
def create_and_delete_user():
    user_data = generate_user_data()
    api_create_user(user_data)
    yield user_data

    login_response = api_login_user(user_data)
    if login_response.status_code == 200:
        token = login_response.json()["accessToken"]
        api_delete_user(token)


@pytest.fixture()
def get_ingredients():
    response = requests.get(Urls.INGR_LIST)
    response.raise_for_status()
    all_ingredients = [item['_id'] for item in response.json()['data']]
    count = random.randint(1, 15)
    return random.sample(all_ingredients, count)

@pytest.fixture(scope="session")
def get_auth_token():
    user_data = generate_user_data()
    api_create_user(user_data)
    response = api_login_user(user_data)
    return response.json().get('accessToken')
