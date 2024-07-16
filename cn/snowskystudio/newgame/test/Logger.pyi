from typing import Optional


class Logger:
    class Type:
        def __init__(self, type_name: str, type_id: int): ...
    
    TYPES: dict[str, Type]
    
    def __init__(self, name: Optional[str]=None): ...
    
    def log(self, msg: str, _type: Type): ...
    
    def debug(self, msg: str): ...
    
    def error(self, msg: str): ...
    
    def warn(self, msg: str): ...
    
    def info(self, msg: str): ...