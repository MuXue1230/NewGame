import pygame


class Button:
    NORMAL = 0
    HOVER = 1
    PRESSED = 2
    DISABLED = 3

    def __init__(self):
        self.status = self.NORMAL
        self.x = 0
        self.y = 0
        self.action = lambda: None
        self.pressing = False
        self.hovering = False
        self.hover_mix = None
        self.pressing_mix = None
        self.text = None
        self.disabled = None
        self.pressed = None
        self.hover = None
        self.normal = None

    def tick(self, screen):
        if self.status == self.NORMAL:
            screen.get_screen().blit(self.normal, (self.x, self.y))
            screen.get_screen().blit(self.text, (self.x + self.normal.get_width() / 2 - self.text.get_width() / 2,
                                                 self.y + self.normal.get_height() / 2 - self.text.get_height() / 2))
        elif self.status == self.HOVER:
            screen.get_screen().blit(self.hover, (self.x, self.y))
            screen.get_screen().blit(self.text, (self.x + self.hover.get_width() / 2 - self.text.get_width() / 2,
                                                 self.y + self.hover.get_height() / 2 - self.text.get_height() / 2))
        elif self.status == self.PRESSED:
            screen.get_screen().blit(self.pressed, (self.x, self.y))
            screen.get_screen().blit(self.text, (self.x + self.pressed.get_width() / 2 - self.text.get_width() / 2,
                                                 self.y + self.pressed.get_height() / 2 - self.text.get_height() / 2))
        elif self.status == self.DISABLED:
            screen.get_screen().blit(self.disabled, (self.x, self.y))
            screen.get_screen().blit(self.text, (self.x + self.disabled.get_width() / 2 - self.text.get_width() / 2,
                                                 self.y + self.disabled.get_height() / 2 - self.text.get_height() / 2))
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

    def pre_render(self, screen):
        if self.status == self.NORMAL:
            screen.get_screen().blit(self.normal, (self.x, self.y))
            screen.get_screen().blit(self.text, (self.x + self.normal.get_width() / 2 - self.text.get_width() / 2,
                                                 self.y + self.normal.get_height() / 2 - self.text.get_height() / 2))
        elif self.status == self.DISABLED:
            screen.get_screen().blit(self.disabled, (self.x, self.y))
            screen.get_screen().blit(self.text, (self.x + self.disabled.get_width() / 2 - self.text.get_width() / 2,
                                                 self.y + self.disabled.get_height() / 2 - self.text.get_height() / 2))

    def set_mix(self, hover_mix, pressing_mix):
        self.hover_mix = hover_mix
        self.pressing_mix = pressing_mix

    def set_img(self, normal, hover, pressed, disabled):
        self.normal = normal
        self.hover = hover
        self.pressed = pressed
        self.disabled = disabled

    def set_text(self, text):
        self.text = text

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_action(self, action):
        self.action = action
