import threading
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.resource.Translator import Translator


class BaseScreen:
    def __init__(self, game, loc_config:Configuration, client) -> None:
        self.game = game
        self.trans = Translator(self.game.getConfig())
        self.client = client
    
    def pre_init(self) -> None:
        pass
    
    def start(self, screen:Screen) -> None:
        self.screen = screen
        threading.Thread(target=self.pre_init).start()

    def tick(self) -> None:
        pass