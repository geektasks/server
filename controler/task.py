from repository.repository import Repository
from repository.models_tasks import Tasks
from repository.models_watchers import Watchers
from repository.models_performers import Performers
from repository.models_comments import Comments
from controler.task_responses import *

rep = Repository()


def get_all_tasks(body, session_id):
    try:
        creator_id = rep.get_user_by_session_id(session_id=session_id).user_id
    except:
        return create_task_unauthorized  # изменить возврат ошибки
    else:
        tasks = rep.get_all_tasks(creator_id)
        tasks_list = {}
        for task in tasks:
            tasks_list[task.task_id] = {'name': task.name,
                                        'description': task.description,
                                        'date_reminder': task.date_reminder,
                                        'time_reminder': task.time_reminder,
                                        'date_create': task.date_create,
                                        'date_deadline': task.date_deadline}
        return tasks_get(tasks_list)


def get_task_by_id(body, session_id):
    try:
        creator_id = rep.get_user_by_session_id(session_id=session_id).user_id
    except:
        return create_task_unauthorized  # изменить возврат ошибки
    try:
        task = rep.get_task_by_task_id(body['id'])
        return task_by_id(task)

    except Exception as err:
        return task_edit_bad_request  # изменить возврат ошибки


def create_task(body, session_id):
    try:
        creator_id = rep.get_user_by_session_id(session_id=session_id).user_id
    except:
        return create_task_unauthorized
    else:
        task = Tasks(creator_id=creator_id,
                     name=body.get('name'),
                     description=body.get('description'),
                     date_create=body.get('date_create'),
                     date_deadline=body.get('date_deadline'),
                     date_reminder=body.get('date_reminder'),
                     time_reminder=body.get('time_reminder'))
        if rep.add(task):
            task_id = rep.get_task(name=body.get('name')).task_id
            return task_created(task_id)
        else:
            # сообщение об ошибке добаления задачи?
            pass


def delete_task(body, session_id):
    # TODO сделать проверку на наличие доступа к удалению Задачи
    if rep.get_user_by_session_id(session_id):
        try:
            task = rep.get_task_by_task_id(body.get('id'))
            task_id = task.task_id
        except:
            return delete_task_bad_request
        else:
            all_watchers = rep.get_all_watchers(task_id=task_id)
            all_performers = rep.get_all_performers(task_id=task_id)
            for watcher in all_watchers:
                rep.del_(watcher)
            for performer in all_performers:
                rep.del_(performer)
            if rep.del_(task):
                return delete_task_ok
            else:
                print('failed to delete task')
                pass
    else:
        return delete_task_unauthorized


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


def edit_date_reminder(body, session_id):
    try:
        creator_id = rep.get_user_by_session_id(session_id=session_id).user_id
        # TODO проверить права Пользователя на редактирование
    except:
        return edit_date_reminder_unauthorized
    try:
        task_id = rep.get_task_by_task_id(body.get('id')).task_id
        attr = 'date_reminder'
        value = body.get('date_reminder')
        if rep.edit_task(task_id, attr, value):
            return edit_date_reminder_ok
        else:
            # ???
            pass
    except Exception as err:
        rep.session.rollback()
        return edit_date_reminder_bad_request


def edit_time_reminder(body, session_id):
    try:
        creator_id = rep.get_user_by_session_id(session_id=session_id).user_id
        # TODO проверить права Пользователя на редактирование
    except:
        return edit_time_reminder_unauthorized
    try:
        task_id = rep.get_task_by_task_id(body.get('id')).task_id
        attr = 'time_reminder'
        value = body.get('time_reminder')
        if rep.edit_task(task_id, attr, value):
            return edit_time_reminder_ok
        else:
            # ???
            pass
    except Exception as err:
        rep.session.rollback()
        return edit_time_reminder_bad_request


def edit_date_deadline(body, session_id):
    try:
        creator_id = rep.get_user_by_session_id(session_id=session_id).user_id
        # TODO проверить права Пользователя на редактирование
    except:
        return edit_date_deadline_unauthorized
    try:
        task_id = rep.get_task_by_task_id(body.get('id')).task_id
        attr = 'date_deadline'
        value = body.get('date_deadline')
        if rep.edit_task(task_id, attr, value):
            return edit_date_deadline_ok
        else:
            # ???
            pass
    except Exception as err:
        rep.session.rollback()
        return edit_date_deadline_bad_request


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


def get_all_performers(body, session_id):
    if rep.get_user_by_session_id(session_id):
        performers_list = list()
        task_id = body.get('id')
        performers = rep.get_all_performers(task_id=task_id)
        for performer in performers:
            username = rep.get_user_by_user_id(performer.user_id).username
            performers_list.append(username)
        return get_all_performers_ok(performers_list)
    else:
        return get_all_performers_unauthorized


def get_all_watchers(body, session_id):
    if rep.get_user_by_session_id(session_id):
        watchers_list = list()
        task_id = body.get('id')
        watchers = rep.get_all_watchers(task_id=task_id)
        for performer in watchers:
            username = rep.get_user_by_user_id(performer.user_id).username
            watchers_list.append(username)
        return get_all_watchers_ok(watchers_list)
    else:
        return get_all_watchers_unauthorized


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


def get_comments(body, session_id):
    '''сделать ответы на ошибки'''
    try:
        user_id = rep.get_user_by_session_id(session_id).user_id
    except:
        return get_comments_unauthorized
    else:
        comments = rep.get_comments(body.get('id'))  # server_task_id
        if comments.get(body.get('id')):
            return get_comments_ok(comments)
        else:
            return get_comments_forbidden

