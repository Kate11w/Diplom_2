class Urls:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'
    USER_CREATE = f'{MAIN_URL}/api/auth/register'  # Создание пользователя
    USER_LOGIN = f'{MAIN_URL}/api/auth/login'  # Логин пользователя
    USER_LOGOUT = f'{MAIN_URL}/api/auth/logout'
    USER_TOKEN = f'{MAIN_URL}/api/auth/token'
    USER_DELETE = f'{MAIN_URL}/api/auth/user'
    ORDER_CREATE = f'{MAIN_URL}/api/orders'  # Создание заказа
    INGR_LIST = f'{MAIN_URL}/api/ingredients'
