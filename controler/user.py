from repository.repository import Repository
from repository.models_tasks import Tasks
from repository.models_watchers import Watchers
from repository.models_performers import Performers
from repository.models_comments import Comments
from serv.shortcuts import search

rep = Repository()

def search_user(body, session_id):
    try:
        creator_id = rep.get_user_by_session_id(session_id=session_id).user_id
    except Exception as err:
        print(err) # изменить возврат ошибки
    try:
        users = []
        if body['name'] == '':
            return search(users)
        for user in rep.get_all_users():
            if body['name'].lower() in user.username.lower():
                users.append(user.username)
        return search(users)

    except Exception as err:
        print(err) # изменить возврат ошибки