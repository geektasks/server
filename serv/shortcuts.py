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

internal_server_error = {
    "head": {
        "type": "error",
        "name": "internal_server_error"
    },
    "body":{
        "code": 400,
        "message": "internal_server_error"
    }
}