import threading
import time

import PIL
import PIL.Image
import pygame
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.client.Sounds import Sounds
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.client.renderer.VirtulScreen import VirtualScreen
from cn.snowskystudio.newgame.gui.Animations import Animations
from cn.snowskystudio.newgame.gui.BaseScreen import BaseScreen
from cn.snowskystudio.newgame.gui.compact.Button import Button
from cn.snowskystudio.newgame.resource.LanguageLocation import LanguageLocation
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation


class MainScreen(BaseScreen):
    def __init__(self, game, loc_config: Configuration, client) -> None:
        super().__init__(game, loc_config, client)
        self.size = (-1, -1)
        self.config = game.getConfig()
        self.font_location = ResourceLocation("newgame", "font/"+self.game.getConfig().getLang()+".ttf")
        self.bg_location = ResourceLocation("newgame", "texture/gui/background.jpg")

        self.normal_loc = ResourceLocation("newgame", "texture/gui/button.png")
        self.hover_loc = ResourceLocation("newgame", "texture/gui/button_over.png")
        self.press_loc = ResourceLocation("newgame", "texture/gui/button_pressed.png")
        self.disabled_loc = ResourceLocation("newgame", "texture/gui/button_disabled.png")

        self.button_hover_mix_loc = ResourceLocation("newgame", "sound/button.wav")
        self.button_press_mix_loc = ResourceLocation("newgame", "sound/button_click.wav")

        self.title_loc = LanguageLocation("newgame", "gui/main/title")
        self.logo_loc = LanguageLocation("newgame", "gui/logo")
        self.describe_loc = LanguageLocation("newgame", "gui/welcome/describe")
    
    def __button_start(self):
        self.client.loaded = True
        self.client.processing = True
        self.client.main = False
    
    def __button_muti_play(self):
        self.client.loaded = True
        self.client.processing = True
        self.client.main = False
    
    def __button_settings(self):
        self.client.loaded = True
        self.client.processing = True
        self.client.main = False
    
    def __button_exit(self):
        self.game.running = False
    
    def start(self, screen: Screen, mixer: Sounds) -> None:
        self.mixer = mixer
        self.button_hover_mix = self.mixer.get(ResourceLocation("newgame", "sound/button.wav"))
        self.button_press_mix = self.mixer.get(ResourceLocation("newgame", "sound/button_click.wav"))
        super().start(screen)
    
    def pre_init(self) -> None:
        self.c = self.config.getScreen().getSize()[1] / 540 * self.config.getGUI()
        self.c25 = int((25*self.c) - (25*self.c)%1)
        self.c50 = int((50*self.c) - (50*self.c)%1)
        self.c100 = int((100*self.c) - (100*self.c)%1)
        self.c150 = int((150*self.c) - (150*self.c)%1)
        self.c200 = int((200*self.c) - (200*self.c)%1)

        self.font16 = pygame.font.Font(self.font_location.get_full_path(), int(16*self.c))
        self.font24 = pygame.font.Font(self.font_location.get_full_path(), int(24*self.c))
        self.font48 = pygame.font.Font(self.font_location.get_full_path(), int(48*self.c))
        self.size = self.config.getScreen().getSize()

        normal = pygame.image.load(self.normal_loc.get_full_path()).convert_alpha()
        normal_img = PIL.Image.frombytes('RGBA', normal.get_size(), pygame.image.tostring(normal, 'RGBA'))
        normal_img = normal_img.resize((int(normal_img.size[0] * self.c * 0.8 - (normal_img.size[0] * self.c * 0.8)%1), int(normal_img.size[1] * self.c * 0.8 - (normal_img.size[1] * self.c * 0.8)%1)), PIL.Image.Resampling.BICUBIC)
        normal = pygame.image.fromstring(normal_img.tobytes(), normal_img.size, 'RGBA').convert_alpha()
        hover = pygame.image.load(self.hover_loc.get_full_path()).convert_alpha()
        hover_img = PIL.Image.frombytes('RGBA', hover.get_size(), pygame.image.tostring(hover, 'RGBA'))
        hover_img = hover_img.resize((int(hover_img.size[0] * self.c * 0.8 - (hover_img.size[0] * self.c * 0.8)%1), int(hover_img.size[1] * self.c * 0.8 - (hover_img.size[1] * self.c * 0.8)%1)), PIL.Image.Resampling.BICUBIC)
        hover = pygame.image.fromstring(hover_img.tobytes(), hover_img.size, 'RGBA').convert_alpha()
        pressed = pygame.image.load(self.press_loc.get_full_path()).convert_alpha()
        pressed_img = PIL.Image.frombytes('RGBA', pressed.get_size(), pygame.image.tostring(pressed, 'RGBA'))
        pressed_img = pressed_img.resize((int(pressed_img.size[0] * self.c * 0.8 - (pressed_img.size[0] * self.c * 0.8)%1), int(pressed_img.size[1] * self.c * 0.8 - (pressed_img.size[1] * self.c * 0.8)%1)), PIL.Image.Resampling.BICUBIC)
        pressed = pygame.image.fromstring(pressed_img.tobytes(), pressed_img.size, 'RGBA').convert_alpha()
        disabled = pygame.image.load(self.disabled_loc.get_full_path()).convert_alpha()
        disabled_img = PIL.Image.frombytes('RGBA', disabled.get_size(), pygame.image.tostring(disabled, 'RGBA'))
        disabled_img = disabled_img.resize((int(disabled_img.size[0] * self.c * 0.8 - (disabled_img.size[0] * self.c * 0.8)%1), int(disabled_img.size[1] * self.c * 0.8 - (disabled_img.size[1] * self.c * 0.8)%1)), PIL.Image.Resampling.BICUBIC)
        disabled = pygame.image.fromstring(disabled_img.tobytes(), disabled_img.size, 'RGBA').convert_alpha()

        self.mixer.set_volume(self.button_hover_mix_loc, 0.5)
        self.mixer.set_volume(self.button_press_mix_loc, 0.5)
        
        self.logo = self.font48.render(self.trans.translate(self.logo_loc), True, (255, 255, 255))
        self.describe = self.font24.render(self.trans.translate(self.describe_loc), True, (255, 255, 255))
        
        self.start_button = Button()
        self.start_button.set_img(normal, hover, pressed, disabled)
        self.start_button.set_action(self.__button_start)
        self.start_button.set_mix(self.button_hover_mix, self.button_press_mix)
        self.start_button.set_pos(self.size[0]//2 - self.start_button.normal.get_width()//2, self.size[1] // 2 - self.start_button.normal.get_height()//2)
        self.start_button.set_text(self.font16.render(self.trans.translate(LanguageLocation("newgame", "gui/main/button/start")), True, (255, 255, 255)))
        
        self.muti_play_button = Button()
        self.muti_play_button.set_img(normal, hover, pressed, disabled)
        self.muti_play_button.set_action(self.__button_muti_play)
        self.muti_play_button.set_mix(self.button_hover_mix, self.button_press_mix)
        self.muti_play_button.set_pos(self.size[0]//2 - self.muti_play_button.normal.get_width()//2, self.size[1] // 2 - self.muti_play_button.normal.get_height()//2 + self.c50)
        self.muti_play_button.set_text(self.font16.render(self.trans.translate(LanguageLocation("newgame", "gui/main/button/muti_play")), True, (255, 255, 255)))
        
        self.settings_button = Button()
        self.settings_button.set_img(normal, hover, pressed, disabled)
        self.settings_button.set_action(self.__button_settings)
        self.settings_button.set_mix(self.button_hover_mix, self.button_press_mix)
        self.settings_button.set_pos(self.size[0]//2 - self.settings_button.normal.get_width()//2, self.size[1] // 2 - self.settings_button.normal.get_height()//2 + self.c100)
        self.settings_button.set_text(self.font16.render(self.trans.translate(LanguageLocation("newgame", "gui/main/button/settings")), True, (255, 255, 255)))

        self.exit_button = Button()
        self.exit_button.set_img(normal, hover, pressed, disabled)
        self.exit_button.set_action(self.__button_exit)
        self.exit_button.set_mix(self.button_hover_mix, self.button_press_mix)
        self.exit_button.set_pos(self.size[0]//2 - self.exit_button.normal.get_width()//2, self.size[1] // 2 - self.exit_button.normal.get_height()//2 + self.c150)
        self.exit_button.set_text(self.font16.render(self.trans.translate(LanguageLocation("newgame", "gui/main/button/exit")), True, (255, 255, 255)))

        self.enter_animation = Animations.MAIN_ENTER_ANIMATION
        self.enter_animation.init_self(self)
        self.enter_animation.get_ready()
        
        self.client.main = True
    
    def tick(self) -> None:
        if self.size != self.config.getScreen().getSize():
            self.animation = 0

            self.client.loaded = False
            self.client.processing = True
            self.client.main = False
            threading.Thread(target=self.pre_init).start()
            return
        
        if self.enter_animation.tick():
            return 
        else:
            self.client.loaded = True
            self.client.processing = False
        
            self.screen.getScreen().blit(self.logo, ((self.config.getScreen().getSize()[0]-self.logo.get_width())/2, (self.config.getScreen().getSize()[1]-self.logo.get_height())/2 - self.c100))
            self.screen.getScreen().blit(self.describe, ((self.config.getScreen().getSize()[0]-self.logo.get_width())/2 + self.c100, (self.config.getScreen().getSize()[1]-self.logo.get_height())/2 - self.c50))
    
            self.start_button.tick(self.screen)
            self.muti_play_button.tick(self.screen)
            self.settings_button.tick(self.screen)
            self.exit_button.tick(self.screen)
