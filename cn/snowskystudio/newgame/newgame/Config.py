import pyautogui
from cn.snowskystudio.gameapi.utils.Arguments import Arguments
from cn.snowskystudio.gameapi.utils.Configuration import Configuration
from cn.snowskystudio.newgame.client.renderer.VirtulScreen import VirtualScreen


class Config:
    _objects = ['screen']

    def __init__(self, out_conf: Configuration, run_args: Arguments) -> None:
        self.screen = VirtualScreen()
        self.size = pyautogui.size()
        self.screen.set_size((self.size.width, self.size.height))
        self.gui = out_conf.get('gui')
        self.lang = out_conf.get('lang')
        if run_args.get_arg('gui'):
            self.gui = run_args.get_arg('gui')
            out_conf.set('gui', run_args.get_arg('gui'))
        if run_args.get_arg('lang') != 'False':
            self.lang = run_args.get_arg('lang')
            out_conf.set('lang', run_args.get_arg('lang'))

    def get_screen(self) -> VirtualScreen:
        return self.screen

    def get_gui(self) -> float:
        return self.gui

    def get_lang(self) -> str:
        return self.lang
