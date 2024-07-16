from snowskystudio.newgame.newgame.Config import Config
from snowskystudio.newgame.resource.LanguageLocation import LanguageLocation
from snowskystudio.newgame.resource.ResourceLocation import ResourceLocation


class Translator:
    translations: dict[str, str]
    lang: str
    location: ResourceLocation
    
    def __init__(self, config: Config): ...
    
    def load_translations(self): ...
    
    def translate(self, key: LanguageLocation): ...
