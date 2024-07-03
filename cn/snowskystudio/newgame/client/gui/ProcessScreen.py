import random

import PIL
import PIL.Image
import PIL.ImageDraw
import pygame
from cn.snowskystudio.newgame.client.gui.Animations import Animations
from cn.snowskystudio.newgame.client.gui.BaseScreen import BaseScreen
from cn.snowskystudio.newgame.resource.LanguageLocation import LanguageLocation
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation


class ProcessScreen(BaseScreen):
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

        self.text_load = None
        self.tips = None
        self.random_tip = None
        self.bg = None

        self.loading_animation = Animations.PROCESS_LOADING_ANIMATION
        self.logo_animation = Animations.PROCESS_LOGO_ANIMATION

        self.load_text_loc = LanguageLocation("newgame", "gui/load/load")
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

        self.config = game.get_config()
        self.font_location = ResourceLocation("newgame", "font/" + self.game.get_config().get_lang() + ".ttf")
        self.bg_location = ResourceLocation("newgame", "texture/gui/background.jpg")

    def pre_init(self) -> None:
        self.c = self.config.get_screen().get_size()[1] / 540 * self.config.get_gui()
        self.c25 = int((25 * self.c) - (25 * self.c) % 1)
        self.c50 = int((50 * self.c) - (50 * self.c) % 1)
        self.c100 = int((100 * self.c) - (100 * self.c) % 1)
        self.c150 = int((150 * self.c) - (150 * self.c) % 1)
        self.c200 = int((200 * self.c) - (200 * self.c) % 1)

        self.font16 = pygame.font.Font(self.font_location.get_full_path(), int(16 * self.c))
        self.font24 = pygame.font.Font(self.font_location.get_full_path(), int(24 * self.c))
        self.text_load = self.font16.render(self.trans.translate(self.load_text_loc), True, (0, 0, 0)).convert_alpha()
        self.tips = self.font24.render(self.trans.translate(self.tips_loc), True, (255, 255, 255)).convert_alpha()
        self.random_tip = self.font24.render(self.trans.translate(self.random_tip_loc), True,
                                             (255, 255, 255)).convert_alpha()

        self.logo_animation.init_self(self)
        self.logo_animation.get_ready()

        self.loading_animation.init_self(self)
        self.loading_animation.get_ready()

        self.bg = pygame.image.load(self.bg_location.get_full_path()).convert()
        img = PIL.Image.frombytes('RGBA', self.bg.get_size(), pygame.image.tostring(self.bg, 'RGBA'))
        img = img.resize(self.config.get_screen().get_size(), PIL.Image.Resampling.BICUBIC)
        self.bg = pygame.image.fromstring(img.tobytes(), self.config.get_screen().get_size(), 'RGBA').convert()

        self.client.loading = False
        self.client.processing = True

    def tick(self) -> None:
        self.screen.get_screen().blit(self.bg, (0, 0))

        if self.logo_animation.tick():
            return

        self.loading_animation.tick()

        self.screen.get_screen().blit(self.tips, (self.c50, self.config.get_screen().get_size()[
            1] - self.random_tip.get_height() - self.tips.get_height() / 2 - self.c50))
        self.screen.get_screen().blit(self.random_tip, (
        self.c50, self.config.get_screen().get_size()[1] - self.tips.get_height() / 2 - self.c50))
