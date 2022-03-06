from twisted.internet.protocol import Protocol, ServerFactory, Factory
from twisted.internet import endpoints, reactor

class Echo(Protocol):

    def __init__(self, users):
        self.users = users

    def connectionMade(self):
        self.users.append(self)
        self.transport.write('New connection'.encode('utf-8'))


    def dataReceived(self, data: bytes):
        for user in self.users:
            if user != self:
                user.transport.write(data)


class QOTDFactory(ServerFactory):
    def __init__(self):
        self.users = []

    def buildProtocol(self, addr):
        return Echo(self.users)

endpoint = endpoints.TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(QOTDFactory())
reactor.run()
