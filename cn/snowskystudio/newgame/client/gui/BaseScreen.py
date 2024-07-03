import threading
from abc import abstractmethod

from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.resource.Translator import Translator


class BaseScreen:
    def __init__(self, game, client) -> None:
        self.screen = None
        self.game = game
        self.trans = Translator(self.game.get_config())
        self.client = client

    @abstractmethod
    def pre_init(self) -> None:
        pass

    @abstractmethod
    def start(self, screen: Screen) -> None:
        self.screen = screen
        threading.Thread(target=self.pre_init).start()

    @abstractmethod
    def tick(self) -> None:
        pass
