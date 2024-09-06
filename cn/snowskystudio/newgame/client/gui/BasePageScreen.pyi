from abc import abstractmethod
from typing import Optional, Self

from pygame import Surface
from pygame.font import Font
from pygame.mixer import Sound

from cn.snowskystudio.newgame.client.gui.BaseScreen import BaseScreen
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation
from cn.snowskystudio.newgame.client.Client import Client
from cn.snowskystudio.newgame.client.Sounds import Sounds
from cn.snowskystudio.newgame.client.gui.compact.BackButton import BackButton
from cn.snowskystudio.newgame.client.gui.compact.Compact import Compact
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.newgame.Config import Config
from cn.snowskystudio.newgame.newgame.NewGame import NewGame
from cn.snowskystudio.newgame.resource import CompactLocation
from cn.snowskystudio.newgame.resource.LanguageLocation import LanguageLocation
from cn.snowskystudio.newgame.resource.Translator import Translator


class BasePageScreen(BaseScreen):
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
    
    config: Config
    font_location: ResourceLocation
    bg_location: ResourceLocation
    bg1_location: ResourceLocation
    
    normal_loc: ResourceLocation
    hover_loc: ResourceLocation
    press_loc: ResourceLocation
    disabled_loc: ResourceLocation
    
    button_hover_mix_loc: ResourceLocation
    button_press_mix_loc: ResourceLocation
    
    background: Optional[Surface]
    background1: Optional[Surface]
    back_button: Optional[BackButton]
    
    mixer: Optional[Sounds]
    button_hover_mix: Optional[Sound]
    button_press_mix: Optional[Sound]
    
    title_loc: LanguageLocation
    title: Optional[Surface]
    
    screen: Screen
    trans: Translator
    
    compacts: dict[CompactLocation, Compact]
    c_ids: list[CompactLocation]
    
    def __init__(self, game: NewGame, client: Client) -> Self: ...
    
    @abstractmethod
    def start(self, screen: Screen, mixer: Sounds) -> None: ...
    
    @abstractmethod
    def pre_init(self) -> None: ...
    
    @abstractmethod
    def __button_back(self) -> None: ...
    
    @abstractmethod
    def tick(self) -> None: ...
    
    def add_compact(self, c_id: CompactLocation, compact: Compact) -> None: ...
