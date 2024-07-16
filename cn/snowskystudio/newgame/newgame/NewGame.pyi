from threading import Thread
from typing import Optional

from snowskystudio.gameapi.utils.Arguments import Arguments
from snowskystudio.gameapi.utils.Configuration import Configuration
from snowskystudio.newgame.client.Client import Client
from snowskystudio.newgame.client.renderer.Screen import Screen
from snowskystudio.newgame.newgame.Config import Config
from snowskystudio.newgame.server.Server import Server
from snowskystudio.newgame.test.Logger import Logger


class NewGame:
    logger: Logger
    config: Config
    server: Server
    client: Client
    server_thread: Optional[Thread]
    running: bool
    
    def __init__(self, user: str, session_id: str, config: Configuration, args: Arguments): ...
    
    def start(self, screen: Screen): ...
    
    def server_tick(self): ...
    
    def stop(self): ...
    
    def get_config(self): ...
