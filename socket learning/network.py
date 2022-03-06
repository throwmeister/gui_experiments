import socket


class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname())
        self.header = 64
        self.format = 'utf-8'
        self.port = 5050
        self.addr = (self.server, self.port)
        self.discon_msg = '!DISCONNECT'
        self.id = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except socket.error:
            pass

    def send(self, msg):
        message = msg.encode(self.format)
        send_len = str(len(message)).encode(self.format)
        send_len += b' ' * (self.header - len(send_len))
        self.client.send(send_len)
        self.client.send(message)
        print(self.client.recv(2048).decode())
