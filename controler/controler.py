from controler.registration import registration, check_user
from controler.authorization import authorization
import serv.shortcuts as shortcuts


TYPE = {
	'action':'pass',
    'action':'action'

}
NAME ={
	'registration':registration,
	'authorization':authorization,
    'check_user':check_user
}

class CControler:

    @classmethod
    def handle(cls, request):
        try:

            if request['head']['type'] in TYPE and request['head']['name'] in NAME:

                controller = NAME.get(request['head']['name'])
                return controller(request['body'])
            else:
                print('unknown_request')
                return shortcuts.unknown_request
        except Exception as err:
            print(err)
            return shortcuts.internal_server_error(err)

