from typing import Self

from pygame import Surface

from snowskystudio.newgame.client.renderer.VirtaulScreen import VirtualScreen
from snowskystudio.newgame.test.Logger import Logger


class Screen:
    logger: Logger
    width: int
    height: int
    surface: Surface
    screen: Surface
    
    def __init__(self, virtual: VirtualScreen) -> Self: ...
    
    def init(self) -> None: ...
    
    def get_screen(self) -> Surface: ...
    
    def set_screen(self, screen: Surface) -> None: ...
    
    def copy(self) -> Screen: ...
    
    def draw(self) -> None: ...
    
    def test(self, x1: int, y1: int, x2: int, y2: int) -> bool: ...
