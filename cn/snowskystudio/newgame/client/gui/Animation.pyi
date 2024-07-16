from typing import Any, Callable, Self

from pygame import Surface

from snowskystudio.newgame.client.gui.BaseScreen import BaseScreen
from snowskystudio.newgame.resource.AnimationLocation import AnimationLocation
from snowskystudio.newgame.test.Logger import Logger


class Animation:
    id: AnimationLocation
    readyFunc: Callable
    tickFunc: Callable
    animation_dict: dict[Any, list[Surface]]
    
    def __init__(self, _id: AnimationLocation, logger: Logger, ready_func: Callable, tick_func: Callable) -> Self: ...
    
    def init_self(self, scr: BaseScreen) -> None: ...
    
    def get_ready(self) -> Any: ...
    
    def get_id(self) -> AnimationLocation: ...
    
    def tick(self, *args: tuple[Any], **argv: dict[str, Any]) -> Any: ...
    
    def reset(self) -> None: ...
    
    def reverse(self) -> None: ...
