from cn.snowskystudio.newgame.client.gui.Animation import Animation
from cn.snowskystudio.newgame.test.Logger import Logger


class Animations:
    def __default(self): ...
    
    # Main Screen
    @staticmethod
    def __main_enter_animation_ready(self): ...
    
    @staticmethod
    def __main_enter_animation_tick(self): ...
    
    # Process Screen
    @staticmethod
    def __process_logo_animation_ready(self): ...
    
    @staticmethod
    def __process_logo_animation_tick(self): ...
    
    @staticmethod
    def __process_loading_animation_ready(self): ...
    
    @staticmethod
    def __process_loading_animation_tick(self): ...
    
    logger: Logger
    
    # All the animations
    EMPTY_ANIMATION: Animation
    MAIN_ENTER_ANIMATION: Animation
    PROCESS_LOGO_ANIMATION: Animation
    PROCESS_LOADING_ANIMATION: Animation
