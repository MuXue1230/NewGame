from cn.snowskystudio.newgame.client.gui.BasePageScreen import BasePageScreen
from cn.snowskystudio.newgame.resource.LanguageLocation import LanguageLocation


class SettingsScreen(BasePageScreen):
    def __init__(self, game, client):
        super().__init__(game, client)
        self.title_loc = LanguageLocation("newgame", "gui/settings/title")
        self._in = False
    
    def start(self, screen, mixer):
        super().start(screen, mixer)

    def pre_init(self):
        super().pre_init()
        self.back_button.set_action(self.__button_back)
        self.done = True
    
    def __button_back(self):
        self.client.main_scr.out = False
        self.client.main_scr.enter_animation.reverse()
        self._in = True

    def tick(self):
        super().tick()
        if self.client.main_scr.out:
            if self.client.main_scr.enter_animation.tick():
                return
            self.client.main_scr.out = False
            self._in = False
            return
        elif self._in:
            if self.client.main_scr.enter_animation.tick():
                return
            self.client.settings_scr.deactivate()
            self.client.main_scr.activate()
            return
