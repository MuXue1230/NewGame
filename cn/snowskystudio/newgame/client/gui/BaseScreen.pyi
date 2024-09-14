from abc import abstractmethod
from typing import Self

from cn.snowskystudio.newgame.client.Client import Client
from cn.snowskystudio.newgame.client.Sounds import Sounds
from cn.snowskystudio.newgame.client.renderer.Screen import Screen
from cn.snowskystudio.newgame.newgame.NewGame import NewGame


class BaseScreen:
    game: NewGame
    
    done: bool
    running: bool
    
    def __init__(self, game: NewGame, client: Client) -> Self: ...
    
    @abstractmethod
    def pre_init(self) -> None: ...
    
    def __pre_init(self) -> None: ...
    
    @abstractmethod
    def start(self, screen: Screen, mixer: Sounds) -> None: ...
    
    @abstractmethod
    def tick(self) -> None: ...
    
    def is_done(self) -> bool: ...
    
    def is_running(self) -> bool: ...
    
    def activate(self) -> None: ...
    
    def deactivate(self) -> None: ...
