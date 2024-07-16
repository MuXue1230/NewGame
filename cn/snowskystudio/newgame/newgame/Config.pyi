from typing import Any, Self

from pyautogui import Size

from snowskystudio.gameapi.utils.Arguments import Arguments
from snowskystudio.gameapi.utils.Configuration import Configuration
from snowskystudio.newgame.client.renderer.VirtaulScreen import VirtualScreen


class Config:
    _objects: list[str]
    
    screen: VirtualScreen
    size: Size
    gui: int
    lang: str
    
    def __init__(self, out_conf: Configuration, run_args: Arguments) -> Self: ...
    
    def get_screen(self) -> VirtualScreen: ...
    
    def get_gui(self) -> int: ...
    
    def get_lang(self) -> str: ...
    
    def get(self) -> Any: ...
