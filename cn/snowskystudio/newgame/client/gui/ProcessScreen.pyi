from typing import Optional

from pygame import Surface
from pygame.font import Font

from cn.snowskystudio.newgame.client.gui.BaseScreen import BaseScreen
from snowskystudio.newgame.client.Client import Client
from snowskystudio.newgame.client.gui.Animation import Animation
from snowskystudio.newgame.client.renderer.Screen import Screen
from snowskystudio.newgame.newgame.Config import Config
from snowskystudio.newgame.resource.LanguageLocation import LanguageLocation
from snowskystudio.newgame.resource.ResourceLocation import ResourceLocation
from snowskystudio.newgame.resource.Translator import Translator


class ProcessScreen(BaseScreen):
    c: int
    c25: int
    c50: int
    c100: int
    c150: int
    c200: int
    
    font16: Optional[Font]
    font24: Optional[Font]
    font48: Optional[Font]
    size: tuple[int, int]
    
    text_load: Optional[Surface]
    tips: Optional[Surface]
    random_tip: Optional[Surface]
    bg: Optional[Surface]
    
    loading_animation: Animation
    logo_animation = Animation
    
    load_text_loc: LanguageLocation
    logo_loc: LanguageLocation
    describe_loc: LanguageLocation
    tips_loc: LanguageLocation
    random_tip_locs: list[LanguageLocation]
    random_tip_loc: LanguageLocation
    
    config: Config
    font_location: ResourceLocation
    bg_location: ResourceLocation
    
    client: Client
    screen: Screen
    trans: Translator
    
    def __init__(self, game, client): ...
    
    def start(self, screen, mixer): ...
    
    def pre_init(self): ...
    
    def tick(self): ...
