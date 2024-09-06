from typing import Optional, Self

from pygame import Surface
from pygame.font import Font
from pygame.mixer import Sound

from cn.snowskystudio.newgame.client.gui.BaseScreen import BaseScreen
from cn.snowskystudio.newgame.client.Client import Client
from cn.snowskystudio.newgame.client.Sounds import Sounds
from cn.snowskystudio.newgame.client.gui.Animation import Animation
from cn.snowskystudio.newgame.client.gui.compact.Button import Button
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.newgame.Config import Config
from cn.snowskystudio.newgame.newgame.NewGame import NewGame
from cn.snowskystudio.newgame.resource.LanguageLocation import LanguageLocation
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation
from cn.snowskystudio.newgame.resource.Translator import Translator


class MainScreen(BaseScreen):
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
    
    mixer: Optional[Sounds]
    button_hover_mix: Optional[Sound]
    button_press_mix: Optional[Sound]
    out: bool
    client: Optional[Client]
    
    logo: Optional[Surface]
    describe: Optional[Surface]
    
    start_button: Optional[Button]
    multi_play_button: Optional[Button]
    settings_button: Optional[Button]
    exit_button: Optional[Button]
    
    enter_animation: Animation
    
    config: Config
    font_location: ResourceLocation
    bg_location: ResourceLocation
    
    normal_loc: ResourceLocation
    hover_loc: ResourceLocation
    press_loc: ResourceLocation
    disabled_loc: ResourceLocation
    
    button_hover_mix_loc: ResourceLocation
    button_press_mix_loc: ResourceLocation
    
    title_loc: LanguageLocation
    logo_loc: LanguageLocation
    describe_loc: LanguageLocation
    
    screen: Screen
    trans: Translator
    
    def __init__(self, game: NewGame, client: Client) -> Self: ...
    
    def __button_start(self) -> None: ...
    
    def __button_multi_play(self) -> None: ...
    
    def __button_settings(self) -> None: ...
    
    def __button_exit(self) -> None: ...
    
    def start(self, screen: Screen, mixer: Sounds) -> None: ...
    
    def pre_init(self) -> None: ...
    
    def tick(self) -> None: ...
