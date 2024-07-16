import threading
import pygame
from cn.snowskystudio.newgame.test.Logger import Logger


class Sounds:
    def __init__(self):
        self.loaded = {}
        self.logger = Logger("Mixer")
        self.music_running = False

    def get(self, loc):
        if loc.get_name() in self.loaded.keys():
            return self.loaded[loc.get_name()]
        else:
            self.logger.debug("Loaded mix: %s" % loc)
            self.loaded[loc.get_name()] = pygame.mixer.Sound(loc.get_full_path())
            return self.loaded[loc.get_name()]

    @staticmethod
    def set_music_volume(volume):
        pygame.mixer.music.set_volume(volume)

    def set_volume(self, loc, volume):
        self.get(loc).set_volume(volume)

    def music(self, loc_list):
        threading.Thread(target=self.__music, args=(loc_list,)).start()
        self.music_running = True

    def __music(self, loc_list):
        self.logger.info("Background music is ready.")
        x = 0
        try:
            while self.music_running:
                if x >= len(loc_list):
                    x = 0
                self.logger.info("Loading next music: " + loc_list[x].get_name())
                pygame.mixer.music.load(loc_list[x].get_full_path())
                pygame.mixer.music.play()
                x += 1
                while pygame.mixer.music.get_busy():
                    pass
        except pygame.error:
            pass
