from repository.repository import Repository
from repository.models_tasks import Tasks
from repository.models_watchers import Watchers
from repository.models_performers import Performers
from repository.models_comments import Comments
from controler.task_responses import *

rep = Repository()


def create_task(body, session_id):
    try:
        creator_id = rep.get_user_by_session_id(session_id=session_id).user_id
    except:
        return create_task_unauthorized
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
        task_id = rep.get_task_by_task_id(body.get('id')).task_id
        attr = 'description' if 'description' in body else 'name'
        value = body.get('description') if 'description' in body else body.get('name')
        if rep.edit_task(task_id, attr, value):
            return task_edit_ok
        else:
            # ???
            pass
    except Exception as err:
        rep.session.rollback()
        return task_edit_bad_request


def grant_access(body, session_id):
    # TODO сделать проверку на наличие доступа к предоставлению прав
    if rep.get_user_by_session_id(session_id):  # проверяем авторизацию пользователя, актуальность сессии
        try:
            task_id = rep.get_task_by_task_id(body.get('id')).task_id
            user_id = rep.get_user(body.get('user')).user_id
        except:
            return grant_access_bad_request
        else:
            if not rep.session.query(Watchers).filter_by(task_id=task_id, user_id=user_id).first():
                watcher = Watchers(task_id=task_id, user_id=user_id)
                if rep.add(watcher):
                    return grant_access_ok
            else:
                # сообщение пользователь уже в списке?
                pass
    else:
        return grant_access_unauthorized


def deny_access(body, session_id):
    # TODO сделать проверку на наличие доступа к предоставлению прав
    if rep.get_user_by_session_id(session_id):
        try:
            task_id = rep.get_task_by_task_id(body.get('id')).task_id
            user_id = rep.get_user(body.get('user')).user_id
        except:
            return deny_access_bad_request
        else:
            wathcher = rep.get_watcher(task_id, user_id)
            if rep.del_(wathcher):
                return deny_access_ok
            else:
                # сообщение, что пользователя нет в списке доступа??
                pass
    else:
        return deny_access_unauthorized


def assign_performer(body, session_id):
    # TODO сделать проверку на наличие доступа к назначению исполнителя
    if rep.get_user_by_session_id(session_id):  # проверяем авторизацию пользователя, актуальность сессии
        try:
            task_id = rep.get_task_by_task_id(body.get('id')).task_id
            user_id = rep.get_user(body.get('user')).user_id if 'user' in body else rep.get_user_by_session_id(
                session_id).user_id
        except:
            return assign_performer_bad_request
        else:
            if not rep.session.query(Performers).filter_by(task_id=task_id, user_id=user_id).first():
                performer = Performers(task_id=task_id, user_id=user_id)
                if rep.add(performer):
                    return assign_performer_ok
            else:
                # сообщение пользователь уже в списке?
                pass
    else:
        return assign_performer_unauthorized


def remove_performer(body, session_id):
    # TODO сделать проверку на наличие доступа к удалению исполнителя
    if rep.get_user_by_session_id(session_id):
        try:
            task_id = rep.get_task_by_task_id(body.get('id')).task_id
            user_id = rep.get_user(body.get('user')).user_id if 'user' in body else rep.get_user_by_session_id(
                session_id).user_id
        except:
            return remove_performer_bad_request
        else:
            performer = rep.get_performer(task_id, user_id)
            if rep.del_(performer):
                return remove_performer_ok
            else:
                pass
    else:
        return remove_performer_unauthorized


def change_status(body, session_id):
    # TODO сделать проверку на права пользователя менять статус задачи
    # TODO сделать проверку на значение поля статус {0, 1, 2}
    if rep.get_user_by_session_id(session_id):
        try:
            task_id = rep.get_task_by_task_id(body.get('id')).task_id
        except:
            return change_status_bad_request
        else:
            if rep.edit_task(task_id, 'status', body.get('status')):
                return change_status_task_ok
            else:
                pass
    else:
        return change_status_unauthorized


def create_comment(body, session_id):
    # TODO сделать проверку на право пользователя оставить комментарий
    try:
        user_id = rep.get_user_by_session_id(session_id).user_id
    except:
        return create_comment_unauthorized
    else:
        try:
            task_id = rep.get_task_by_task_id(body.get('id')).task_id
        except:
            return create_comment_bad_request
        else:
            comment = Comments(user_id=user_id, task_id=task_id, text=body.get('text'), time=body.get('time'))
            if rep.add(comment):
                comment_id = rep.get_comment(user_id=user_id, task_id=task_id, time=body.get('time')).comment_id
                return comment_created(comment_id)
            else:
                pass


def delete_comment(body, session_id):
    try:
        user_id = rep.get_user_by_session_id(session_id).user_id
    except:
        return delete_comment_unauthorized
    else:
        comment = rep.get_comment_by_comment_id(body.get('id'))
        if comment.comment_id and comment.task_id:
            if comment.user_id == user_id:
                if rep.del_(comment):
                    return delete_comment_ok
            else:
                return delete_comment_forbidden
        else:
            return delete_comment_bad_request
