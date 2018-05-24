from repository.repository import Repository, Users

serverdb = Repository()

def registration(body):
    global client_dict
    print(body)
    if serverdb.add(Users(body['name'], body['password'])):
        message = {
            "head": {
                "type": "server response",
                "name": "registration"
            },
            "body": {
                "code": 201,
                "message": "created"
            }
        }
    else:
        message = {
            "head": {
                "type": "server response",
                "name": "registration error"
            },
            "body": {
                "code": 500,
                "message": "Error"
            }
        }
    return message

def check_user(body):
    if serverdb.get_user(body['name']):
        message = {
            "head": {
                "type": "server response",
                "name": "check_user"
            },
            "body": {
                "code": 409,
                "message": "error"
            }
        }
        return message
    else:
        message = {
            "head": {
                "type": "server response",
                "name": "check_user"
            },
            "body": {
                "code": 200,
                "message": "ok"
            }
        }
        return message
