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

#####################################
delete_task_ok = {
    "head": {
        "type": "server response",
        "name": "delete task"
    },
    "body": {
        "code": 200,
        "message": "ok"
    }
}
delete_task_bad_request = {
    "head": {
        "type": "server response",
        "name": "delete task"
    },
    "body": {
        "code": 400,
        "message": "bad request"
    }
}

delete_task_forbidden = {
    "head": {
        "type": "server response",
        "name": "delete task"
    },
    "body": {
        "code": 403,
        "message": "forbidden"
    }
}

delete_task_unauthorized = {
    "head": {
        "type": "server response",
        "name": "delete task"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}
###########################################
def tasks_get(tasks_list):
    return {
        'head': {
            'type': 'server response',
            'name': 'get all tasks'
        },
        'body': {
            'code': 200,
            'message': tasks_list
        }
    }


def task_by_id(task):
    return {
        "head": {
            "type": "server response",
            "name": "get task by id"
        },
        'body': {
            'code': 200,
            'message': 'ok',
            'task name': task.name,
            'description': task.description,
            'date_create': task.date_create,
            'date_deadline': task.date_deadline,
            'date_reminder': task.date_reminder,
            'time_reminder': task.time_reminder
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
edit_date_reminder_unauthorized = {
    "head": {
        "type": "server response",
        "name": "edit date reminder"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}

edit_date_reminder_ok = {
    "head": {
        "type": "server response",
        "name": "edit date reminder"
    },
    "body": {
        "code": 200,
        "message": "ok"
    }
}
edit_date_reminder_bad_request = {
    "head": {
        "type": "server response",
        "name": "edit date reminder"
    },
    "body": {
        "code": 400,
        "message": "bad request"
    }
}
#####################################
edit_time_reminder_unauthorized = {
    "head": {
        "type": "server response",
        "name": "edit time reminder"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}

edit_time_reminder_ok = {
    "head": {
        "type": "server response",
        "name": "edit time reminder"
    },
    "body": {
        "code": 200,
        "message": "ok"
    }
}
edit_time_reminder_bad_request = {
    "head": {
        "type": "server response",
        "name": "edit time reminder"
    },
    "body": {
        "code": 400,
        "message": "bad request"
    }
}

####################################
edit_date_deadline_unauthorized = {
    "head": {
        "type": "server response",
        "name": "edit date deadline"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}

edit_date_deadline_ok = {
    "head": {
        "type": "server response",
        "name": "edit date deadline"
    },
    "body": {
        "code": 200,
        "message": "ok"
    }
}
edit_date_deadline_bad_request = {
    "head": {
        "type": "server response",
        "name": "edit date deadline"
    },
    "body": {
        "code": 400,
        "message": "bad request"
    }
}

#####################################
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
    "body": {
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
    "body": {
        "code": 200,
        "message": "ok"
    }
}

deny_access_bad_request = {
    "head": {
        "type": "server response",
        "name": "deny access"
    },
    "body": {
        "code": 400,
        "message": "bad request"
    }
}

deny_access_forbidden = {
    "head": {
        "type": "server response",
        "name": "deny access"
    },
    "body": {
        "code": 403,
        "message": "forbidden"
    }
}

deny_access_unauthorized = {
    "head": {
        "type": "server response",
        "name": "deny access"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}

#######################################

assign_performer_ok = {
    "head": {
        "type": "server response",
        "name": "assign performer"
    },
    "body": {
        "code": 200,
        "message": "ok"
    }
}

assign_performer_bad_request = {
    "head": {
        "type": "server response",
        "name": "assign performer"
    },
    "body": {
        "code": 400,
        "message": "bad request"
    }
}

assign_performer_unauthorized = {
    "head": {
        "type": "server response",
        "name": "assign performer"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}

assign_performer_forbidden = {
    "head": {
        "type": "server response",
        "name": "assign performer"
    },
    "body": {
        "code": 403,
        "message": "forbidden"
    }
}

#######################################
remove_performer_ok = {
    "head": {
        "type": "server response",
        "name": "remove performer"
    },
    "body": {
        "code": 200,
        "message": "ok"
    }
}
remove_performer_bad_request = {
    "head": {
        "type": "server response",
        "name": "remove performer"
    },
    "body": {
        "code": 400,
        "message": "bad request"
    }
}
remove_performer_unauthorized = {
    "head": {
        "type": "server response",
        "name": "remove performer"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}
remove_performer_forbidden = {
    "head": {
        "type": "server response",
        "name": "remove performer"
    },
    "body": {
        "code": 403,
        "message": "forbidden"
    }
}


#####################################
def get_all_performers_ok(performers_list):
    return {"head": {
        "type": "server response",
        "name": "get all performers"
    },
        "body": {
            "code": 200,
            "message": "ok",
            "performers": performers_list
        }
    }


get_all_performers_unauthorized = {
    "head": {
        "type": "server response",
        "name": "get all performers"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}


#####################################
def get_all_watchers_ok(watchers_list):
    return {"head": {
        "type": "server response",
        "name": "get all watchers"
    },
        "body": {
            "code": 200,
            "message": "ok",
            "watchers": watchers_list
        }
    }


get_all_watchers_unauthorized = {
    "head": {
        "type": "server response",
        "name": "get all watchers"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}

#####################################
change_status_task_ok = {
    "head": {
        "type": "server response",
        "name": "change status"
    },
    "body": {
        "code": 200,
        "message": "ok"
    }
}
change_status_bad_request = {
    "head": {
        "type": "server response",
        "name": "change status"
    },
    "body": {
        "code": 400,
        "message": "bad request"
    }
}
change_status_unauthorized = {
    "head": {
        "type": "server response",
        "name": "change status"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}
change_status_forbidden = {
    "head": {
        "type": "server response",
        "name": "change status"
    },
    "body": {
        "code": 403,
        "message": "forbidden"
    }
}

##############################
create_comment_ok = {
    "head": {
        "type": "server response",
        "name": "create comment"
    },
    "body": {
        "code": 200,
        "message": "ok",
        "id": "[идентификатор комментария]"
    }
}


def comment_created(comment_id):
    return {"head": {
        "type": "server response",
        "name": "create comment"
    },
        "body": {
            "code": 200,
            "message": "ok",
            "id": "{}".format(comment_id)
        }
    }


create_comment_bad_request = {
    "head": {
        "type": "server response",
        "name": "create comment"
    },
    "body": {
        "code": 400,
        "message": "bad request"
    }
}
create_comment_unauthorized = {
    "head": {
        "type": "server response",
        "name": "create comment"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}
create_comment_forbidden = {
    "head": {
        "type": "server response",
        "name": "create comment"
    },
    "body": {
        "code": 403,
        "message": "forbidden"
    }
}
#########################################

delete_comment_ok = {
    "head": {
        "type": "server response",
        "name": "delete comment"
    },
    "body": {
        "code": 200,
        "message": "ok"
    }
}
delete_comment_bad_request = {
    "head": {
        "type": "server response",
        "name": "delete comment"
    },
    "body": {
        "code": 400,
        "message": "bad request"
    }
}
delete_comment_unauthorized = {
    "head": {
        "type": "server response",
        "name": "delete comment"
    },
    "body": {
        "code": 401,
        "message": "unauthorized"
    }
}
delete_comment_forbidden = {
    "head": {
        "type": "server response",
        "name": "delete comment"
    },
    "body": {
        "code": 403,
        "message": "forbidden"
    }
}
