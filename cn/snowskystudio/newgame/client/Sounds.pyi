from pygame.mixer import Sound

from snowskystudio.newgame.resource.ResourceLocation import ResourceLocation
from snowskystudio.newgame.test.Logger import Logger


class Sounds:
    loaded: dict[str, Sound]
    logger: Logger
    music_running: bool
    
    def __init__(self): ...
    
    def get(self, loc: ResourceLocation): ...
    
    @staticmethod
    def set_music_volume(volume: float): ...
    
    def set_volume(self, loc: ResourceLocation, volume: float): ...
    
    def music(self, loc_list: list[ResourceLocation]): ...
    
    def __music(self, loc_list: list[ResourceLocation]): ...
