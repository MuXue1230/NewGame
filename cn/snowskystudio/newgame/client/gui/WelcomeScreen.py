import PIL
import PIL.Image
import pygame
from cn.snowskystudio.newgame.client.gui.BaseScreen import BaseScreen
from cn.snowskystudio.newgame.resource.LanguageLocation import LanguageLocation
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation


class WelcomeScreen(BaseScreen):
    def __init__(self, game, client) -> None:
        super().__init__(game, client)
        self.c = 0
        self.c25 = 0
        self.c50 = 0
        self.c100 = 0
        self.c150 = 0
        self.c200 = 0

        self.font24 = None
        self.font48 = None
        self.size = (0, 0)

        self.bg = None
        self.logo = None
        self.describe = None

        self.size = (-1, -1)
        self.config = game.get_config()
        self.font_location = ResourceLocation("newgame", "font/" + self.game.get_config().get_lang() + ".ttf")
        self.logo_loc = LanguageLocation("newgame", "gui/logo")
        self.describe_loc = LanguageLocation("newgame", "gui/welcome/describe")
        self.bg_location = ResourceLocation("newgame", "texture/gui/background.jpg")
        self.logo_y = 0
        self.describe_tick = 0

    def tick(self) -> None:
        if self.size != self.config.get_screen().get_size():
            self.c = self.config.get_screen().get_size()[1] / 540 * self.config.get_gui()
            self.c25 = int((25 * self.c) - (25 * self.c) % 1)
            self.c50 = int((50 * self.c) - (50 * self.c) % 1)
            self.c100 = int((100 * self.c) - (100 * self.c) % 1)
            self.c150 = int((150 * self.c) - (150 * self.c) % 1)
            self.c200 = int((200 * self.c) - (200 * self.c) % 1)

            self.font24 = pygame.font.Font(self.font_location.get_full_path(), int(24 * self.c))
            self.font48 = pygame.font.Font(self.font_location.get_full_path(), int(48 * self.c))
            self.size = self.config.get_screen().get_size()
            self.bg = pygame.image.load(self.bg_location.get_full_path()).convert()
            img = PIL.Image.frombytes('RGBA', self.bg.get_size(), pygame.image.tostring(self.bg, 'RGBA'))
            img = img.resize(self.config.get_screen().get_size(), PIL.Image.Resampling.BICUBIC)
            self.bg = pygame.image.fromstring(img.tobytes(), self.config.get_screen().get_size(), 'RGBA').convert()
            self.logo = self.font48.render(self.trans.translate(self.logo_loc), True, (255, 255, 255))
            self.describe = self.font24.render("", True, (255, 255, 255))

            self.logo_y = 0
            self.describe_tick = 0

        self.screen.get_screen().blit(self.bg, (0, 0))

        self.screen.get_screen().blit(self.logo, ((self.config.get_screen().get_size()[0] - self.logo.get_width()) / 2,
                                                  (self.logo_y - self.logo.get_height()) / 2 - self.c25))
        self.screen.get_screen().blit(self.describe, (
        (self.config.get_screen().get_size()[0] - self.logo.get_width()) / 2 + self.c100,
        (self.config.get_screen().get_size()[1] - self.logo.get_height()) / 2 + self.c25))

        if self.logo_y + int(5 * self.c - (10 * self.c) % 1) < self.config.get_screen().get_size()[1]:
            self.logo_y += int(5 * self.c - (10 * self.c) % 1)
        else:
            self.logo_y = self.config.get_screen().get_size()[1]
            if self.describe_tick <= 20 * len(self.trans.translate(self.describe_loc)):
                self.describe_tick += 1
            if self.describe_tick % 20 == 0:
                self.describe = self.font24.render(self.trans.translate(self.describe_loc)[:self.describe_tick // 20],
                                                   True, (255, 255, 255))
