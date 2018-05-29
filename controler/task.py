from repository.repository import Repository
from repository.models_tasks import Tasks
from controler.task_responses import task_created, unauthorized


def create_task(body, session_id):
    # print(body)
    rep = Repository()
    try:
        creator_id = rep.get_user_by_session_id(session_id=session_id).user_id
        task = Tasks(creator_id=creator_id, name=body.get('name'), description=body.get('description'))
        rep.add(task)
        task_id = rep.get_task(name=body.get('name')).task_id
        return task_created(task_id)
    except:
        return unauthorized
