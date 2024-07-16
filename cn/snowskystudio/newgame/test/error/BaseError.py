class BaseError(RuntimeError):
    TYPE = "unknown"

    def __init__(self, *args, _from="NOWHERE"):
        print("An error raised: %s" % self.TYPE)
        print("The error is from %s." % _from)
        print("\n==============================\n")
        print("Details below.")
        super().__init__(*args)
