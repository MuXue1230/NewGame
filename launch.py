import sys
from cn.snowskystudio.gameapi.launch.Decorators import Decorators
from cn.snowskystudio.newgame.client.main.Main import Main


@Decorators.LauncherLogger
def launch(args, argv):
    """
    To launch the hole program.
    """
    main = Main()
    return main.main(args, argv)


if __name__ == '__main__':
    code = launch(len(sys.argv), sys.argv)
    exit(code)
