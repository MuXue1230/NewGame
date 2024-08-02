from abc import abstractmethod

import PIL.Image
import pygame
from cn.snowskystudio.newgame.client.gui.BaseScreen import BaseScreen
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation
from snowskystudio.newgame.client.gui.compact.BackButton import BackButton
from snowskystudio.newgame.resource.LanguageLocation import LanguageLocation


class BasePageScreen(BaseScreen):
    def __init__(self, game, client):
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

        self.config = game.get_config()
        self.font_location = ResourceLocation("newgame", "font/" + self.game.get_config().get_lang() + ".ttf")
        self.bg_location = ResourceLocation("newgame", "texture/gui/background.jpg")
        self.bg1_location = ResourceLocation("newgame", "texture/gui/title.png")
        
        self.normal_loc = ResourceLocation("newgame", "texture/gui/back.png")
        self.hover_loc = ResourceLocation("newgame", "texture/gui/back_over.png")
        self.press_loc = ResourceLocation("newgame", "texture/gui/back_pressed.png")
        self.disabled_loc = ResourceLocation("newgame", "texture/gui/button_disabled.png")
        
        self.button_hover_mix_loc = ResourceLocation("newgame", "sound/button.wav")
        self.button_press_mix_loc = ResourceLocation("newgame", "sound/button_click.wav")
        
        self.background = None
        self.background1 = None
        self.back_button = None
        
        self.mixer = None
        self.button_hover_mix = None
        self.button_press_mix = None
        
        self.title_loc = LanguageLocation("newgame", "gui/base/page_screen/title")
        self.title = None
    
    @abstractmethod
    def start(self, screen, mixer):
        self.mixer = mixer
        self.button_hover_mix = self.mixer.get(ResourceLocation("newgame", "sound/button.wav"))
        self.button_press_mix = self.mixer.get(ResourceLocation("newgame", "sound/button_click.wav"))
        super().start(screen, mixer)

    @abstractmethod
    def pre_init(self):
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
        
        background = self.game.client.texture.get(self.bg_location)
        img = PIL.Image.frombytes('RGBA', background.get_size(), pygame.image.tostring(background, 'RGBA'))
        img = img.resize(self.size, PIL.Image.Resampling.BICUBIC)
        self.background = pygame.image.fromstring(img.tobytes(), self.size, 'RGBA').convert_alpha()
        
        background1 = self.game.client.texture.get(self.bg1_location)
        img1 = PIL.Image.frombytes('RGBA', background1.get_size(), pygame.image.tostring(background1, 'RGBA'))
        img1 = img1.resize(self.size, PIL.Image.Resampling.BICUBIC)
        self.background1 = pygame.image.fromstring(img1.tobytes(), self.size, 'RGBA').convert_alpha()
        
        btn_img = self.game.client.texture.get(self.normal_loc)
        btn_img_pil = PIL.Image.frombytes('RGBA', btn_img.get_size(), pygame.image.tostring(btn_img, 'RGBA'))
        btn_img_pil = btn_img_pil.resize((
            int(btn_img_pil.size[0] * self.c * 0.8 - (btn_img_pil.size[0] * self.c * 0.8) % 1),
            int(btn_img_pil.size[1] * self.c * 0.8 - (
                    btn_img_pil.size[1] * self.c * 0.8) % 1)),
                PIL.Image.Resampling.BICUBIC)
        btn_img = pygame.image.fromstring(btn_img_pil.tobytes(), btn_img_pil.size, 'RGBA').convert_alpha()
        
        self.back_button = BackButton()
        self.back_button.set_img(btn_img)
        self.back_button.set_action(self.__button_back)
        self.back_button.set_mix(self.button_hover_mix, self.button_press_mix)
        self.back_button.set_pos(0, 0)
        self.back_button.set_text(
                self.font16.render("", True, (255, 255, 255)))
        
        self.title = self.font24.render(self.trans.translate(self.title_loc), True, (255, 255, 255)).convert_alpha()
    
    @abstractmethod
    def __button_back(self):
        pass
    
    @abstractmethod
    def tick(self):
        self.screen.get_screen().blit(self.background, (0, 0))
        self.screen.get_screen().blit(self.background1, (0, 0))
        self.back_button.tick(self.screen)
        self.screen.get_screen().blit(self.title, (200, 0))
