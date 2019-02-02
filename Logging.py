from datetime import datetime
import os


class Logger:
    ERROR = 0
    DEBUG = 1
    ACTION = 2
    INFO = 3
    __prefixes = ["ERROR", "DEBUG", "ACTION", "INFO"]
    __pattern = "[{}] [{}] -> {}\n"

    def __init__(self):
        if not os.path.isdir("logs"):
            os.mkdir("logs")
        name = "Log-{}.txt".format(datetime.now().strftime("%H%M%S"))
        self.file = os.path.join("logs", name)
        open(self.file, "w").write("")
        self.write("Logger initialized", self.INFO)

    def write(self, registry, reg_type):
        with open(self.file, "a+") as f:
            f.write(self.__pattern.format(
                datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
                Logger.__prefixes[reg_type],
                registry
            ))
