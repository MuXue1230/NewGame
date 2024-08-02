import PIL.Image
import pygame

from snowskystudio.newgame.client.gui.compact.Button import Button
from snowskystudio.newgame.client.renderer.Screen import Screen


class BackButton(Button):
    def tick(self, screen: Screen) -> None:
        if self.status == self.NORMAL:
            screen.get_screen().blit(self.normal, (self.x, self.y))
            screen.get_screen().blit(self.text, (self.x + self.normal.get_width() / 2 - self.text.get_width() / 2,
                                                 self.y + self.normal.get_height() / 2 - self.text.get_height() / 2))
        elif self.status == self.HOVER:
            tmp_w = self.hover.get_width() / 2 - self.normal.get_width() / 2
            tmp_h = self.hover.get_height() / 2 - self.normal.get_height() / 2
            screen.get_screen().blit(self.hover, (self.x - tmp_w, self.y - tmp_h))
            screen.get_screen().blit(self.text,
                                     (self.x - tmp_w + self.hover.get_width() / 2 - self.text.get_width() / 2,
                                      self.y - tmp_h + self.hover.get_height() / 2 - self.text.get_height() / 2))
        elif self.status == self.PRESSED:
            tmp_w = self.pressed.get_width() / 2 - self.normal.get_width() / 2
            tmp_h = self.pressed.get_height() / 2 - self.normal.get_height() / 2
            screen.get_screen().blit(self.pressed, (self.x - tmp_w, self.y - tmp_h))
            screen.get_screen().blit(self.text,
                                     (self.x - tmp_w + self.pressed.get_width() / 2 - self.text.get_width() / 2,
                                      self.y - tmp_h + self.pressed.get_height() / 2 - self.text.get_height() / 2))
        elif self.status == self.DISABLED:
            tmp_w = self.disabled.get_width() / 2 - self.normal.get_width() / 2
            tmp_h = self.disabled.get_height() / 2 - self.normal.get_height() / 2
            screen.get_screen().blit(self.disabled, (self.x - tmp_w, self.y - tmp_h))
            screen.get_screen().blit(self.text,
                                     (self.x - tmp_w + self.disabled.get_width() / 2 - self.text.get_width() / 2,
                                      self.y - tmp_h + self.disabled.get_height() / 2 - self.text.get_height() / 2))
        if not self.status == self.DISABLED:
            if screen.test(self.x, self.y, self.x + self.normal.get_width(), self.y + self.normal.get_height()):
                if pygame.mouse.get_pressed()[0]:
                    self.status = self.PRESSED
                    if not self.pressing:
                        self.pressing = True
                        if self.pressing_mix is not None:
                            self.pressing_mix.play()
                elif self.pressing:
                    self.pressing = False
                    self.action()
                else:
                    self.status = self.HOVER
                    if not self.hovering:
                        self.hovering = True
                        if self.hover_mix is not None:
                            self.hover_mix.play()
            else:
                self.pressing = False
                self.hovering = False
                self.status = self.NORMAL
    
    def set_img(self, img, hover=None, pressed=None, disabled=None):
        img_pil = PIL.Image.frombytes('RGBA', img.get_size(), pygame.image.tostring(img, 'RGBA'))
        img_hover_pil = img_pil.resize((int(img.get_size()[0] * 1.1), int(img.get_size()[1] * 1.1)),
                                       PIL.Image.Resampling.BICUBIC)
        img_pressed_pil = img_pil.resize((int(img.get_size()[0] * 0.9), int(img.get_size()[1] * 0.9)),
                                         PIL.Image.Resampling.BICUBIC)
        img_hover = (pygame.image.fromstring(img_hover_pil.tobytes(),
                                             (int(img.get_size()[0] * 1.1), int(img.get_size()[1] * 1.1)), 'RGBA')
                     .convert_alpha())
        img_pressed = pygame.image.fromstring(img_pressed_pil.tobytes(),
                                              (int(img.get_size()[0] * 0.9), int(img.get_size()[1] * 0.9)),
                                              'RGBA').convert_alpha()
        self.normal = img
        self.hover = img_hover
        self.pressed = img_pressed
        self.disabled = img
