class VirtualScreen:
    _objects = ['width', 'height', 'is_full']
    def __init__(self, w=0, h=0, is_full=False) -> None:
        self.width = w
        self.height = h
        self.is_full = is_full
    
    def setSize(self, size:tuple[int,int]) -> None:
        self.width = size[0]
        self.height = size[1]

    def getSize(self) -> tuple[int,int]:
        return (self.width, self.height)

    def isFull(self) -> bool:
        return self.is_full
    
    def full(self) -> None:
        self.is_full = not self.is_full