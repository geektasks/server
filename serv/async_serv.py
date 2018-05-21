import asyncio
from serv.model_serv import Server

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
        #пока просто отсылаю обратно полученное сообщение, т.к. нет бд
        self.transport.write(data)

    def connection_lost(self, exc):
        print('The server closed the connection')
        for key, value in self.server.client_dict.items():
            if value == self.transport:
                self.server.client_dict.pop(key)
                break
        print(self.server.client_dict)