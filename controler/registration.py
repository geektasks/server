from repository.repository import Repository, Users
from serv.shortcuts import user_created, reg_error, check_user_ok, check_user_err


serverdb = Repository()

def registration(body):
    global client_dict
    print(body)
    if serverdb.add(Users(body['name'], body['password'])):
        return reg_error
    else:
        return user_created

def check_user(body):
    if serverdb.get_user(body['name']):
        return check_user_err
    else:
        return check_user_ok
