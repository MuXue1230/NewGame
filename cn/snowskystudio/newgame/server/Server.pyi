from snowskystudio.newgame.network.ServerNetworkController import ServerNetworkController
from snowskystudio.newgame.newgame.NewGame import NewGame
from snowskystudio.newgame.test.Logger import Logger


class Server:
    game: NewGame
    network: ServerNetworkController
    logger: Logger
    
    def __init__(self, game: NewGame): ...
    
    def start(self): ...
    
    def tick(self): ...
    
    def stop(self): ...
