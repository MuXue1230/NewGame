class Arguments:
    def __init__(self, logger):
        self.args = {}
        self.types = {}
        self.logger = logger

    def set_logger(self, logger):
        self.logger = logger

    def set_arg(self, arg_name, arg_type=str):
        self.types[arg_name] = arg_type

    def get_arg(self, arg_name, default=None):
        if default:
            if arg_name in self.types.keys():
                if arg_name in self.args.keys():
                    return self.args[arg_name]
                else:
                    return self.types[arg_name](False)
            else:
                return default
        else:
            if arg_name in self.args.keys():
                return self.args[arg_name]
            else:
                return self.types[arg_name](False)

    def make(self, args):
        temp = {}
        is_set = ""
        for arg in args:
            if arg[:2] == "--":
                self.logger.debug("> Handling arg: %s" % arg[2:])
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
                self.logger.warn("> Ignore an unknown argument: %s" % key)
