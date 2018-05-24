import asyncio

from controler.controler import CControler
from serv.convert import bytes_to_json
from serv.convert import json_to_bytes
from serv.model_serv import Server

class ServerClientProtocol(asyncio.Protocol):
    server = Server()
    controler = CControler
    def __init__(self):
        pass

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        print('Data received: {}'.format(data))
        request=bytes_to_json(data)

        #Передаем декодирование сообщение на обратоку.
        answer=self.controler.handle(request)

        #Кодируем
        data=json_to_bytes(answer)

        #отсылаем ответ
        print(answer)
        self.transport.write(data)

    def connection_lost(self, exc):
        print('The server closed the connection')
        for key, value in self.server.client_dict.items():
            if value == self.transport:
                self.server.client_dict.pop(key)
                break
        print(self.server.client_dict)

#    @property
 #   def controler(self):
#
 #       return self.controler