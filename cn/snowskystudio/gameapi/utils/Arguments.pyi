from typing import Any, Optional, Self, Type

from snowskystudio.newgame.test.Logger import Logger


class Arguments:
    types: dict[str, Any]
    args: dict[str, Any]
    logger: Logger
    
    def __init__(self, logger: Logger) -> Self: ...
    
    def set_logger(self, logger: Logger) -> None: ...
    
    def set_arg(self, arg_name: str, arg_type: Type[Optional[str]]) -> None: ...
    
    def get_arg(self, arg_name: str, default: Any=None): ...
    
    def make(self, args: list[Any]): ...
