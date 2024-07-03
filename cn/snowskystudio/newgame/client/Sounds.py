import threading
from typing import overload
import pygame
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation
from cn.snowskystudio.newgame.test.Logger import Logger


class Sounds:
    def __init__(self) -> None:
        self.loaded = {}
        self.logger = Logger("Mixer")
        self.music_running = False

    def get(self, loc: ResourceLocation) -> pygame.mixer.Sound:
        if loc.get_name() in self.loaded.keys():
            return self.loaded[loc.get_name()]
        else:
            self.logger.debug("Loaded mix: %s" % loc)
            self.loaded[loc.get_name()] = pygame.mixer.Sound(loc.get_full_path())
            return self.loaded[loc.get_name()]

    @staticmethod
    def set_music_volume(volume: float) -> None:
        pygame.mixer.music.set_volume(volume)

    def set_volume(self, loc: ResourceLocation, volume: float) -> None:
        self.get(loc).set_volume(volume)

    def music(self, loc_list: list[ResourceLocation]):
        threading.Thread(target=self.__music, args=(loc_list,)).start()
        self.music_running = True

    def __music(self, loc_list: list[ResourceLocation]) -> None:
        self.logger.info("Background music is ready.")
        x = 0
        while self.music_running:
            if x >= len(loc_list):
                x = 0
            pygame.mixer.music.load(loc_list[x].get_full_path())
            pygame.mixer.music.play()
            x += 1
            while pygame.mixer.music.get_busy():
                pass
