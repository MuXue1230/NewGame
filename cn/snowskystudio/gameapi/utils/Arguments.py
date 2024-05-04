from typing import Any

from cn.snowskystudio.newgame.test.Logger import Logger
from cn.snowskystudio.newgame.test.error.ArgumentNameDoesNotExists import ArgumentNameDoesNotExists


class Arguments:
    def __init__(self, logger:Logger) -> None:
        self.args = {}
        self.types = {}
        self.logger = logger
    
    def setLogger(self, logger:Logger) -> None:
        self.logger = logger
    
    def set_arg(self, arg_name:str, arg_type:Any=str) -> None:
        self.types[arg_name] = arg_type
    
    def get_arg(self, arg_name:str, default:Any=None) -> Any:
        if default:
            if arg_name in self.types.keys():
                if arg_name in self.args.keys():
                    return self.args[arg_name]
                else:
                    return self.types[arg_name](False)
            else:
                return default
        else:
            if arg_name in self.types.keys():
                if arg_name in self.args.keys():
                    return self.args[arg_name]
                else:
                    return self.types[arg_name](False)
            else:
                raise ArgumentNameDoesNotExists("Argument which is been requested does not exists.", 
                                                _from="cn.snowskystudio.gameapi.utils.Arguments - Line 25")
    
    def make(self, args:list):
        temp = {}
        is_set = ""
        for arg in args:
            if arg[:2] ==  "--":
                self.logger.debug("> Handling arg: %s" %arg[2:])
                temp[arg[2:]] = True
                is_set = arg[2:]
                continue
            elif is_set:
                temp[is_set] = arg
                is_set = False
        for key in temp.keys():
            if key in self.types.keys():
                self.args[key] = self.types[key](temp[key])
            else:
                self.logger.warn("> Ignore an unknow argument: %s" %key)
