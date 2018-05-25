unknown_request = {
    "head": {
        "type": "error",
        "name": "bad_request"
    },
    "body":{
        "code": 400,
        "message": "unknown_request"
    }
}

def internal_server_error(err='internal_server_error'):
    return {
    "head": {
        "type": "error",
        "name": "internal_server_error"
    },
    "body":{
        "code": 400,
        "message": err
    }
}

user_created = {
    "head": {
        "type": "server response",
        "name": "registration"
    },
    "body": {
        "code": 201,
        "message": "created"
    }
}

reg_error = {
            "head": {
                "type": "server response",
                "name": "registration error"
            },
            "body": {
                "code": 500,
                "message": "Error"
            }
        }

check_user_err = {
    "head": {
        "type": "server response",
        "name": "check_user"
    },
    "body": {
        "code": 409,
        "message": "error"
    }
}

check_user_ok = {
            "head": {
                "type": "server response",
                "name": "check_user"
            },
            "body": {
                "code": 200,
                "message": "ok"
            }
        }