from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation


class AnimationLocation(ResourceLocation):
    id: str
    path: list[str]
    full_path: str
    name: str
    
    def __init__(self, _id: str, path: str): ...
