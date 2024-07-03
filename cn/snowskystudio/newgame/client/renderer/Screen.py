import pygame
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.client.renderer.VirtulScreen import VirtualScreen
from cn.snowskystudio.newgame.test.Logger import Logger


class Screen:
    def __init__(self, virtual: VirtualScreen) -> None:
        self.surface = None
        self.width, self.height = virtual.get_size()
        self.logger = Logger("Renderer")

    def init(self):
        self.logger.info("Renderer init")
        self.surface = pygame.display.set_mode((self.width, self.height),
                                               pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)

    def get_screen(self) -> pygame.Surface:
        return self.surface

    def set_screen(self, screen: pygame.Surface):
        self.surface = screen

    def copy(self):
        new = Screen(VirtualScreen(self.width, self.height))
        new.set_screen(self.surface.copy())
        return new
