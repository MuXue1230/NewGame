import os
import pickle
from typing import Any

from cn.snowskystudio.newgame.test.Logger import Logger
from cn.snowskystudio.newgame.test.error.ConfigurationDoesNotExists import ConfigurationDoesNotExists
from cn.snowskystudio.newgame.test.error.ConfigurationFileDoesNotExists import ConfigurationFileDoesNotExists
from cn.snowskystudio.newgame.test.error.ConfigurationFileIsAlreadyExists import ConfigurationFileIsAlreadyExists
from cn.snowskystudio.newgame.test.error.ConfigurationFileIsReadOnly import ConfigurationFileIsReadOnly
from cn.snowskystudio.newgame.test.error.FunctionError import FunctionError


class Configuration:
    def __init__(self, config_file:str, logger:Logger|None=None) -> None:
        self.config_file = config_file
        self.config = {}
        self.logger = logger
    
    def setLogger(self, logger:Logger) -> None:
        self.logger = logger

    def init(self) -> None:
        self.logger.info("Initializing configuration file.") # type: ignore
        self.config = {
            'debug': False,
            'size': (960, 540),
            'gui': 1.0, 
            'lang': 'zh_cn'
        }
        if os.path.exists(self.config_file): 
            raise ConfigurationFileIsAlreadyExists("Config file already exists. It has NO NEED to init again.", 
                                                   _from="cn.snowskystudio.gameapi.utils.Configuration - Line 24")
        with open(self.config_file, "wb") as f:
            pickle.dump(self.config, f)

    
    def load(self) -> None:
        self.logger.info("Loading configuration file.") # type: ignore
        if not os.path.exists(self.config_file): 
            raise ConfigurationFileDoesNotExists("Config file not found.", 
                                                   _from="cn.snowskystudio.gameapi.utils.Configuration - Line 33")
        with open(self.config_file, "rb") as f:
            self.config = pickle.load(f)
    
    def save(self) -> None:
        self.logger.info("Saving configuration file.") # type: ignore
        if not os.path.exists(self.config_file): 
            raise ConfigurationFileDoesNotExists("Config file not found.", 
                                                   _from="cn.snowskystudio.gameapi.utils.Configuration - Line 41")
        with open(self.config_file, "wb") as f:
            if not f.writable():
                raise ConfigurationFileIsReadOnly("Config file is read only.", 
                                                   _from="cn.snowskystudio.gameapi.utils.Configuration - Line 45")
            pickle.dump(self.config, f)
    
    def isDebug(self) -> bool:
        return self.config["debug"]
    
    def setDebug(self, debug:bool) -> None:
        self.config["debug"] = debug
    
    def set(self, key:str, value:Any) -> None:
        if key in self.config.keys():
            self.config[key] = value
        else:
            raise FunctionError("Configuration does not exists, you should use 'new' but not 'set'.",
                                _from="cn.snowskystudio.gameapi.utils.Configuration - Line 61")
    
    def get(self, key:str) -> Any:
        if key in self.config.keys():
            return self.config[key]
        else:
            raise ConfigurationDoesNotExists("Configuration does not exists.",
                                _from="cn.snowskystudio.gameapi.utils.Configuration - Line 68")
