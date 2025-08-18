import allure
import pytest
import data
from helpers import api_create_user, generate_user_data


class TestUserCreate:

    @allure.title('Проверка успешного создания пользователя')
    def test_user_create(self, new_user_data):
        with allure.step('Создание пользователя'):
            response = api_create_user(new_user_data)

        with allure.step('Проверка кода ответа и данных пользователя'):
            assert response.status_code == 200
            assert response.json()['user'] == {
                'email': new_user_data['email'],
                'name': new_user_data['name']
            }

    @allure.title('Проверка создания уже созданного пользователя')
    def test_create_user_duplicate(self, create_and_delete_user):
        user_data = create_and_delete_user
        with allure.step('Попытка повторного создания пользователя'):
            response = api_create_user(user_data)

        with allure.step('Проверка кода и ответа на дубликат пользователя'):
            assert response.status_code == 403
            assert response.json() == data.ResponseData.RESPONSE_CREATE_EXISTING_USER

    @allure.title('Проверка создания пользователя без указания одного из полей')
    @pytest.mark.parametrize('missing_field', ['email', 'password', 'name'])
    def test_create_user_with_missing_field(self, missing_field):
        user_data = generate_user_data()
        user_data.pop(missing_field)

        with allure.step(f'Создание пользователя без {missing_field}'):
            response = api_create_user(user_data)

        with allure.step('Проверка кода и ответа при отсутствии одного из полей'):
            assert response.status_code == 403
            assert response.json() == data.ResponseData.RESPONSE_CREATE_USER_MISSING_FIELD
