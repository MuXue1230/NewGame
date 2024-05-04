from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.network.ServerNetworkController import ServerNetworkController
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation
from cn.snowskystudio.newgame.resource.Translator import Translator
from cn.snowskystudio.newgame.test.Logger import Logger


class Server:
    def __init__(self, game, config:Configuration) -> None:
        self.game = game
        self.network = ServerNetworkController(self.game.getConfig())
        self.logger = Logger("Server", config)
    
    def start(self) -> None:
        self.network.start()
    
    def tick(self) -> None:
        for client in self.network.get_clients():
            pass

    def stop(self) -> None:
        self.network.stop()