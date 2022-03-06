from twisted.internet.protocol import Protocol
from twisted.internet import reactor, endpoints
import sys


class Echo(Protocol):
    def dataReceived(self, data):
        sys.stdout.write(data)


class WelcomeMessage(Protocol):
    def connectionMade(self):
        self.transport.write('hi :)')
        self.transport.loseConnection()


class Greeter(Protocol):
    def sendMessage(self, msg):
        self.transport.write(f'MESSAGE {msg}\n')


def gotProtocol(p):
    p.sendMessage('Hello')
    reactor.callLater(1, p.sendMessage, 'This is sent in a second')
    reactor.callLater(2, p.transport.loseConnection)


point = endpoints.TCP4ClientEndpoint(reactor, 'localhost', 1234)
d = endpoints.connectProtocol(point, Greeter())
d.addCallback(gotProtocol)
reactor.run()
