class BaseError(RuntimeError):
    TYPE = "unknow"
    def __init__(self, *args: object, _from:str="NOWHERE") -> None:
        print("An error raised: %s" %self.TYPE)
        print("The error is from %s." %_from)
        print("\n==============================\n")
        print("Details below.")
        super().__init__(*args)