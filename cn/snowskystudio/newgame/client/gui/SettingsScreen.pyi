from cn.snowskystudio.newgame.client.gui.BasePageScreen import BasePageScreen
from snowskystudio.newgame.client.Client import Client


class SettingsScreen(BasePageScreen):
    client: Client
    _in: bool
    
    def __init__(self, game, client): ...
    
    def start(self, screen, mixer): ...
    
    def pre_init(self): ...
    
    def __button_back(self): ...
    
    def tick(self): ...
