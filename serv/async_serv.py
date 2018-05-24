import asyncio
from serv.model_serv import Server
from serv.convert import json_to_bytes
from serv.convert import bytes_to_json
from controler.controler import msg_in, search

class ServerClientProtocol(asyncio.Protocol):
    server = Server()
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
        answer=msg_in(request)

        #Кодируем
        data=json_to_bytes(answer)

        #отсылаем ответ
        self.transport.write(data)

    def connection_lost(self, exc):
        print('The server closed the connection')
        for key, value in self.server.client_dict.items():
            if value == self.transport:
                self.server.client_dict.pop(key)
                break
        print(self.server.client_dict)