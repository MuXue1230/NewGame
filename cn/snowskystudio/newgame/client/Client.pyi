from typing import Optional

from snowskystudio.newgame.client.Sounds import Sounds
from snowskystudio.newgame.client.gui.MainScreen import MainScreen
from snowskystudio.newgame.client.gui.ProcessScreen import ProcessScreen
from snowskystudio.newgame.client.gui.SettingsScreen import SettingsScreen
from snowskystudio.newgame.client.gui.WelcomeScreen import WelcomeScreen
from snowskystudio.newgame.client.renderer.Screen import Screen
from snowskystudio.newgame.network.ClientNetworkController import ClientNetworkController
from snowskystudio.newgame.newgame.NewGame import NewGame


class Client:
    game: NewGame
    mixer: Sounds
    screen: Optional[Screen]
    
    process_scr: ProcessScreen
    welcome_scr: WelcomeScreen
    main_scr: MainScreen
    settings_scr: SettingsScreen
    
    loading: bool
    processing: bool
    main: bool
    settings: bool
    DONE: bool
    
    network: ClientNetworkController
    
    def __init__(self, game: NewGame): ...
    
    def start(self, screen: Screen): ...
    
    def tick(self): ...
    
    def tick_gui(self): ...
    
    def stop(self): ...
