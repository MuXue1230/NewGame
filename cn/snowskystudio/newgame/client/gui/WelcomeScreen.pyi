from typing import Optional, Self

from pygame import Surface
from pygame.font import Font

from cn.snowskystudio.newgame.client.gui.BaseScreen import BaseScreen
from snowskystudio.newgame.client.Client import Client
from snowskystudio.newgame.client.Sounds import Sounds
from snowskystudio.newgame.client.renderer.Screen import Screen
from snowskystudio.newgame.newgame.Config import Config
from snowskystudio.newgame.newgame.NewGame import NewGame
from snowskystudio.newgame.resource.LanguageLocation import LanguageLocation
from snowskystudio.newgame.resource.ResourceLocation import ResourceLocation
from snowskystudio.newgame.resource.Translator import Translator


class WelcomeScreen(BaseScreen):
    c: int
    c25: int
    c50: int
    c100: int
    c150: int
    c200: int
    
    font24: Optional[Font]
    font48: Optional[Font]
    size: tuple[int, int]
    
    bg: Optional[Surface]
    logo: Optional[Surface]
    describe: Optional[Surface]
    
    config: Config
    font_location: ResourceLocation
    logo_loc: LanguageLocation
    describe_loc: LanguageLocation
    bg_location: ResourceLocation
    logo_y: int
    describe_tick: int
    
    screen: Screen
    trans: Translator
    
    def __init__(self, game: NewGame, client: Client) -> Self: ...
    
    def pre_init(self) -> None: ...
    
    def start(self, screen: Screen, mixer: Sounds) -> None: ...
    
    def tick(self) -> None: ...
