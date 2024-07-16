import json
from cn.snowskystudio.newgame.resource.ResourceLocation import ResourceLocation


class Translator:
    def __init__(self, config):
        self.translations = {}
        self.lang = config.get_lang()
        self.location = ResourceLocation("newgame", "lang/" + self.lang + ".json")
        self.load_translations()

    def load_translations(self):
        with open(self.location.get_full_path(), encoding="utf-8") as f:
            self.translations = json.load(f)

    def translate(self, key):
        if key.get_full_path() not in self.translations:
            return key.get_full_path()
        return self.translations[key.get_full_path()]
