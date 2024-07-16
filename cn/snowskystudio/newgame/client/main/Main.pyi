from typing import Optional, Self

from cn.snowskystudio.newgame.test.Logger import Logger
from snowskystudio.gameapi.utils.Arguments import Arguments
from snowskystudio.gameapi.utils.Configuration import Configuration
from snowskystudio.newgame.client.renderer.Screen import Screen
from snowskystudio.newgame.newgame.NewGame import NewGame


class Main:
    DEBUG: bool
    VERSION: tuple[int, int, int, int]
    
    logger: Logger
    config: Configuration
    argument: Arguments
    user: str
    session_id: str
    game: Optional[NewGame]
    screen: Optional[Screen]
    
    def __init__(self) -> Self: ...
    
    def main(self, args: int, argv: list[str]) -> int: ...
