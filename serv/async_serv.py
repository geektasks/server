import asyncio

from controler.controler import CControler
from serv.convert import bytes_to_json
from serv.convert import json_to_bytes
from serv.model_serv import Server
from serv.model_msg import CMessage
from serv.shortcuts import internal_server_error


class ServerClientProtocol(asyncio.Protocol):
    server = Server()
    controler = CControler

    def __init__(self):
        self.message = CMessage

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')

        print('Connection from {}'.format(peername))
        self.transport = transport
        # self.transport.write('Hello')

    def data_received(self, data):
        print('Data received: {}'.format(data))

        try:
            message = bytes_to_json(data)
            # Передаем декодирование сообщение на обратоку.
            answer = self.controler.handle(message)

            # Кодируем
            data = json_to_bytes(answer)

            # отсылаем ответ
            print('Answer: ', answer)
            self.transport.write(data)
            print('Data sent: {}'.format(answer))
        except Exception as err:
            json = internal_server_error(err)
            answer = json_to_bytes(json)
            self.transport.write(answer)
            print('Data sent: {}'.format(answer))
            print(err)
            return err

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
