import socket
import asyncio


HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCON_MSG = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
count = 0


async def handle_client(conn, addr):
    global count
    count += 1
    print(f'NEW CONNECTION {addr} connected')

    connected = True
    while connected:
        msg_len = await conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            print(f'{addr} {msg}')
            if msg == DISCON_MSG:
                connected = False
            conn.send('MSG received'.encode(FORMAT))
    conn.close()


async def start():
    conn, addr = server.accept()
    await asyncio.create_task(handle_client(conn, addr))
    print(f'ACTIVE CONNECTIONS: {count}')

def setup():
    while True:
        server.listen()
        asyncio.run(start())

print('SERVER IS Starting')
setup()
