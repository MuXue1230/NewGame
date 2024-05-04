class ResourceLocation:
    def __init__(self, id, path):
        self.id = id
        self.path = path
        self.full_path = 'assets/' + self.id + '/' + self.path
        self.name = self.path.split('/')[-1]
    
    def __str__(self):
        return self.id + ':' + self.path
    
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.id == other.id and self.path == other.path
    
    def get_id(self): return self.id

    def get_path(self): return self.path

    def get_full_path(self): return self.full_path

    def get_name(self): return self.name
