from twisted.internet import reactor, protocol
import dns.resolver



class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("Hello World!")
        asnA = dns.resolver.query('A')

    def dataReceived(self, data):
        print "Server said:", data
        self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print "Connection filed."
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "Connection lost."
        reactor.stop()

reactor.connectTCP("localhost", 53, EchoFactory())
reactor.run()
