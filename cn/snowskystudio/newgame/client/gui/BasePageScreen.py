from abc import abstractmethod

import PIL.Image
import pygame
from cn.snowskystudio.newgame.client.gui.BaseScreen import BaseScreen
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation
from snowskystudio.newgame.client.gui.compact.Button import Button
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
        super().start(screen, None)

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
        
        background = pygame.image.load(self.bg_location.get_full_path()).convert_alpha()
        img = PIL.Image.frombytes('RGBA', background.get_size(), pygame.image.tostring(background, 'RGBA'))
        img = img.resize(self.size, PIL.Image.Resampling.BICUBIC)
        self.background = pygame.image.fromstring(img.tobytes(), self.size, 'RGBA').convert_alpha()
        
        background1 = pygame.image.load(self.bg1_location.get_full_path()).convert_alpha()
        img1 = PIL.Image.frombytes('RGBA', background1.get_size(), pygame.image.tostring(background1, 'RGBA'))
        img1 = img1.resize(self.size, PIL.Image.Resampling.BICUBIC)
        self.background1 = pygame.image.fromstring(img1.tobytes(), self.size, 'RGBA').convert_alpha()
        
        normal = pygame.image.load(self.normal_loc.get_full_path()).convert_alpha()
        normal_img = PIL.Image.frombytes('RGBA', normal.get_size(), pygame.image.tostring(normal, 'RGBA'))
        normal_img = normal_img.resize((
            int(normal_img.size[0] * self.c * 0.8 - (normal_img.size[0] * self.c * 0.8) % 1),
            int(normal_img.size[1] * self.c * 0.8 - (
                    normal_img.size[1] * self.c * 0.8) % 1)),
                PIL.Image.Resampling.BICUBIC)
        normal = pygame.image.fromstring(normal_img.tobytes(), normal_img.size, 'RGBA').convert_alpha()
        hover = pygame.image.load(self.hover_loc.get_full_path()).convert_alpha()
        hover_img = PIL.Image.frombytes('RGBA', hover.get_size(), pygame.image.tostring(hover, 'RGBA'))
        hover_img = hover_img.resize((int(hover_img.size[0] * self.c * 0.8 - (hover_img.size[0] * self.c * 0.8) % 1),
                                      int(hover_img.size[1] * self.c * 0.8 - (hover_img.size[1] * self.c * 0.8) % 1)),
                                     PIL.Image.Resampling.BICUBIC)
        hover = pygame.image.fromstring(hover_img.tobytes(), hover_img.size, 'RGBA').convert_alpha()
        pressed = pygame.image.load(self.press_loc.get_full_path()).convert_alpha()
        pressed_img = PIL.Image.frombytes('RGBA', pressed.get_size(), pygame.image.tostring(pressed, 'RGBA'))
        pressed_img = pressed_img.resize((int(
                pressed_img.size[0] * self.c * 0.8 - (pressed_img.size[0] * self.c * 0.8) % 1), int(
                pressed_img.size[1] * self.c * 0.8 - (pressed_img.size[1] * self.c * 0.8) % 1)),
                PIL.Image.Resampling.BICUBIC)
        pressed = pygame.image.fromstring(pressed_img.tobytes(), pressed_img.size, 'RGBA').convert_alpha()
        disabled = pygame.image.load(self.disabled_loc.get_full_path()).convert_alpha()
        disabled_img = PIL.Image.frombytes('RGBA', disabled.get_size(), pygame.image.tostring(disabled, 'RGBA'))
        disabled_img = disabled_img.resize((int(
                disabled_img.size[0] * self.c * 0.8 - (disabled_img.size[0] * self.c * 0.8) % 1), int(
                disabled_img.size[1] * self.c * 0.8 - (disabled_img.size[1] * self.c * 0.8) % 1)),
                PIL.Image.Resampling.BICUBIC)
        disabled = pygame.image.fromstring(disabled_img.tobytes(), disabled_img.size, 'RGBA').convert_alpha()
        
        self.back_button = Button()
        self.back_button.set_img(normal, hover, pressed, disabled)
        self.back_button.set_action(self.__button_back)
        self.back_button.set_mix(self.button_hover_mix, self.button_press_mix)
        self.back_button.set_pos(230, 48)
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
        self.screen.get_screen().blit(self.title, (310, 48))
