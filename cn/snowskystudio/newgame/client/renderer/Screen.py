import pygame
from cn.snowskystudio.newgame.client.renderer.VirtaulScreen import VirtualScreen
from cn.snowskystudio.newgame.test.Logger import Logger


class Screen:
    def __init__(self, virtual):
        self.screen = pygame.Surface((0, 0))
        self.surface = pygame.Surface((0, 0))
        self.width, self.height = virtual.get_size()
        self.logger = Logger("Renderer")

    def init(self):
        self.logger.info("Renderer init")
        self.screen = pygame.display.set_mode((7680, 4320), pygame.DOUBLEBUF)
        self.surface = pygame.Surface((self.width, self.height))

    def get_screen(self):
        return self.surface

    def set_screen(self, screen):
        self.surface = screen

    def copy(self):
        new = Screen(VirtualScreen(self.width, self.height))
        new.set_screen(self.surface.copy())
        return new
    
    def draw(self):
        self.screen.blit(self.surface, (7680 / 2 - self.width / 2, 4320 / 2 - self.height / 2))
    
    def test(self, x1: int, y1: int, x2: int, y2: int):
        w, h = (7680 / 2 - self.width / 2, 4320 / 2 - self.height / 2)
        mouse = pygame.mouse.get_pos()
        if x1 + w <= mouse[0] <= x2 + w and y1 + h <= mouse[1] <= y2 + h:
            return True
        else:
            return False
