import warnings


class VirtualScreen:
    _objects = ['width', 'height', 'is_full']
    
    def __init__(self, w=0, h=0, is_full=False):
        self.width = w
        self.height = h
        self.is_full = is_full
    
    def set_size(self, size):
        self.width = size[0]
        self.height = size[1]
    
    def get_size(self):
        return self.width, self.height
    
    def get_full(self):
        warnings.warn("Function 'is_full' is deprecated.", DeprecationWarning)
        return self.is_full
    
    def full(self):
        warnings.warn("Function 'full' is deprecated.", DeprecationWarning)
        self.is_full = not self.is_full
