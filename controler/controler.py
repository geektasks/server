from controler.registration import registration, check_user
from controler.authorization import authorization
from controler.user import search_user
from controler.task import create_task, edit_task, get_task_by_id, grant_access, deny_access, assign_performer, \
    remove_performer, \
    change_status, create_comment, delete_comment, get_all_tasks, get_all_performers, get_all_watchers, \
    edit_date_reminder, edit_time_reminder, delete_task
import serv.shortcuts as shortcuts

TYPE = {
    'action': 'pass',
    'action': 'action'

}
NAME = {
    'registration': registration,
    'authorization': authorization,
    'check user': check_user,
    'create task': create_task,
    'edit task': edit_task,
    'get all tasks': get_all_tasks,
    'get task by id': get_task_by_id,
    'grant access': grant_access,
    'deny access': deny_access,
    'assign performer': assign_performer,
    'remove performer': remove_performer,
    'change status': change_status,
    'create comment': create_comment,
    'delete comment': delete_comment,
    'search user': search_user,
    'get all performers': get_all_performers,
    'get all watchers': get_all_watchers,
    'edit date reminder': edit_date_reminder,
    'edit time reminder': edit_time_reminder,
    'delete task': delete_task
}


class CControler:

    @classmethod
    def handle(cls, request):
        try:

            if request['head']['type'] in TYPE and request['head']['name'] in NAME:
                controller = NAME.get(request['head']['name'])

                if 'session_id' not in request['head']:
                    return controller(request['body'])
                else:
                    return controller(request['body'], request['head']['session_id'])

            else:
                print('unknown_request')
                return shortcuts.unknown_request
        except Exception as err:
            print(err)
            return shortcuts.internal_server_error(err)
