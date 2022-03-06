def hello():
    print('allo')

from twisted.internet import reactor

reactor.callWhenRunning(hello)

reactor.run()