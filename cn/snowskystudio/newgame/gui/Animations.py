
import random
import PIL.ImageDraw
import PIL.Image
import pygame
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.client.renderer.VirtulScreen import VirtualScreen
from cn.snowskystudio.newgame.gui.Animation import Animation
from cn.snowskystudio.newgame.resource.AnimationLocation import AnimationLocation
from cn.snowskystudio.newgame.test.Logger import Logger


class Animations:
    def __default(self): pass

    # Main Screen
    def __main_enter_animation_ready(self):
        self.transition_animation = []
        for i in range(0, 256, 4):
            frame = pygame.image.load(self.screen.bg_location.get_full_path()).convert_alpha()
            img = PIL.Image.frombytes('RGBA', frame.get_size(), pygame.image.tostring(frame, 'RGBA'))
            img = img.resize(self.screen.size, PIL.Image.Resampling.BICUBIC)
            frame = pygame.image.fromstring(img.tobytes(), self.screen.size, 'RGBA').convert_alpha()
            frame_screen = Screen(VirtualScreen(*self.screen.size))
            frame_screen.setScreen(frame)
            frame_screen.getScreen().blit(self.screen.logo, ((self.screen.config.getScreen().getSize()[0]-self.screen.logo.get_width())/2, (self.screen.config.getScreen().getSize()[1]-self.screen.logo.get_height())/2 - self.screen.c100))
            frame_screen.getScreen().blit(self.screen.describe, ((self.screen.config.getScreen().getSize()[0]-self.screen.logo.get_width())/2 + self.screen.c100, (self.screen.config.getScreen().getSize()[1]-self.screen.logo.get_height())/2 - self.screen.c50))
            self.screen.start_button.pre_render(frame_screen)
            self.screen.muti_play_button.pre_render(frame_screen)
            self.screen.settings_button.pre_render(frame_screen)
            self.screen.exit_button.pre_render(frame_screen)
            frame.set_alpha(i)
            self.transition_animation.append(frame_screen.getScreen())
    def __main_enter_animation_tick(self):
        if self.animation_time < 256//4:
            self.screen.screen.getScreen().blit(self.transition_animation[self.animation_time], (0, 0))
            self.animation_time += 1
            return True
        self.screen.screen.getScreen().blit(self.transition_animation[self.animation_time - 1], (0, 0))
        return False
    # Process Screen
    def __process_logo_animation_ready(self):
        self.logos = []
        self.describes = []
        self.describe = True
        for i in range(16, 49):
            self.logos.append(pygame.font.Font(self.screen.font_location.get_full_path(), int(i*self.screen.c)).render(self.screen.trans.translate(self.screen.logo_loc), True, (255, 255, 255)).convert_alpha())
        for i in range(0, 256, 4):
            text = self.screen.font24.render(self.screen.trans.translate(self.screen.describe_loc), True, (255, 255, 255)).convert_alpha()
            text.set_alpha(i)
            self.describes.append(text)
    def __process_logo_animation_tick(self):
        if self.animation_time < 63 and self.describe:
            self.animation_time += 1
            self.screen.screen.getScreen().blit(self.logos[32], ((self.screen.config.getScreen().getSize()[0]-self.logos[32].get_width())/2, (self.screen.config.getScreen().getSize()[1]-self.logos[32].get_height())/2 - self.screen.c25))
            self.screen.screen.getScreen().blit(self.describes[63 - self.animation_time], ((self.screen.config.getScreen().getSize()[0]-self.logos[32].get_width())/2 + self.screen.c100, (self.screen.config.getScreen().getSize()[1]-self.logos[32].get_height())/2 + self.screen.c25))
            return True
        if self.animation_time == 63:
            self.animation_time = 0
            self.describe = False
        if self.animation_time < 33:
            self.animation_time += 1
            trans_x = ((self.screen.config.getScreen().getSize()[1]-self.logos[48-15-self.animation_time].get_height())/2 - self.screen.c25 - self.screen.c25)*self.animation_time // (48-15)
            trans_y = ((self.screen.config.getScreen().getSize()[0]-self.logos[48-15-self.animation_time].get_width())/2 - self.screen.c50)*self.animation_time // (48-15)
            self.screen.screen.getScreen().blit(self.logos[48-15-self.animation_time], ((self.screen.config.getScreen().getSize()[0]-self.logos[48-15-self.animation_time].get_width())/2 - trans_y, (self.screen.config.getScreen().getSize()[1]-self.logos[48-15-self.animation_time].get_height())/2 - self.screen.c25 - trans_x))
            return True
        self.screen.screen.getScreen().blit(self.logos[0], (self.screen.c50, self.screen.c25))
        return False
    def __process_loading_animation_ready(self):
        self.img1 = PIL.Image.new("RGBA", (self.screen.c200, self.screen.c200), (0, 0, 0, 0))
        self.draw1 = PIL.ImageDraw.Draw(self.img1)
        self.draw1.rectangle((self.screen.c50, self.screen.c50, self.screen.c150, self.screen.c150), (65,105,225,200))
        self.rect1_rotated = {}
        for i in range(0, 91, 1):
            img1 = self.img1.rotate(i, resample=PIL.Image.Resampling.BICUBIC)
            self.rect1_rotated[i] = pygame.image.fromstring(img1.tobytes(), img1.size, 'RGBA').convert_alpha()

        self.img2 = PIL.Image.new("RGBA", (self.screen.c200, self.screen.c200), (0, 0, 0, 0))
        self.draw2 = PIL.ImageDraw.Draw(self.img2)
        self.draw2.rectangle((self.screen.c50, self.screen.c50, self.screen.c150, self.screen.c150), (135,206,235,200))
        self.rect2_rotated = {}
        for i in range(0, 91, 1):
            img2 = self.img2.rotate(i, resample=PIL.Image.Resampling.BICUBIC)
            self.rect2_rotated[i] = pygame.image.fromstring(img2.tobytes(), img2.size, 'RGBA').convert_alpha()

        self.img3 = PIL.Image.new("RGBA", (self.screen.c200, self.screen.c200), (0, 0, 0, 0))
        self.draw3 = PIL.ImageDraw.Draw(self.img3)
        self.draw3.ellipse((self.screen.c50, self.screen.c50, self.screen.c150, self.screen.c150), fill=(255, 255, 255, 200))
        
        self.circle = pygame.image.fromstring(self.img3.tobytes(), self.img3.size, 'RGBA').convert_alpha()

        self.animation_time_x = 0
        self.animation_time_y = 0
        self.animation_time_z = 0
    def __process_loading_animation_tick(self):
        rect1 = self.rect1_rotated[90 - self.animation_time_x]
        self.screen.screen.getScreen().blit(rect1, (self.screen.config.getScreen().getSize()[0] - rect1.get_width()/2 - self.screen.c100, self.screen.config.getScreen().getSize()[1] - rect1.get_height()/2 - self.screen.c100))
    
        rect2 = self.rect2_rotated[self.animation_time_x]
        self.screen.screen.getScreen().blit(rect2, (self.screen.config.getScreen().getSize()[0] - rect2.get_width()/2 - self.screen.c100, self.screen.config.getScreen().getSize()[1] - rect2.get_height()/2 - self.screen.c100))
        self.screen.screen.getScreen().blit(self.circle, (self.screen.config.getScreen().getSize()[0] - self.circle.get_width() / 2 - self.screen.c100, self.screen.config.getScreen().getSize()[1] - self.circle.get_height() / 2 - self.screen.c100))
        self.screen.screen.getScreen().blit(self.screen.textload, (self.screen.config.getScreen().getSize()[0] - self.screen.textload.get_width() / 2 - self.screen.c100, self.screen.config.getScreen().getSize()[1] - self.screen.textload.get_height() / 2 - self.screen.c100))
        
        if self.animation_time_x == 45:
            self.animation_time_y += 1
            if self.animation_time_y == 30:
                self.animation_time_x = (self.animation_time_x + 3) % 90
                self.animation_time_y = 0
        else:
            self.animation_time_x = (self.animation_time_x + 1) % 90
        if self.animation_time_z%400 == 0:
            self.random_tip_loc = random.choice(self.screen.random_tip_locs)
            self.random_tip = self.screen.font24.render(self.screen.trans.translate(self.random_tip_loc), True, (255, 255, 255)).convert_alpha()
        self.animation_time_z += 1

    logger = Logger('Animation')

    # All the animations
    EMPTY_ANIMATION = Animation(AnimationLocation('newgame', 'empty'), logger, __default, __default)
    MAIN_ENTER_ANIMATION = Animation(AnimationLocation('newgame', 'main/enter'), logger, __main_enter_animation_ready, __main_enter_animation_tick)
    PROCESS_LOGO_ANIMATION = Animation(AnimationLocation('newgame', 'process/logo'), logger, __process_logo_animation_ready, __process_logo_animation_tick)
    PROCESS_LOADING_ANIMATION = Animation(AnimationLocation('newgame', 'process/loading'), logger, __process_loading_animation_ready, __process_loading_animation_tick)
