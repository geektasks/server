import asyncio
from serv.async_serv import ServerClientProtocol

import sys
try:
#    sys.stdout=open("log.txt","w")
#    sys.stderr=open("log_err.txt","w")


    from serv.create_config import get_setting
    path = 'serv/settings.ini'
    ip = get_setting(path, 'Settings', 'ip')
    port = get_setting(path, 'Settings', 'port')

    loop = asyncio.get_event_loop()
    coro = loop.create_server(ServerClientProtocol, ip, port)
    server = loop.run_until_complete(coro)

    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
    sys.stdout.close()
    sys.stderr.close()
except Exception as err:
    print(err)
    loop.close()
    sys.stdout.close()
    sys.stderr.close()