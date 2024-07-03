from cn.snowskystudio.newgame.test.Logger import Logger


class Decorators:
    class LauncherLogger:
        def __init__(self, launcher: callable) -> None:
            self.launcher = launcher
            self.logger = Logger("Launcher")

        def __call__(self, args: int, argv: list) -> int:
            self.logger.info("Launching...")
            code = self.launcher(args, argv)
            self.logger.info("Stopped.")
            return code
