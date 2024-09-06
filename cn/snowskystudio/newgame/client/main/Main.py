import os

from cn.snowskystudio.gameapi.utils.Arguments import Arguments
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.newgame.NewGame import NewGame
from cn.snowskystudio.newgame.test.Logger import Logger


class Main:
    DEBUG = True
    VERSION = (1, 0, 0, 0)

    def __init__(self):
        self.game = None
        self.user = 'Player'
        self.session_id = ''
        self.screen = None
        self.logger = Logger("Main")
        self.config = Configuration("config.dat", self.logger)
        self.argument = Arguments(self.logger)

    def main(self, args, argv):
        self.logger.info("Entered Main Function.")

        # Load Config
        if not os.path.exists("config.dat"):
            self.config.init()
            self.logger.info("Updating Configuration.")
            self.config.save()
        self.config.load()

        # Set Up Config
        self.config.set_logger(self.logger)
        self.argument.set_logger(self.logger)

        # Process Argument
        self.logger.info("Processing Arguments: [%d arguments]" % args)
        self.logger.debug(str(argv))
        self.argument.set_arg("user", str)
        self.argument.set_arg("session_id", str)
        self.argument.set_arg("full", bool)
        self.argument.set_arg("gui", float)
        self.argument.set_arg("lang", str)
        self.argument.make(argv)
        self.user = self.argument.get_arg("user")
        self.logger.info("Get user: %s" % self.user)
        self.session_id = self.argument.get_arg("session_id")
        self.logger.info("Get session id: %s" % self.session_id)

        # Start Game
        self.logger.info("Starting Game...")
        self.game = NewGame(self.user, self.session_id, self.config, self.argument)
        self.screen = Screen(self.game.get_config().get_screen())
        self.screen.init()
        try:
            self.game.start(self.screen)
        except KeyboardInterrupt:
            pass
        self.game.stop()
        self.config.save()

        return 0
