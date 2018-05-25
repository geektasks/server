from controler.registration import registration, check_user
from controler.authorization import authorization
import serv.shortcuts as shortcuts


TYPE = {
	'action':'pass'
}
NAME ={
	'registration':registration,
	'authorization':authorization,
    'check_user': check_user
}

class CControler:

    @classmethod
    def handle(cls, request):
        try:
            head = request['head']
            head_type= head['type']
            head_name=head['name']
            if head_type in TYPE and head_name in NAME:
                body=request['body']
                controller = NAME.get(head_name)
                return controller(body)
            else:
                print('unknown_request')
                return shortcuts.unknown_request
        except Exception as err:
            print(err)
            return shortcuts.internal_server_error(err)

