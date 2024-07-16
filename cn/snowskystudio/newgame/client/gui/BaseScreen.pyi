from abc import abstractmethod
from typing import Self

from snowskystudio.newgame.client.Client import Client
from snowskystudio.newgame.client.Sounds import Sounds
from snowskystudio.newgame.client.renderer.Screen import Screen
from snowskystudio.newgame.newgame.NewGame import NewGame


class BaseScreen:
    game: NewGame
    
    def __init__(self, game: NewGame, client: Client) -> Self: ...
    
    @abstractmethod
    def pre_init(self) -> None: ...
    
    @abstractmethod
    def start(self, screen: Screen, mixer: Sounds) -> None: ...
    
    @abstractmethod
    def tick(self) -> None: ...
