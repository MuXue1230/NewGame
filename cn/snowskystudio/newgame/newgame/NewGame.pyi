from threading import Thread
from typing import Optional

from cn.snowskystudio.gameapi.utils.Arguments import Arguments
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.client.Client import Client
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.newgame.Config import Config
from cn.snowskystudio.newgame.test.Logger import Logger


class NewGame:
    logger: Logger
    config: Config
    client: Client
    running: bool
    
    def __init__(self, user: str, session_id: str, config: Configuration, args: Arguments): ...
    
    def start(self, screen: Screen): ...
    
    def stop(self): ...
    
    def get_config(self): ...
