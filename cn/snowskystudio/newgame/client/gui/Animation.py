import warnings


class Animation:
    def __init__(self, _id, logger, ready_func, tick_func):
        self.screen = None
        self.id = _id
        self.animation_time = 0
        self.animation_dict = {}
        self.logger = logger
        self.tickFunc = tick_func
        self.readyFunc = ready_func

    def init_self(self, scr):
        self.screen = scr

    def get_ready(self):
        return self.readyFunc(self)

    def get_id(self):
        warnings.warn("Function 'get_id' is deprecated", DeprecationWarning)
        return self.id

    def tick(self, *args, **argv):
        return self.tickFunc(self, *args, **argv)
    
    def reset(self):
        self.animation_time = 0
        
    def reverse(self):
        for animation_list_name in self.animation_dict:
            self.animation_dict[animation_list_name].reverse()
        self.reset()
