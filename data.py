class ResponseData:
    RESPONSE_CREATE_EXISTING_USER = {
        'success': False,
        'message': 'User already exists'
    }
    RESPONSE_CREATE_USER_MISSING_FIELD = {
        'success': False,
        'message': 'Email, password and name are required fields'
    }
    RESPONSE_INVALID_LOGIN = {
        'success': False,
        'message': 'email or password are incorrect'
    }
    RESPONSE_INVALID_CREATE_ORDER = {
        'success': False,
        'message': 'Ingredient ids must be provided'
    }
    RESPONSE_ERROR_GET_ORDERS = {
        'success': False,
        'message': 'You should be authorised'
    }

class Ingredients:
    INVALID_HASH = ['61c0c5a71d1f82001bd1111', '61c0c5a71d1f82001bd7777']