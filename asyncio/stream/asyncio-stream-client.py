import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    
    print(f'[asyncio-stream-client] send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'[asyncio-stream-client] read: {data.decode()!r}')

    print(f'[asyncio-stream-client] close the connection')
    writer.close()

asyncio.run(tcp_echo_client('hello world'))