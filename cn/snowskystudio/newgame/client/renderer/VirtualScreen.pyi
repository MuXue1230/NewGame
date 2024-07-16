import warnings


class VirtualScreen:
    _objects: list[str, str, str]
    
    def __init__(self, w=0, h=0, is_full=False): ...
    
    def set_size(self, size: tuple[int, int]) -> None: ...
    
    def get_size(self) -> tuple[int, int]: ...
    
    def get_full(self) -> bool:
        warnings.warn("Function 'is_full' is deprecated.", DeprecationWarning)
        ...
    
    def full(self) -> bool:
        warnings.warn("Function 'full' is deprecated.", DeprecationWarning)
        ...
