from typing import Callable, Optional, Self

from pygame import Surface
from pygame.mixer import Sound

from cn.snowskystudio.newgame.client.gui.compact.Compact import Compact
from cn.snowskystudio.newgame.client.renderer.Screen import Screen


class Button(Compact):
    NORMAL: int
    HOVER: int
    PRESSED: int
    DISABLED: int
    
    status: int
    normal: Optional[Surface]
    hover: Optional[Surface]
    pressed: Optional[Surface]
    disabled: Optional[Surface]
    text: Optional[Surface]
    
    x: int
    y: int
    
    pressing: bool
    hovering: bool
    
    hover_mix: Optional[Sound]
    pressing_mix: Optional[Sound]
    
    action: Callable
    
    def __init__(self) -> Self: ...
    
    def tick(self, screen: Screen) -> None: ...
    
    def pre_render(self, screen: Screen) -> None: ...
    
    def set_mix(self, hover_mix: Sound, pressing_mix: Sound) -> None: ...
    
    def set_img(self, normal: Surface, hover: Surface, pressed: Surface, disabled: Surface) -> None: ...
    
    def set_text(self, text: Surface) -> None: ...
    
    def set_pos(self, x: int, y: int) -> None: ...
    
    def set_action(self, action: Callable) -> None: ...
