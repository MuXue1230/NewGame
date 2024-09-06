from pygame import Surface

from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation
from cn.snowskystudio.newgame.test.Logger import Logger


class Textures:
    loaded: dict[str, Surface]
    logger: Logger
    
    def __init__(self): ...
    
    def get(self, loc: ResourceLocation): ...
