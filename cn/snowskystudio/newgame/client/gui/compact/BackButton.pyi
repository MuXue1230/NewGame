from typing import override

from pygame import Surface

from snowskystudio.newgame.client.gui.compact.Button import Button
from snowskystudio.newgame.client.renderer.Screen import Screen


class BackButton(Button):
    @override
    def tick(self, screen: Screen) -> None: ...
    
    @override
    def set_img(self, normal: Surface, hover: None=None, pressed: None=None, disabled: None=None) -> None: ...
