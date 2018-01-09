from configure import ProductionConfig
from flask import request
from functools import wraps
from api.error.views import request_not_authen, request_content_type_wrong


# decort wrapper function check conten-type
def requires_content_type(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if request.content_type != 'application/json':
            return request_content_type_wrong()
        return f(*args, **kwargs)

    return decorator


# decorter wrapper function check scret key
def requires_auth(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth = request.authorization
        if not auth or not __check_auth(auth.username, auth.password):
            return request_not_authen()
        return f(*args, **kwargs)
    return decorator


def __check_auth(username, password):
    return username == ProductionConfig.SECRET_USER and password == ProductionConfig.SECRET_KEY



