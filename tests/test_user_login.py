import allure
import pytest
import data
from helpers import api_login_user


class TestUserLogin:

    @allure.title('Проверка успешной авторизации пользователя')
    def test_user_login(self, create_and_delete_user):
        user_data = create_and_delete_user

        with allure.step('Отправляем POST-запрос на авторизацию пользователя'):
            response = api_login_user(user_data)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка поля success в ответе"):
            assert response.json()['success'] is True
        with allure.step("Проверка данных пользователя в ответе"):
            assert response.json()['user'] == {
                'email': user_data['email'],
                'name': user_data['name']
            }

    @allure.title("Ошибка при авторизации с некорректным логином или паролем")
    @pytest.mark.parametrize("wrong_field", ["email", "password"])
    def test_login_with_wrong_credentials(self, create_and_delete_user, wrong_field):
        user_data = create_and_delete_user
        login_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        login_data[wrong_field] = "wrongvalue"

        with allure.step(f"Авторизация с неверным '{wrong_field}'"):
            response = api_login_user(login_data)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 401
        with allure.step("Проверка текста ошибки"):
            assert response.json() == data.ResponseData.RESPONSE_INVALID_LOGIN
