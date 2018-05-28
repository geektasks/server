
class CMessage:
    def __init__(self,message):

        self._message=message



    @property
    def head(self):
        return self._message['head']

    @property
    def type(self):
        return self._message['head']['type']

    @property
    def name(self):
        return self._message['head']['name']

    @property
    def session_id(self):
        return self._message['head']['session_id']


    @property
    def body(self):
        return self._message['body']

    @property
    def code(self):
        return self._message['body']['code']

    @property
    def message(self):
        return self._message['body']['message']



    @head.setter
    def head(self,val):
        self._message['head']=val

    @type.setter
    def type(self,val):
        self._message['head']['type']=val

    @name.setter
    def name(self,val):
        self._message['head']['type']=val

    @session_id.setter
    def session_id(self,val):
        self._message['head']['session_id']=val



    @body.setter
    def body(self,val):
        self._message['body']=val

    @code.setter
    def code(self,val):
        self._message['body']['code']=val

    @message.setter
    def message(self,val):
        self._message['body']['message']=val




if __name__ == '__main__':
    test=CMessage( {"head": {
        "type": "error",
        "name": "internal_server_error",
        'session_id':''
    },
    "body":{
        "code": 400,
        "message": 'none'
    }})
    print(test.code)
    test.message='sjdhfgshjdf'
    print(test.message)
