import os
import pygame
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.client.Sounds import Sounds
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.gui.MainScreen import MainScreen
from cn.snowskystudio.newgame.gui.ProcessScreen import ProcessScreen
from cn.snowskystudio.newgame.gui.WelcomeScreen import WelcomeScreen
from cn.snowskystudio.newgame.network.ClientNetworkController import ClientNetworkController
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation
from cn.snowskystudio.newgame.test.Logger import Logger


class Client:
    def __init__(self, game, loc_config:Configuration) -> None:
        self.game = game
        self.network = ClientNetworkController()
        self.logger = Logger("Client")
        self.config = game.getConfig()
        self.mixer = Sounds()
        self.loaded = False
        self.processing = False
        self.main = False
        self.process_scr = ProcessScreen(self.game, loc_config, self)
        self.welcome_scr = WelcomeScreen(self.game, loc_config, self)
        self.main_scr = MainScreen(self.game, loc_config, self)
    
    def start(self, screen:Screen) -> None:
        self.network.connect()
        self.screen = screen
        self.process_scr.start(screen)
        self.welcome_scr.start(screen)
        self.main_scr.start(screen, self.mixer)
        bg_music = []
        for item in os.listdir("assets/newgame/sound/gui_music/"):
            bg_music.append(ResourceLocation("newgame", "sound/gui_music/"+item))
        self.mixer.music(bg_music)
    
    def tick(self) -> None:
        self.tickGUI()

    def tickGUI(self):
        if not self.loaded:
            self.welcome_scr.tick()
        if self.processing:
            self.process_scr.tick()
        if self.main:
            self.main_scr.tick()
        
        pygame.display.flip()

    def stop(self) -> None:
        self.network.disconnect()
