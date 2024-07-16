from cn.snowskystudio.newgame.network.ServerNetworkController import ServerNetworkController
from cn.snowskystudio.newgame.test.Logger import Logger


class Server:
    def __init__(self, game):
        self.game = game
        self.network = ServerNetworkController()
        self.logger = Logger("Server")

    def start(self):
        self.network.start()

    def tick(self):
        for client in self.network.get_clients():
            pass

    def stop(self):
        self.network.stop()
