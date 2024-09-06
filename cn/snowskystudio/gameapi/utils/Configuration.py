import pickle
import warnings


class Configuration:
    def __init__(self, config_file, logger=None):
        self.config_file = config_file
        self.config = {}
        self.logger = logger

    def set_logger(self, logger):
        self.logger = logger

    def init(self):
        self.logger.info("Initializing configuration file.")
        self.config = {
            'debug': False,
            'size': (960, 540),
            'gui': 1.0,
            'lang': 'zh_cn'
        }
        with open(self.config_file, "wb") as f:
            pickle.dump(self.config, f)

    def load(self):
        self.logger.info("Loading configuration file.")
        with open(self.config_file, "rb") as f:
            self.config = pickle.load(f)

    def save(self):
        self.logger.info("Saving configuration file.")
        with open(self.config_file, "wb") as f:
            pickle.dump(self.config, f)

    def is_debug(self):
        warnings.warn("Function 'is_debug' is deprecated.", DeprecationWarning)
        return self.config["debug"]

    def set_debug(self, debug):
        warnings.warn("Function 'set_debug' is deprecated.", DeprecationWarning)
        self.config["debug"] = debug

    def set(self, key, value):
        self.config[key] = value

    def get(self, key):
        return self.config[key]
