from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation


class LanguageLocation(ResourceLocation):
    def __init__(self, id, path):
        self.id = id
        self.path = path.split('/')
        self.full_path = self.path[0]+'.'+id+'.'+'.'.join(self.path[1:])