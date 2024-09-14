import threading
from abc import abstractmethod

from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.resource.Translator import Translator


class BaseScreen:
    def __init__(self, game, client):
        self.screen = Screen
        self.game = game
        self.trans = Translator(self.game.get_config())
        self.client = client
        
        self.done = False
        self.running = False

    @abstractmethod
    def pre_init(self):
        pass
    
    def __pre_init(self):
        try:
            self.pre_init()
        except KeyboardInterrupt:
            pass

    @abstractmethod
    def start(self, screen, mixer):
        self.screen = screen
        threading.Thread(target=self.__pre_init).start()

    @abstractmethod
    def tick(self):
        pass
    
    def is_done(self):
        return self.done
    
    def is_running(self):
        return self.running
    
    def activate(self) -> None:
        self.running = True
    
    def deactivate(self) -> None:
        self.running = False
