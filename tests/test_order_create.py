import allure
import pytest
import requests
import data
from urls import Urls


class TestCreateOrder:

    @allure.title('Проверка создания заказа с авторизацией')
    def test_create_order_with_authorization(self, get_auth_token, get_ingredients):
        access_token = {'Authorization': get_auth_token}
        ingredients = {'ingredients': get_ingredients}

        with allure.step('Создание заказа с ингредиентами'):
            response = requests.post(Urls.ORDER_CREATE, json=ingredients, headers=access_token)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка поля success в ответе"):
            assert response.json()['success'] is True

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_without_authorization(self, get_ingredients):
        ingredients = {'ingredients': get_ingredients}

        with allure.step('Создание заказа без авторизации'):
            response = requests.post(Urls.ORDER_CREATE, json=ingredients)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 401
        with allure.step("Проверка поля success в ответе"):
            assert response.json()['success'] is False

    @pytest.mark.parametrize('hash_ingredient', data.Ingredients.INVALID_HASH)
    @allure.title('Проверка создания заказа с невалидным хэшом ингредиента')
    def test_create_order_with_invalid_hash(self, get_auth_token, hash_ingredient):
        access_token = {'Authorization': get_auth_token}
        ingredients = {'ingredients': hash_ingredient}

        with allure.step('Создание заказа с невалидным хэшом ингредиента'):
            response = requests.post(Urls.ORDER_CREATE, json=ingredients, headers=access_token)

        with allure.step("Проверяем код ответа"):
            assert response.status_code == 500

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self, get_auth_token):
        access_token = {'Authorization': get_auth_token}
        ingredients = {'ingredients': []}

        with allure.step('Создание заказа без ингредиентов'):
            response = requests.post(Urls.ORDER_CREATE, json=ingredients, headers=access_token)

        with allure.step("Проверяем код ответа"):
            assert response.status_code == 400
        with allure.step("Проверяем текст ошибки"):
            assert response.json() == data.ResponseData.RESPONSE_INVALID_CREATE_ORDER