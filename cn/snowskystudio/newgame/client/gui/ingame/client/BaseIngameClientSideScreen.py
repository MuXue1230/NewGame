from abc import abstractmethod

from cn.snowskystudio.newgame.client.gui.BaseScreen import BaseScreen


class BaseIngameScreen(BaseScreen):
    def __init__(self):
        pass
    
    @abstractmethod
    def pre_init(self):
        pass
    
    @abstractmethod
    def start(self, screen, mixer):
        pass
    
    @abstractmethod
    def tick(self):
        pass
    