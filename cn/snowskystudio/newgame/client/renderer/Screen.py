import pygame
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.client.renderer.VirtulScreen import VirtualScreen
from cn.snowskystudio.newgame.test.Logger import Logger


class Screen:
    def __init__(self, virtual:VirtualScreen, config:Configuration) -> None:
        self.width, self.height = virtual.getSize()
        self.logger = Logger("Renderer", config)
    
    def init(self):
        self.logger.info("Renderer init")
        self.surface = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
    
    def getScreen(self) -> pygame.Surface:
        return self.surface
    
    def setScreen(self, screen:pygame.Surface):
        self.surface = screen