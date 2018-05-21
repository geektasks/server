import asyncio
from serv.async_serv import ServerClientProtocol

loop = asyncio.get_event_loop()
coro = loop.create_server(ServerClientProtocol, '127.0.0.1', 7777)
server = loop.run_until_complete(coro)

print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()