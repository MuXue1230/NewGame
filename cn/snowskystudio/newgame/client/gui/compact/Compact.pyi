from abc import abstractmethod
from typing import Self

from cn.snowskystudio.newgame.client.renderer.Screen import Screen


class Compact:
    x: int
    y: int
    
    def __init__(self) -> Self: ...
    
    @abstractmethod
    def tick(self, screen: Screen) -> None: ...
    
    @abstractmethod
    def pre_render(self, screen: Screen) -> None: ...
    
    @abstractmethod
    def set_pos(self, x: int, y: int) -> None: ...
