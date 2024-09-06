from abc import abstractmethod

from pygame.mixer import Sound

from cn.snowskystudio.newgame.client.gui.BaseScreen import BaseScreen
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.newgame.NewGame import NewGame


class BaseIngameScreen(BaseScreen):
    game: NewGame
    
    def __init__(self): ...
    
    @abstractmethod
    def pre_init(self) -> None: ...
    
    @abstractmethod
    def start(self, screen: Screen, mixer: Sound) -> None: ...
    
    @abstractmethod
    def tick(self) -> None: ...
    