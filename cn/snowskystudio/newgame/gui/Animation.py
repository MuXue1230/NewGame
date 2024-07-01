from typing import Any, Callable
from cn.snowskystudio.newgame.gui.BaseScreen import BaseScreen
from cn.snowskystudio.newgame.resource.AnimationLocation import AnimationLocation
from cn.snowskystudio.newgame.test.Logger import Logger


class Animation:
    def __init__(self, id:AnimationLocation, logger:Logger, readyFunc:Callable, tickFunc:Callable):
        self.id = id
        self.active = False
        self.finish = False
        self.animation_time = 0
        self.logger = logger
        self.tickFunc = tickFunc
        self.readyFunc = readyFunc
    
    def init_self(self, scr:BaseScreen):
        self.screen = scr
    
    def get_ready(self) -> Any:
        return self.readyFunc(self)

    def get_id(self) -> AnimationLocation:
        return self.id
    
    def tick(self, *args, **argv):
        return self.tickFunc(self, *args, **argv)

    def set_active(self, active:bool) -> None:
        self.active = active
    
    def finished(self) -> bool:
        return self.finish