from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint

class Client(Protocol):
    def __init__(self):
        reactor.callInThread(self.send_data)

    def dataReceived(self, data: bytes):
        print(data.decode('utf-8'))

    def send_data(self):
        connection = True
        while connection:
            text =  input()
            if text == 'DISCONNECT':
                connection = False
                reactor.stop()
            else:
                self.transport.write(text.encode('utf-8'))



class ClientF(ClientFactory):
    def buildProtocol(self, addr):
        return Client()

endpoint = TCP4ClientEndpoint(reactor, 'localhost', 8007)
endpoint.connect(ClientF())
reactor.run()
