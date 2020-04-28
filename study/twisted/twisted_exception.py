from twisted.internet import reactor


def falldown():
    raise Exception('I fall down')

def upagain():
    print('I get up again')
    reactor.stop()

reactor.callWhenRunning(falldown)
reactor.callWhenRunning(upagain)

reactor.run()

