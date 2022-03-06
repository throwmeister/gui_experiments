import socket
import threading
import logging

logger = logging.getLogger('MAIN_LOGGER')
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)

HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCON_MSG = '!DISCONNECT'

def hande_client(conn, addr):
    print(f'NEW CONNECTION {addr} connected')
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            print(f'{addr} {msg}')
            if msg == DISCON_MSG:
                connected = False
            conn.send('MSG received'.encode(FORMAT))
    conn.close()


def start():
    server.listen()
    logger.info(f'LISTENING ON {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=hande_client, args=(conn, addr))
        thread.start()
        print(f'ACTIVE CONNECTIONS: {threading.active_count() - 1}')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind(ADDR)
except socket.error as a:
    logger.critical(a)

logger.info('SERVER IS STARTING')
start()
