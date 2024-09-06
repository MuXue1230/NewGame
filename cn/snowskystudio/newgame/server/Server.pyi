from cn.snowskystudio.newgame.network.ServerNetworkController import ServerNetworkController
from cn.snowskystudio.newgame.newgame.NewGame import NewGame
from cn.snowskystudio.newgame.test.Logger import Logger


class Server:
    game: NewGame
    network: ServerNetworkController
    logger: Logger
    
    def __init__(self, game: NewGame): ...
    
    def start(self): ...
    
    def tick(self): ...
    
    def stop(self): ...
