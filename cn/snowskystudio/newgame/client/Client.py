import os
import pygame

from cn.snowskystudio.newgame.client.Sounds import Sounds
from cn.snowskystudio.newgame.client.gui.MainScreen import MainScreen
from cn.snowskystudio.newgame.client.gui.ProcessScreen import ProcessScreen
from cn.snowskystudio.newgame.client.gui.SettingsScreen import SettingsScreen
from cn.snowskystudio.newgame.client.gui.WelcomeScreen import WelcomeScreen
from cn.snowskystudio.newgame.network.ClientNetworkController import ClientNetworkController
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation
from cn.snowskystudio.newgame.test.Logger import Logger
from cn.snowskystudio.newgame.client.Textures import Textures


class Client:
    def __init__(self, game):
        self.screen = None
        self.game = game
        self.network = ClientNetworkController()
        self.logger = Logger("Client")
        self.config = game.get_config()
        self.mixer = Sounds()
        self.texture = Textures()
        self.process_scr = ProcessScreen(self.game, self)
        self.welcome_scr = WelcomeScreen(self.game, self)
        self.main_scr = MainScreen(self.game, self)
        self.settings_scr = SettingsScreen(self.game, self)
        
        self.DONE = False

    def start(self, screen):
        self.screen = screen
        self.process_scr.start(screen, self.mixer)
        self.welcome_scr.start(screen, self.mixer)
        self.main_scr.start(screen, self.mixer)
        self.settings_scr.start(screen, self.mixer)
        bg_music = []
        for item in os.listdir("assets/newgame/sound/gui_music/"):
            bg_music.append(ResourceLocation("newgame", "sound/gui_music/" + item))
        self.mixer.music(bg_music)

    def tick(self):
        self.tick_gui()
        self.screen.draw()
        pygame.display.flip()

    def tick_gui(self):
        if self.loading:
            self.DONE = self.process_scr.is_done() and \
                        self.welcome_scr.is_done() and \
                        self.main_scr.is_done() and \
                        self.settings_scr.is_done()
            self.welcome_scr.tick()
        if self.processing:
            self.DONE = self.process_scr.is_done() and \
                        self.welcome_scr.is_done() and \
                        self.main_scr.is_done() and \
                        self.settings_scr.is_done()
            self.process_scr.tick()
        if self.main:
            self.main_scr.tick()
        if self.settings:
            self.settings_scr.tick()
            
    def event(self, event):
        pass

    def stop(self):
        self.network.disconnect()
