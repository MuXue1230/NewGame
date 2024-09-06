import warnings

import pyautogui
from cn.snowskystudio.newgame.client.renderer.VirtaulScreen import VirtualScreen


class Config:
    _objects = ['screen']
    
    def __init__(self, out_conf, run_args):
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
    
    def get_screen(self):
        warnings.warn("Function 'get_screen' is deprecated.", DeprecationWarning)
        return self.screen
    
    def get_gui(self):
        warnings.warn("Function 'get_gui' is deprecated.", DeprecationWarning)
        return self.gui
    
    def get_lang(self):
        warnings.warn("Function 'get_lang' is deprecated.", DeprecationWarning)
        return self.lang
    
    def get(self, key):
        if key == 'screen':
            return self.screen
        elif key == 'size':
            return self.size
        elif key == 'gui':
            return self.gui
        elif key == 'lang':
            return self.lang
