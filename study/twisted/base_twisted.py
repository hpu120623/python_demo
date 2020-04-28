from twisted.internet import reactor


class CountDown:
    counter = 5

    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print(self.counter)
            self.counter -= 1
            reactor.callLater(0.5, self.count)

reactor.callWhenRunning(CountDown().count)
print('begin')
reactor.run()
print('ok')