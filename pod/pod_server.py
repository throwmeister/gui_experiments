from PodSixNet.Server import Server
from PodSixNet.Channel import Channel
from time import sleep


class ClientChannel(Channel):

    def Network(self, data):
        print('message has been sent')

    def Network_myaction(self, data):
        print(data)

    def Network_wow(self, data):
        print('i have received the data. wow!')

class GameServer(Server):

    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)

    def Connected(self, channel, addr):
        print(f'new connection {channel}')


game = GameServer(localaddr=('localhost', 5050))

while True:
    game.Pump()
    sleep(0.01)
