from repository.repository import Repository

servdb = Repository()

def msg_in(request):
	print(request)
	print(request['action'])
	result = commands[request['action']](request['data'])
	return result

def check_user(data):
    if servdb.get_user(data):
        return {'No':'no'}
    else:
        return {'ok': 'ok'}


commands = {'check_user': check_user}