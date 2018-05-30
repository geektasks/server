from repository.repository import Repository
from repository.models_tasks import Tasks
from repository.models_watchers import Watchers
from controler.task_responses import task_created, unauthorized

rep = Repository()


def create_task(body, session_id):
    # print(body)
    try:
        creator_id = rep.get_user_by_session_id(session_id=session_id).user_id
    except:
        return unauthorized
    else:
        task = Tasks(creator_id=creator_id, name=body.get('name'), description=body.get('description'))
        if rep.add(task):
            task_id = rep.get_task(name=body.get('name')).task_id
            return task_created(task_id)
        else:
            # сообщение об ошибке добаления задачи?
            pass


def edit_task(body, session_id):
    try:
        creator_id = rep.get_user_by_session_id(session_id=session_id).user_id
        # TODO проверить права Пользователя на редактирование
    except:
        return task_edit_unauthorized
    try:
        # TODO перенести функционал редактирование в Repository
        task = rep.get_task_by_task_id(body.get('id'))
        attr = 'description' if 'description' in body else 'name'
        value = body.get('description') if 'description' in body else body.get('name')
        if rep.edit_task(task.task_id, attr, value):
            return task_edit_ok
        else:
            # ???
            pass
    except Exception as err:
        rep.session.rollback()
        return user_or_task_not_found


def grant_access(body, session_id):
    # TODO сделать проверку на наличие доступа к предоставлению прав
    task_id = body.get('id')
    try:
        task = rep.get_task_by_task_id(task_id)
        user = rep.get_user(body.get('user'))
    except:
        return user_or_task_not_found
    else:
        if rep.get_user_by_session_id(session_id):  # проверяем авторизацию пользователя, актуальность сессии
            if not rep.session.query(Watchers).filter_by(task_id=task.task_id, user_id=user.user_id).first():
                watcher = Watchers(task_id=task.task_id, user_id=user.user_id)
                if rep.add(watcher):
                    return grant_access_ok
            else:
                # сообщение пользователь уже в списке?
                pass
        else:
            return grant_access_unauthorized
