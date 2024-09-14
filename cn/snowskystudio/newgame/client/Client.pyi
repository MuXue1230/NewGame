from typing import Optional

from pygame.event import Event

from cn.snowskystudio.newgame.client.Sounds import Sounds
from cn.snowskystudio.newgame.client.Textures import Textures
from cn.snowskystudio.newgame.client.gui.MainScreen import MainScreen
from cn.snowskystudio.newgame.client.gui.ProcessScreen import ProcessScreen
from cn.snowskystudio.newgame.client.gui.SettingsScreen import SettingsScreen
from cn.snowskystudio.newgame.client.gui.WelcomeScreen import WelcomeScreen
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.network.ClientNetworkController import ClientNetworkController
from cn.snowskystudio.newgame.newgame.NewGame import NewGame


class Client:
    game: NewGame
    mixer: Sounds
    texture: Textures
    screen: Optional[Screen]
    
    process_scr: ProcessScreen
    welcome_scr: WelcomeScreen
    main_scr: MainScreen
    settings_scr: SettingsScreen
    
    DONE: bool
    
    network: ClientNetworkController
    
    def __init__(self, game: NewGame): ...
    
    def start(self, screen: Screen): ...
    
    def tick(self): ...
    
    def tick_gui(self): ...
    
    def event(self, event: Event): ...
    
    def stop(self): ...
