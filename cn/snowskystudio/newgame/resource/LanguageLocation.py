from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation


class LanguageLocation(ResourceLocation):
    def __init__(self, _id, path):
        super().__init__(_id, path)
        self.id = _id
        self.path = path.split('/')
        self.full_path = self.path[0] + '.' + _id + '.' + '.'.join(self.path[1:])
