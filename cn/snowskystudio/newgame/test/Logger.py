import time

from cn.snowskystudio.newgame.test.error.LoggerHasNoName import LoggerHasNoName


class Logger:
    class Type:
        def __init__(self, type_name, type_id):
            self.type_name = type_name
            self.type_id = type_id

    TYPES = {
        "DEBUG": Type("DEBUG", 0),
        "ERROR": Type("ERROR", 1),
        "WARN": Type("WARN", 2),
        "INFO": Type("INFO", 3)
    }

    def __init__(self, name=None):
        if not name:
            raise LoggerHasNoName("Logger(from cn.sn.ne.te.Logger) must create with a name.",
                                  _from="cn.snowskystudio.newgame.test.Logger - Line 7")

        self.name = name

    def log(self, msg, _type):
        print("[%d:%d:%d][%s/%s] %s" % (
            time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec, _type.type_name, self.name, msg))

    def debug(self, msg):
        self.log(msg, self.TYPES["DEBUG"])

    def error(self, msg):
        self.log(msg, self.TYPES["ERROR"])

    def warn(self, msg):
        self.log(msg, self.TYPES["WARN"])

    def info(self, msg):
        self.log(msg, self.TYPES["INFO"])
