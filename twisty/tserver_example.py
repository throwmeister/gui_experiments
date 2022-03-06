from twisted.internet.protocol import Factory
from twisted.internet import endpoints, reactor
from twisted.protocols.basic import LineReceiver

class Chat(LineReceiver):
    def __init__(self, users):
        self.users = users
        self.name = None
        self.state = 'GETNAME'

    def connectionMade(self):
        self.sendLine('What\'s your name?')

    def connectionLost(self, reason):
        if self.name in self.users:
            del self.users[self.name]

    def lineReceived(self, line):
        if self.state == 'GETNAME':
            self.handle_GETNAME(line)
        else:
            self.handle_CHAT(line)

    def handle_GETNAME(self, name):
        if name in self.users:
            self.sendLine('NAME TAKEN, PLEASE CHOSE ANOTHER')
            return
        self.sendLine(f'Welcome, {name}')
        self.name = name
        self.users[name] = self
        self.state = 'CHAT'

    def handle_CHAT(self, message):
        message = f'{self.name} {message}'
        for name, protocol in self.users.iteritems():
            if protocol != self:
                protocol.sendLine(message)

class QOTDFactory(Factory):
    protocol = Chat

    def __init__(self, quote=None):
        self.users = {}

    def buildProtocol(self, addr):
        return Chat(self.users)


endpoint = endpoints.TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(QOTDFactory('pew pew pew'))
reactor.run()
