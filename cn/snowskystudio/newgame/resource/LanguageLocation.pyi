from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation


class LanguageLocation(ResourceLocation):
    id: str
    path: str
    full_path: str
    name: str
    
    def __init__(self, _id: str, path: str): ...
