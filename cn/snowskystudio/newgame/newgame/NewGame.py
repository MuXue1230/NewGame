import threading
import time
import pygame
from cn.snowskystudio.newgame.client.Client import Client
from cn.snowskystudio.newgame.client.renderer.VirtaulScreen import VirtualScreen
from cn.snowskystudio.newgame.newgame.Config import Config
from cn.snowskystudio.newgame.server.Server import Server
from cn.snowskystudio.newgame.test.Logger import Logger


class NewGame:
    def __init__(self, user, session_id, config, args):
        self.user = user
        self.session_id = session_id
        self.logger = Logger("Game")
        self.config = Config(config, args)
        self.logger.info("Initializing server and client")
        self.server = Server(self)
        self.client = Client(self)
        self.running = True
        self.past_virtual_screen = VirtualScreen(*self.config.get_screen().get_size())
        self.server_thread = None

    def start(self, screen):
        pygame.init()
        pygame.mixer.pre_init(192800, 32, 8, 256 * 1024 * 1024)
        pygame.mixer.init()
        pygame.display.set_caption("NewGame")

        self.server.start()
        self.client.start(screen)

        self.server_thread = threading.Thread(target=self.server_tick)
        self.server_thread.start()

        while self.running:
            start_time = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.client.tick()
            end_time = time.time()
            if end_time - start_time < 1 / 120:
                time.sleep(1 / 120 - (end_time - start_time))

    def server_tick(self):
        while self.running:
            self.server.tick()

    def stop(self):
        pygame.quit()
        self.server.stop()
        self.client.stop()

    def get_config(self):
        return self.config
