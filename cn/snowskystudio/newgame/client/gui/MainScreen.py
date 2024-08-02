import PIL
import PIL.Image
import pygame

from cn.snowskystudio.newgame.client.gui.Animations import Animations
from cn.snowskystudio.newgame.client.gui.BaseScreen import BaseScreen
from cn.snowskystudio.newgame.client.gui.compact.Button import Button
from cn.snowskystudio.newgame.resource.LanguageLocation import LanguageLocation
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation


class MainScreen(BaseScreen):
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

        self.mixer = None
        self.button_hover_mix = None
        self.button_press_mix = None
        self.out = False

        self.logo = None
        self.describe = None

        self.start_button = None
        self.multi_play_button = None
        self.settings_button = None
        self.exit_button = None

        self.enter_animation = Animations.MAIN_ENTER_ANIMATION

        self.config = game.get_config()
        self.font_location = ResourceLocation("newgame", "font/" + self.game.get_config().get_lang() + ".ttf")
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
        self.client.loading = False
        self.client.processing = True
        self.client.main = True
        self.client.settings = False
        self.out = True
        self.enter_animation.reverse()

    def __button_multi_play(self):
        self.client.loading = False
        self.client.processing = True
        self.client.main = True
        self.client.settings = False
        self.out = True
        self.enter_animation.reverse()

    def __button_settings(self):
        self.client.loading = False
        self.client.processing = False
        self.client.main = False
        self.client.settings = True
        self.out = True
        self.enter_animation.reverse()

    def __button_exit(self):
        self.game.running = False

    def start(self, screen, mixer):
        self.mixer = mixer
        self.button_hover_mix = self.mixer.get(ResourceLocation("newgame", "sound/button.wav"))
        self.button_press_mix = self.mixer.get(ResourceLocation("newgame", "sound/button_click.wav"))
        self.out = False
        super().start(screen, mixer)

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

        normal = self.game.client.texture.get(self.normal_loc)
        normal_img = PIL.Image.frombytes('RGBA', normal.get_size(), pygame.image.tostring(normal, 'RGBA'))
        normal_img = normal_img.resize((
            int(normal_img.size[0] * self.c * 0.8 - (normal_img.size[0] * self.c * 0.8) % 1),
            int(normal_img.size[1] * self.c * 0.8 - (
                    normal_img.size[1] * self.c * 0.8) % 1)),
            PIL.Image.Resampling.BICUBIC)
        normal = pygame.image.fromstring(normal_img.tobytes(), normal_img.size, 'RGBA').convert_alpha()
        hover = self.game.client.texture.get(self.hover_loc)
        hover_img = PIL.Image.frombytes('RGBA', hover.get_size(), pygame.image.tostring(hover, 'RGBA'))
        hover_img = hover_img.resize((int(hover_img.size[0] * self.c * 0.8 - (hover_img.size[0] * self.c * 0.8) % 1),
                                      int(hover_img.size[1] * self.c * 0.8 - (hover_img.size[1] * self.c * 0.8) % 1)),
                                     PIL.Image.Resampling.BICUBIC)
        hover = pygame.image.fromstring(hover_img.tobytes(), hover_img.size, 'RGBA').convert_alpha()
        pressed = self.game.client.texture.get(self.press_loc)
        pressed_img = PIL.Image.frombytes('RGBA', pressed.get_size(), pygame.image.tostring(pressed, 'RGBA'))
        pressed_img = pressed_img.resize((int(
            pressed_img.size[0] * self.c * 0.8 - (pressed_img.size[0] * self.c * 0.8) % 1), int(
            pressed_img.size[1] * self.c * 0.8 - (pressed_img.size[1] * self.c * 0.8) % 1)),
            PIL.Image.Resampling.BICUBIC)
        pressed = pygame.image.fromstring(pressed_img.tobytes(), pressed_img.size, 'RGBA').convert_alpha()
        disabled = self.game.client.texture.get(self.disabled_loc)
        disabled_img = PIL.Image.frombytes('RGBA', disabled.get_size(), pygame.image.tostring(disabled, 'RGBA'))
        disabled_img = disabled_img.resize((int(
            disabled_img.size[0] * self.c * 0.8 - (disabled_img.size[0] * self.c * 0.8) % 1), int(
            disabled_img.size[1] * self.c * 0.8 - (disabled_img.size[1] * self.c * 0.8) % 1)),
            PIL.Image.Resampling.BICUBIC)
        disabled = pygame.image.fromstring(disabled_img.tobytes(), disabled_img.size, 'RGBA').convert_alpha()

        self.mixer.set_volume(self.button_hover_mix_loc, 0.5)
        self.mixer.set_volume(self.button_press_mix_loc, 0.5)

        self.logo = self.font48.render(self.trans.translate(self.logo_loc), True, (255, 255, 255))
        self.describe = self.font24.render(self.trans.translate(self.describe_loc), True, (255, 255, 255))

        self.start_button = Button()
        self.start_button.set_img(normal, hover, pressed, disabled)
        self.start_button.set_action(self.__button_start)
        self.start_button.set_mix(self.button_hover_mix, self.button_press_mix)
        self.start_button.set_pos(self.size[0] // 2 - self.start_button.normal.get_width() // 2,
                                  self.size[1] // 2 - self.start_button.normal.get_height() // 2)
        self.start_button.set_text(
            self.font16.render(self.trans.translate(LanguageLocation("newgame", "gui/main/button/start")), True,
                               (255, 255, 255)))

        self.multi_play_button = Button()
        self.multi_play_button.set_img(normal, hover, pressed, disabled)
        self.multi_play_button.set_action(self.__button_multi_play)
        self.multi_play_button.set_mix(self.button_hover_mix, self.button_press_mix)
        self.multi_play_button.set_pos(self.size[0] // 2 - self.multi_play_button.normal.get_width() // 2,
                                       self.size[1] // 2 - self.multi_play_button.normal.get_height() // 2 + self.c50)
        self.multi_play_button.set_text(
            self.font16.render(self.trans.translate(LanguageLocation("newgame", "gui/main/button/muti_play")), True,
                               (255, 255, 255)))

        self.settings_button = Button()
        self.settings_button.set_img(normal, hover, pressed, disabled)
        self.settings_button.set_action(self.__button_settings)
        self.settings_button.set_mix(self.button_hover_mix, self.button_press_mix)
        self.settings_button.set_pos(self.size[0] // 2 - self.settings_button.normal.get_width() // 2,
                                     self.size[1] // 2 - self.settings_button.normal.get_height() // 2 + self.c100)
        self.settings_button.set_text(
            self.font16.render(self.trans.translate(LanguageLocation("newgame", "gui/main/button/settings")), True,
                               (255, 255, 255)))

        self.exit_button = Button()
        self.exit_button.set_img(normal, hover, pressed, disabled)
        self.exit_button.set_action(self.__button_exit)
        self.exit_button.set_mix(self.button_hover_mix, self.button_press_mix)
        self.exit_button.set_pos(self.size[0] // 2 - self.exit_button.normal.get_width() // 2,
                                 self.size[1] // 2 - self.exit_button.normal.get_height() // 2 + self.c150)
        self.exit_button.set_text(
            self.font16.render(self.trans.translate(LanguageLocation("newgame", "gui/main/button/exit")), True,
                               (255, 255, 255)))

        self.enter_animation.init_self(self)
        self.enter_animation.get_ready()
        
        while not self.client.DONE:
            pass

        self.client.main = True

    def tick(self):
        if self.out:
            if self.enter_animation.tick():
                return
            self.out = False
            self.client.main = False
            return
        elif self.enter_animation.tick():
            return
        else:
            self.client.loading = False
            self.client.processing = False

            self.screen.get_screen().blit(self.logo, (
                (self.config.get_screen().get_size()[0] - self.logo.get_width()) / 2,
                (self.config.get_screen().get_size()[1] - self.logo.get_height()) / 2 - self.c100))
            self.screen.get_screen().blit(self.describe, (
                (self.config.get_screen().get_size()[0] - self.logo.get_width()) / 2 + self.c100,
                (self.config.get_screen().get_size()[1] - self.logo.get_height()) / 2 - self.c50))

            self.start_button.tick(self.screen)
            self.multi_play_button.tick(self.screen)
            self.settings_button.tick(self.screen)
            self.exit_button.tick(self.screen)
