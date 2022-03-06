from twisted.internet import reactor, endpoints, protocol, defer, utils
from twisted.protocols import basic

'''
class FingerProtocol(protocol.Protocol):

    def connectionMade(self):
        self.transport.loseConnection()
'''


class FingerProtocol(basic.LineReceiver):

    def lineReceived(self, user):
        d = self.factory.getUser(user)

        def onError(err):
            return 'Internal error in server'
        d.addErrback(onError)

        def write_response(message):
            self.transport.write(message + b'\r\n')
            self.transport.loseConnection()
        d.addCallback(write_response)


class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol

    def __init__(self, users):
        self.users = users

    def getUser(self, user):
        return utils.getProcessOutput(b'finger', [user])


finger_endpoint = endpoints.serverFromString(reactor, 'tcp:5050')
finger_endpoint.listen(FingerFactory({b'alexa' : b'happy and well'}))
reactor.run()
