import sys
from cn.snowskystudio.gameapi.launch.Decorators import Decorators
from cn.snowskystudio.newgame.main.Main import Main

DEBUG = True


@Decorators.LauncherLogger
def launch(args: int, argv: list) -> int:
    """
    To launch the hole program.
    """
    main = Main()
    return main.main(args, argv)


if __name__ == '__main__':
    code = launch(len(sys.argv), sys.argv)
    exit(code)
