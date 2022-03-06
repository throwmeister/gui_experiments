from PodSixNet.Connection import connection, ConnectionListener

class NetworkListener(ConnectionListener):
    def __init__(self, host, port):
        self.Connect((host, port))

    def Network(self, data):
        print(data)

listening = NetworkListener('localhost', 5050)
for _ in range(10000):
    connection.Send({"action": "myaction", "blah": 123, "things": [3, 4, 3, 4, 7]})
    connection.Send({'action': 'wow', 'data': 3})
    connection.Pump()
    listening.Pump()
