import requests
import allure
from urls import Urls
from faker import Faker

faker = Faker()

@allure.step('Создание пользователя')
def generate_user_data():
    return {
        "email": faker.unique.email(),
        "password": faker.password(),
        "name": faker.name()
    }

def api_create_user(user_data):
    return requests.post(Urls.USER_CREATE, json=user_data)


def api_login_user(user_data):
    return requests.post(Urls.USER_LOGIN, json={
        "email": user_data["email"],
        "password": user_data["password"]
    })


def api_delete_user(access_token):
    return requests.delete(Urls.USER_DELETE, headers={"Authorization": access_token})
