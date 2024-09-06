import pygame

from cn.snowskystudio.newgame.test.Logger import Logger


class Textures:
    def __init__(self):
        self.loaded = {}
        self.logger = Logger("Texture")
    
    def get(self, loc):
        if loc.get_name() in self.loaded.keys():
            return self.loaded[loc.get_name()]
        else:
            self.logger.debug("Loaded texture: %s" % loc)
            self.loaded[loc.get_name()] = pygame.image.load(loc.get_full_path()).convert_alpha()
            return self.loaded[loc.get_name()]
