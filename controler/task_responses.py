unauthorized = {
    "head": {
        "type": "server response",
        "name": "create task"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}


def task_created(task_id):
    return {
        "head": {
            "type": "server response",
            "name": "create task"
        },
        "body": {
            "code": 201,
            "message": "сreated",
            "id": "{}".format(task_id)
        }
    }
