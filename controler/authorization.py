from repository.repository import Repository, Users
from serv.shortcuts import auth_done, auth_err, internal_server_error
from random import randrange

serverdb = Repository()

def authorization(body):
    print(body)
    if serverdb.get_pass(body['name']) == body['password']:
        session_id = randrange(1000000000, 99999999999)
        if serverdb.set_session_id(body['name'], session_id) == 1:
            print('урра')
            return auth_done(session_id)
        else:
            print('что то пошло не так')
            return internal_server_error
    else:
        return auth_err
