import os

import pygame
from cn.snowskystudio.gameapi.utils.Arguments import Arguments
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.newgame.NewGame import NewGame
from cn.snowskystudio.newgame.test.Logger import Logger


class Main:
    DEBUG = True
    VERSION = (1, 0, 0, 0)

    def __init__(self) -> None:
        self.logger = Logger("Main")
        self.config = Configuration("config.dat", self.logger)
        self.argument = Arguments(self.logger)

    def Main(self, args:int, argv:list) -> int:
        self.logger.info("Entered Main Function.")
        # Load Config
        if not os.path.exists("config.dat"):
            self.config.init()
            self.logger.info("Updating Configuration.")
            self.config.setDebug(self.DEBUG)
            self.config.save()
        self.config.load()
        # Set Up Config
        self.logger.reconfig(self.config)
        self.config.setLogger(self.logger)
        self.argument.setLogger(self.logger)
        # Processe Argument
        self.logger.info("Processing Arguments: [%d arguments]" % args)
        self.logger.debug(str(argv))
        self.argument.set_arg("user", str)
        self.argument.set_arg("session_id", str)
        self.argument.set_arg("width", int)
        self.argument.set_arg("height", int)
        self.argument.set_arg("full", bool)
        self.argument.set_arg("gui", float)
        self.argument.set_arg("lang", str)
        self.argument.make(argv)
        self.user = self.argument.get_arg("user")
        self.logger.info("Get user: %s" %self.user)
        self.session_id = self.argument.get_arg("session_id")
        self.logger.info("Get session id: %s" %self.session_id)
        #Start Game
        self.logger.info("Starting Game...")
        self.game = NewGame(self.user, self.session_id, self.config, self.argument)
        self.screen = Screen(self.game.config.getScreen(), self.config)
        self.screen.init()
        try:
            self.game.start(self.screen)
        except pygame.error:
            pass
        self.game.stop()
        self.config.save()
        return 0