from abc import abstractmethod

import pygame
from cn.snowskystudio.newgame.client.gui.BaseScreen import BaseScreen
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation


class BasePageScreen(BaseScreen):
    def __init__(self, game, client) -> None:
        super().__init__(game, client)
        self.c = 0
        self.c25 = 0
        self.c50 = 0
        self.c100 = 0
        self.c150 = 0
        self.c200 = 0

        self.font16 = None
        self.font24 = None
        self.font48 = None
        self.size = (0, 0)

        self.size = (-1, -1)
        self.config = game.get_config()
        self.font_location = ResourceLocation("newgame", "font/" + self.game.get_config().get_lang() + ".ttf")
        self.bg_location = ResourceLocation("newgame", "texture/gui/background.jpg")

    @abstractmethod
    def pre_init(self) -> None:
        self.c = self.config.get_screen().get_size()[1] / 540 * self.config.get_gui()
        self.c25 = int((25 * self.c) - (25 * self.c) % 1)
        self.c50 = int((50 * self.c) - (50 * self.c) % 1)
        self.c100 = int((100 * self.c) - (100 * self.c) % 1)
        self.c150 = int((150 * self.c) - (150 * self.c) % 1)
        self.c200 = int((200 * self.c) - (200 * self.c) % 1)

        self.font16 = pygame.font.Font(self.font_location.get_full_path(), int(16 * self.c))
        self.font24 = pygame.font.Font(self.font_location.get_full_path(), int(24 * self.c))
        self.font48 = pygame.font.Font(self.font_location.get_full_path(), int(48 * self.c))
        self.size = self.config.get_screen().get_size()
