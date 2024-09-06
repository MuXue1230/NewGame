from abc import abstractmethod


class Compact:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    @abstractmethod
    def tick(self, screen):
        pass
    
    @abstractmethod
    def pre_render(self, screen):
        pass
    
    @abstractmethod
    def set_pos(self, x, y):
        self.x = x
        self.y = y
