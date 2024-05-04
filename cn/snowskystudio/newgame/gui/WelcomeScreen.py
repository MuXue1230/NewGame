import PIL
import PIL.Image
import pygame
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.gui.BaseScreen import BaseScreen
from cn.snowskystudio.newgame.resource.LanguageLocation import LanguageLocation
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation


class WelcomeScreen(BaseScreen):
    def __init__(self, game, loc_config: Configuration, client) -> None:
        super().__init__(game, loc_config, client)
        self.size = (-1, -1)
        self.config = game.getConfig()
        self.font_location = ResourceLocation("newgame", "font/"+self.game.getConfig().getLang()+".ttf")
        self.logo_loc = LanguageLocation("newgame", "gui/logo")
        self.describe_loc = LanguageLocation("newgame", "gui/welcome/describe")
        self.bg_location = ResourceLocation("newgame", "texture/gui/background.jpg")
    
    def tick(self) -> None:
        if self.size != self.config.getScreen().getSize():
            self.c = self.config.getScreen().getSize()[1] / 540 * self.config.getGUI()
            self.c25 = int((25*self.c) - (25*self.c)%1)
            self.c50 = int((50*self.c) - (50*self.c)%1)
            self.c100 = int((100*self.c) - (100*self.c)%1)
            self.c150 = int((150*self.c) - (150*self.c)%1)
            self.c200 = int((200*self.c) - (200*self.c)%1)

            self.font24 = pygame.font.Font(self.font_location.get_full_path(), int(24*self.c))
            self.font48 = pygame.font.Font(self.font_location.get_full_path(), int(48*self.c))
            self.size = self.config.getScreen().getSize()
            self.bg = pygame.image.load(self.bg_location.get_full_path()).convert()
            img = PIL.Image.frombytes('RGBA', self.bg.get_size(), pygame.image.tostring(self.bg, 'RGBA'))
            img = img.resize(self.config.getScreen().getSize(), PIL.Image.Resampling.BICUBIC)
            self.bg = pygame.image.fromstring(img.tobytes(), self.config.getScreen().getSize(), 'RGBA').convert()
            self.logo = self.font48.render(self.trans.translate(self.logo_loc), True, (255, 255, 255))
            self.describe = self.font24.render(self.trans.translate(self.describe_loc), True, (255, 255, 255))
        self.screen.getScreen().blit(self.bg, (0, 0))

        self.screen.getScreen().blit(self.logo, ((self.config.getScreen().getSize()[0]-self.logo.get_width())/2, (self.config.getScreen().getSize()[1]-self.logo.get_height())/2 - self.c25))
        self.screen.getScreen().blit(self.describe, ((self.config.getScreen().getSize()[0]-self.logo.get_width())/2 + self.c100, (self.config.getScreen().getSize()[1]-self.logo.get_height())/2 + self.c25))
