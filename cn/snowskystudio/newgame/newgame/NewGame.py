import time
import pygame
from cn.snowskystudio.newgame.client.Client import Client
from cn.snowskystudio.newgame.client.renderer.VirtaulScreen import VirtualScreen
from cn.snowskystudio.newgame.newgame.Config import Config
from cn.snowskystudio.newgame.test.Logger import Logger


class NewGame:
    def __init__(self, user, session_id, config, args):
        self.user = user
        self.session_id = session_id
        self.logger = Logger("Game")
        self.config = Config(config, args)
        self.logger.info("Initializing server and client")
        self.client = Client(self)
        self.running = True
        self.past_virtual_screen = VirtualScreen(*self.config.get('screen').get_size())
        self.server_thread = None

    def start(self, screen):
        pygame.init()
        pygame.mixer.pre_init(192800, 32, 8, 256 * 1024 * 1024)
        pygame.mixer.init()
        pygame.display.set_caption("NewGame")

        self.client.start(screen)

        while self.running:
            start_time = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.ACTIVEEVENT:
                    self.client.mixer.pause(not event.gain)
                self.client.event(event)
                
            self.client.tick()
            end_time = time.time()
            if end_time - start_time < 1 / 60:
                time.sleep(1 / 60 - (end_time - start_time))

    def stop(self):
        pygame.quit()
        self.client.stop()

    def get_config(self):
        return self.config
