import random
import PIL
import PIL.Image
import PIL.ImageDraw
import pygame
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.network.ClientNetworkController import ClientNetworkController
from cn.snowskystudio.newgame.resource.LanguageLocation import LanguageLocation
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation
from cn.snowskystudio.newgame.resource.Translator import Translator
from cn.snowskystudio.newgame.test.Logger import Logger


class Client:
    def __init__(self, game, loc_config:Configuration) -> None:
        self.game = game
        self.network = ClientNetworkController(self.game.getConfig())
        self.logger = Logger("Client", loc_config)
        self.size = (-1, -1)
        self.loadtext_loc = LanguageLocation("newgame", "gui/load/load")
        self.tips_loc = LanguageLocation("newgame", "gui/load/tips")
        self.random_tip_locs = [
            LanguageLocation("newgame", "gui/load/tip1"),
            LanguageLocation("newgame", "gui/load/tip2"),
            LanguageLocation("newgame", "gui/load/tip3"),
            LanguageLocation("newgame", "gui/load/tip4"),
            LanguageLocation("newgame", "gui/load/tip5"),
            LanguageLocation("newgame", "gui/load/tip6"),
            LanguageLocation("newgame", "gui/load/tip7"),
            LanguageLocation("newgame", "gui/load/tip8"),
            LanguageLocation("newgame", "gui/load/tip9"),
            LanguageLocation("newgame", "gui/load/tip10"),
            LanguageLocation("newgame", "gui/load/tip11"),
            LanguageLocation("newgame", "gui/load/tip12"),
            LanguageLocation("newgame", "gui/load/tip13"),
            LanguageLocation("newgame", "gui/load/tip14"),
            LanguageLocation("newgame", "gui/load/tip15"),
            LanguageLocation("newgame", "gui/load/tip16"),
            LanguageLocation("newgame", "gui/load/tip17"),
            LanguageLocation("newgame", "gui/load/tip18"),
            LanguageLocation("newgame", "gui/load/tip19"),
            LanguageLocation("newgame", "gui/load/tip20"),
            LanguageLocation("newgame", "gui/load/tip21"),
            LanguageLocation("newgame", "gui/load/tip22"),
            LanguageLocation("newgame", "gui/load/tip23"),
            LanguageLocation("newgame", "gui/load/tip24"),
            LanguageLocation("newgame", "gui/load/tip25"),
            LanguageLocation("newgame", "gui/load/tip26"),
            LanguageLocation("newgame", "gui/load/tip27"),
            LanguageLocation("newgame", "gui/load/tip28"),
            LanguageLocation("newgame", "gui/load/tip29"),
            LanguageLocation("newgame", "gui/load/tip30"),
        ]
        self.random_tip_loc = random.choice(self.random_tip_locs)
        self.config = game.getConfig()
        self.font_location = ResourceLocation("newgame", "font/"+self.game.getConfig().getLang()+".ttf")
        self.bg_location = ResourceLocation("newgame", "texture/gui/background.jpg")
        self.trans = Translator(self.game.getConfig())
        self.hasData = True
    
    def start(self, screen:Screen) -> None:
        self.network.connect()
        self.screen = screen
        
    
    def tick(self) -> None:
        self.tickGUI()

    x = 0
    y = 0
    z = 0
    def tickGUI(self):
        if self.size != self.config.getScreen().getSize():
            self.c = self.config.getScreen().getSize()[1] / 540 * self.config.getGUI()
            self.c50 = int((50*self.c) - (50*self.c)%1)
            self.c100 = int((100*self.c) - (100*self.c)%1)
            self.c150 = int((150*self.c) - (150*self.c)%1)
            self.c200 = int((200*self.c) - (200*self.c)%1)

            self.font16 = pygame.font.Font(self.font_location.get_full_path(), int(16*self.c))
            self.font24 = pygame.font.Font(self.font_location.get_full_path(), int(24*self.c))
            self.textload = self.font16.render(self.trans.translate(self.loadtext_loc), True, (0, 0, 0)).convert_alpha()
            self.tips = self.font24.render(self.trans.translate(self.tips_loc), True, (255, 255, 255)).convert_alpha()
            self.random_tip = self.font24.render(self.trans.translate(self.random_tip_loc), True, (255, 255, 255)).convert_alpha()
            self.size = self.config.getScreen().getSize()
            self.bg = pygame.image.load(self.bg_location.get_full_path()).convert()
            img = PIL.Image.frombytes('RGBA', self.bg.get_size(), pygame.image.tostring(self.bg, 'RGBA'))
            img = img.resize(self.config.getScreen().getSize(), PIL.Image.Resampling.BICUBIC)
            self.bg = pygame.image.fromstring(img.tobytes(), self.config.getScreen().getSize(), 'RGBA').convert()
            
            self.img1 = PIL.Image.new("RGBA", (self.c200, self.c200), (0, 0, 0, 0))
            self.draw1 = PIL.ImageDraw.Draw(self.img1)
            self.draw1.rectangle((self.c50, self.c50, self.c150, self.c150), (65,105,225,200))

            self.img2 = PIL.Image.new("RGBA", (self.c200, self.c200), (0, 0, 0, 0))
            self.draw2 = PIL.ImageDraw.Draw(self.img2)
            self.draw2.rectangle((self.c50, self.c50, self.c150, self.c150), (135,206,235,200))
            
            self.img3 = PIL.Image.new("RGBA", (self.c200, self.c200), (0, 0, 0, 0))
            self.draw3 = PIL.ImageDraw.Draw(self.img3)
            self.draw3.ellipse((self.c50, self.c50, self.c150, self.c150), fill=(255, 255, 255, 200))

            self.circle = pygame.image.fromstring(self.img3.tobytes(), self.img3.size, 'RGBA').convert_alpha()

        self.screen.getScreen().blit(self.bg, (0, 0))

        img1 = self.img1.rotate(90 - self.x, resample=PIL.Image.Resampling.BICUBIC)
        rect1 = pygame.image.fromstring(img1.tobytes(), img1.size, 'RGBA').convert_alpha()
        self.screen.getScreen().blit(rect1, (self.config.getScreen().getSize()[0] - rect1.get_width()/2 - self.c100, self.config.getScreen().getSize()[1] - rect1.get_height()/2 - self.c100))


        img2 = self.img2.rotate(self.x, resample=PIL.Image.Resampling.BICUBIC)
        rect2 = pygame.image.fromstring(img2.tobytes(), img2.size, 'RGBA').convert_alpha()
        self.screen.getScreen().blit(rect2, (self.config.getScreen().getSize()[0] - rect2.get_width()/2 - self.c100, self.config.getScreen().getSize()[1] - rect2.get_height()/2 - self.c100))

        self.screen.getScreen().blit(self.circle, (self.config.getScreen().getSize()[0] - self.circle.get_width() / 2 - self.c100, self.config.getScreen().getSize()[1] - self.circle.get_height() / 2 - self.c100))

        self.screen.getScreen().blit(self.textload, (self.config.getScreen().getSize()[0] - self.textload.get_width() / 2 - self.c100, self.config.getScreen().getSize()[1] - self.textload.get_height() / 2 - self.c100))

        self.screen.getScreen().blit(self.tips, (self.c50, self.config.getScreen().getSize()[1] - self.tips.get_height() / 2 - self.c50))
        self.screen.getScreen().blit(self.random_tip, (self.c50 + self.tips.get_width(), self.config.getScreen().getSize()[1] - self.tips.get_height() / 2 - self.c50))

        pygame.display.flip()
        if self.x == 45:
            self.y += 1
            if self.y == 15:
                self.x = (self.x + 3) % 90
                self.y = 0
        else:
            self.x = (self.x + 3) % 90
        if self.z%200 == 0:
            self.random_tip_loc = random.choice(self.random_tip_locs)
            self.random_tip = self.font24.render(self.trans.translate(self.random_tip_loc), True, (255, 255, 255)).convert_alpha()
        self.z += 1

    def stop(self) -> None:
        self.network.disconnect()