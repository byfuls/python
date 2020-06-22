import asyncio
import multiprocessing
import time

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f'[asyncio-stream-server] read: {message!r} from {addr!r}')

    print(f'[asyncio-stream-server] send: {message!r}')
    writer.write(data)
    await writer.drain()

    print(f'[asyncio-stream-server] close the connection')
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'[asyncio-stream-server] serving on {addr}')

    async with server:
        await server.serve_forever()


# processRun online
print(f'[processRun] ready')
def processRun():
    while True:
        print(f'[processRun] running ... ')
        time.sleep(1)

processManager = multiprocessing.Process(target=processRun)
processManager.start()
print(f'[processRun] end')

asyncio.run(main())