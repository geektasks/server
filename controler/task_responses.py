create_task_unauthorized = {
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
            "message": "created",
            "id": "{}".format(task_id)
        }
    }


###########################################
task_edit_ok = {
    "head": {
        "type": "server response",
        "name": "edit task"
    },
    "body": {
        "code": 200,
        "message": "ok"
    }
}
task_edit_bad_request = {
    "head": {
        "type": "server response",
        "name": "edit task"
    },
    "body": {
        "code": 400,
        "message": "bad request"
    }
}

task_edit_forbidden = {
    "head": {
        "type": "server response",
        "name": "edit task"
    },
    "body": {
        "code": 403,
        "message": "forbidden"
    }
}

task_edit_unauthorized = {
    "head": {
        "type": "server response",
        "name": "task edit"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}

###########################################################

grant_access_ok = {
    "head": {
        "type": "server response",
        "name": "grant access"
    },
    "body": {
        "code": 200,
        "message": "ok"
    }
}

grant_access_bad_request = {
    "head": {
        "type": "server response",
        "name": "grant access"
    },
    "body":{
        "code": 400,
        "message": "bad request"
    }
}

grant_access_forbidden = {
    "head": {
        "type": "server response",
        "name": "grant access"
    },
    "body": {
        "code": 403,
        "message": "forbidden"
    }
}

grant_access_unauthorized = {
    "head": {
        "type": "server response",
        "name": "create task"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}

###############################
deny_access_ok = {
    "head": {
        "type": "server response",
        "name": "deny access"
    },
    "body":{
        "code": 200,
        "message": "ok"
    }
}

deny_access_bad_request = {
    "head": {
        "type": "server response",
        "name": "deny access"
    },
    "body":{
        "code": 400,
        "message": "bad request"
    }
}

deny_access_forbidden = {
    "head": {
        "type": "server response",
        "name": "deny access"
    },
    "body":{
        "code": 403,
        "message": "forbidden"
    }
}


deny_access_unauthorized = {
    "head": {
        "type": "server response",
        "name": "deny access"
    },
    "body":{
        "code": 401,
        "message": "unauthorized"
    }
}