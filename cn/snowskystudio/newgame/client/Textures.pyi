from pygame import Surface

from snowskystudio.newgame.resource.ResourceLocation import ResourceLocation
from snowskystudio.newgame.test.Logger import Logger


class Textures:
    loaded: dict[str, Surface]
    logger: Logger
    
    def __init__(self): ...
    
    def get(self, loc: ResourceLocation): ...
