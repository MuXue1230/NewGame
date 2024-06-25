import random
import threading

import PIL
import PIL.Image
import PIL.ImageDraw
import pygame
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.gui.BaseScreen import BaseScreen
from cn.snowskystudio.newgame.resource.LanguageLocation import LanguageLocation
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation


class ProcessScreen(BaseScreen):
    def __init__(self, game, loc_config: Configuration, client) -> None:
        super().__init__(game, loc_config, client)
        self.size = (-1, -1)
        self.loadtext_loc = LanguageLocation("newgame", "gui/load/load")
        self.logo_loc = LanguageLocation("newgame", "gui/logo")
        self.describe_loc = LanguageLocation("newgame", "gui/welcome/describe")
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
        self.transform = 0
        self.transform_describe = 0

        self.flashing = False
    
    def pre_init(self) -> None:
        self.c = self.config.getScreen().getSize()[1] / 540 * self.config.getGUI()
        self.c25 = int((25*self.c) - (25*self.c)%1)
        self.c50 = int((50*self.c) - (50*self.c)%1)
        self.c100 = int((100*self.c) - (100*self.c)%1)
        self.c150 = int((150*self.c) - (150*self.c)%1)
        self.c200 = int((200*self.c) - (200*self.c)%1)

        self.font16 = pygame.font.Font(self.font_location.get_full_path(), int(16*self.c))
        self.font24 = pygame.font.Font(self.font_location.get_full_path(), int(24*self.c))
        self.textload = self.font16.render(self.trans.translate(self.loadtext_loc), True, (0, 0, 0)).convert_alpha()
        self.tips = self.font24.render(self.trans.translate(self.tips_loc), True, (255, 255, 255)).convert_alpha()
        self.random_tip = self.font24.render(self.trans.translate(self.random_tip_loc), True, (255, 255, 255)).convert_alpha()
            
        self.logos = []
        self.describes = []
        for i in range(16, 49):
            self.logos.append(pygame.font.Font(self.font_location.get_full_path(), int(i*self.c)).render(self.trans.translate(self.logo_loc), True, (255, 255, 255)).convert_alpha())
        for i in range(0, 256, 4):
            text = self.font24.render(self.trans.translate(self.describe_loc), True, (255, 255, 255)).convert_alpha()
            text.set_alpha(i)
            self.describes.append(text)

        self.bg = pygame.image.load(self.bg_location.get_full_path()).convert()
        img = PIL.Image.frombytes('RGBA', self.bg.get_size(), pygame.image.tostring(self.bg, 'RGBA'))
        img = img.resize(self.config.getScreen().getSize(), PIL.Image.Resampling.BICUBIC)
        self.bg = pygame.image.fromstring(img.tobytes(), self.config.getScreen().getSize(), 'RGBA').convert()

        self.img1 = PIL.Image.new("RGBA", (self.c200, self.c200), (0, 0, 0, 0))
        self.draw1 = PIL.ImageDraw.Draw(self.img1)
        self.draw1.rectangle((self.c50, self.c50, self.c150, self.c150), (65,105,225,200))
        self.rect1_rotated = {}
        for i in range(0, 91, 1):
            img1 = self.img1.rotate(i, resample=PIL.Image.Resampling.BICUBIC)
            self.rect1_rotated[i] = pygame.image.fromstring(img1.tobytes(), img1.size, 'RGBA').convert_alpha()

        self.img2 = PIL.Image.new("RGBA", (self.c200, self.c200), (0, 0, 0, 0))
        self.draw2 = PIL.ImageDraw.Draw(self.img2)
        self.draw2.rectangle((self.c50, self.c50, self.c150, self.c150), (135,206,235,200))
        self.rect2_rotated = {}
        for i in range(0, 91, 1):
            img2 = self.img2.rotate(i, resample=PIL.Image.Resampling.BICUBIC)
            self.rect2_rotated[i] = pygame.image.fromstring(img2.tobytes(), img2.size, 'RGBA').convert_alpha()

        self.img3 = PIL.Image.new("RGBA", (self.c200, self.c200), (0, 0, 0, 0))
        self.draw3 = PIL.ImageDraw.Draw(self.img3)
        self.draw3.ellipse((self.c50, self.c50, self.c150, self.c150), fill=(255, 255, 255, 200))
        
        self.circle = pygame.image.fromstring(self.img3.tobytes(), self.img3.size, 'RGBA').convert_alpha()
        self.transform = True
        
        self.client.loaded = True
        self.client.processing = True

        self.size = self.config.getScreen().getSize()
        self.flashing = False
    
    def start(self, screen: Screen) -> None:
        super().start(screen)
        self.x = 45
        self.y = 0
        self.z = 0

    def tick(self) -> None:
        if self.size != self.config.getScreen().getSize():
            self.client.loaded = False
            self.client.processing = False
            if not self.flashing:
                threading.Thread(target=self.pre_init).start()
                self.flashing = True
            return

        if self.flashing:
            return

        self.screen.getScreen().blit(self.bg, (0, 0))

        if self.transform_describe < 255 // 4:
            self.transform_describe += 1
            self.screen.getScreen().blit(self.logos[48-15-self.transform], ((self.config.getScreen().getSize()[0]-self.logos[48-15-self.transform].get_width())/2, (self.config.getScreen().getSize()[1]-self.logos[48-15-self.transform].get_height())/2 - self.c25))
            self.screen.getScreen().blit(self.describes[255//4 - self.transform_describe], ((self.config.getScreen().getSize()[0]-self.logos[48-15-self.transform].get_width())/2 + self.c100, (self.config.getScreen().getSize()[1]-self.logos[48-15-self.transform].get_height())/2 + self.c25))
            return

        if self.transform < 48-15:
            self.transform += 1
            trans_x = ((self.config.getScreen().getSize()[1]-self.logos[48-15-self.transform].get_height())/2 - self.c25 - self.c25)*self.transform // (48-15)
            trans_y = ((self.config.getScreen().getSize()[0]-self.logos[48-15-self.transform].get_width())/2 - self.c50)*self.transform // (48-15)
            self.screen.getScreen().blit(self.logos[48-15-self.transform], ((self.config.getScreen().getSize()[0]-self.logos[48-15-self.transform].get_width())/2 - trans_y, (self.config.getScreen().getSize()[1]-self.logos[48-15-self.transform].get_height())/2 - self.c25 - trans_x))
            return

        rect1 = self.rect1_rotated[90 - self.x]
        self.screen.getScreen().blit(rect1, (self.config.getScreen().getSize()[0] - rect1.get_width()/2 - self.c100, self.config.getScreen().getSize()[1] - rect1.get_height()/2 - self.c100))
        
        rect2 = self.rect2_rotated[self.x]
        self.screen.getScreen().blit(rect2, (self.config.getScreen().getSize()[0] - rect2.get_width()/2 - self.c100, self.config.getScreen().getSize()[1] - rect2.get_height()/2 - self.c100))
        self.screen.getScreen().blit(self.circle, (self.config.getScreen().getSize()[0] - self.circle.get_width() / 2 - self.c100, self.config.getScreen().getSize()[1] - self.circle.get_height() / 2 - self.c100))
        self.screen.getScreen().blit(self.textload, (self.config.getScreen().getSize()[0] - self.textload.get_width() / 2 - self.c100, self.config.getScreen().getSize()[1] - self.textload.get_height() / 2 - self.c100))
        self.screen.getScreen().blit(self.tips, (self.c50, self.config.getScreen().getSize()[1] - self.random_tip.get_height() - self.tips.get_height() / 2 - self.c50))
        self.screen.getScreen().blit(self.random_tip, (self.c50, self.config.getScreen().getSize()[1] - self.tips.get_height() / 2 - self.c50))
        self.screen.getScreen().blit(self.logos[0], (self.c50, self.c25))
        
        if self.x == 45:
            self.y += 1
            if self.y == 30:
                self.x = (self.x + 3) % 90
                self.y = 0
        else:
            self.x = (self.x + 1) % 90
        if self.z%400 == 0:
            self.random_tip_loc = random.choice(self.random_tip_locs)
            self.random_tip = self.font24.render(self.trans.translate(self.random_tip_loc), True, (255, 255, 255)).convert_alpha()
        self.z += 1