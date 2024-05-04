import pygame
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.gui.ProcessScreen import ProcessScreen
from cn.snowskystudio.newgame.gui.WelcomeScreen import WelcomeScreen
from cn.snowskystudio.newgame.network.ClientNetworkController import ClientNetworkController
from cn.snowskystudio.newgame.test.Logger import Logger


class Client:
    def __init__(self, game, loc_config:Configuration) -> None:
        self.game = game
        self.network = ClientNetworkController(self.game.getConfig())
        self.logger = Logger("Client", loc_config)
        self.config = game.getConfig()
        self.loaded = False
        self.process_scr = ProcessScreen(self.game, loc_config, self)
        self.welcome_scr = WelcomeScreen(self.game, loc_config, self)
    
    def start(self, screen:Screen) -> None:
        self.network.connect()
        self.screen = screen
        self.process_scr.start(screen)
        self.welcome_scr.start(screen)        
    
    def tick(self) -> None:
        self.tickGUI()

    x = 0
    y = 0
    z = 0
    def tickGUI(self):
        if not self.loaded:
            self.welcome_scr.tick()
        else:
            self.process_scr.tick()
        
        pygame.display.flip()

    def stop(self) -> None:
        self.network.disconnect()
