import threading
import time
import pyautogui
import pygame
from cn.snowskystudio.gameapi.utils.Arguments import Arguments
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.client.Client import Client
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.client.renderer.VirtulScreen import VirtualScreen
from cn.snowskystudio.newgame.newgame.Config import Config
from cn.snowskystudio.newgame.server.Server import Server
from cn.snowskystudio.newgame.test.Logger import Logger


class NewGame:
    def __init__(self, user:str, session_id:str, config:Configuration, args:Arguments) -> None:
        self.user = user
        self.session_id = session_id
        self.logger = Logger("Game", config)
        self.config = Config(config, args, self.logger)
        self.logger.info("Initilizing server and client")
        self.server = Server(self, config)
        self.client = Client(self, config)
        self.running = True
        self.past_vscreen = VirtualScreen(*self.config.getScreen().getSize())
    
    def start(self, screen:Screen):
        pygame.init()

        self.server.start()
        self.client.start(screen)

        self.server_thread = threading.Thread(target=self.serverTick)
        self.server_thread.start()

        while self.running:
            start_time = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.VIDEORESIZE:
                    self.config.getScreen().setSize(event.size)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_F11:
                        self.config.getScreen().full()
                        if self.config.getScreen().isFull():
                            screen.setScreen(pygame.display.set_mode(pyautogui.size(), pygame.FULLSCREEN | pygame.HWSURFACE))
                            self.past_vscreen.setSize(self.config.getScreen().getSize())
                            self.logger.debug(str(self.past_vscreen.getSize()))
                            self.config.getScreen().setSize(pygame.display.get_window_size())
                            self.logger.debug(str(pygame.display.get_window_size()))
                            self.logger.debug(str(self.past_vscreen.getSize()))
                        else:
                            pygame.display.set_mode(pyautogui.size(), pygame.RESIZABLE)
                            screen.setScreen(pygame.display.set_mode(self.past_vscreen.getSize(), pygame.RESIZABLE))
                            self.logger.debug(str(self.past_vscreen.getSize()))
                            self.config.getScreen().setSize(pygame.display.get_window_size())
                            self.logger.debug(str(pygame.display.get_window_size()))

            self.client.tick()
            end_time = time.time()
            if end_time - start_time < 1/60:
                time.sleep(1/60 - (end_time - start_time))
    
    def serverTick(self) -> None:
        while self.running:
            self.server.tick()

    def stop(self) -> None:
        pygame.quit()
        self.server.stop()
        self.client.stop()
    
    def getConfig(self) -> Config:
        return self.config