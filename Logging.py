from datetime import datetime


class Logger:
    ERROR = 0
    DEBUG = 1
    ACTION = 2
    INFO = 3
    __prefixes = ["ERROR", "DEBUG", "ACTION", "INFO"]
    __pattern = "[{}] [{}] -> {}\n"

    def __init__(self, log_file="log.txt"):
        self.file = log_file
        with open(self.file, "w") as f:
            f.write("Log started")

    def write(self, registry, reg_type):
        with open(self.file, "a+") as f:
            f.write(self.__pattern.format(
                datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
                Logger.__prefixes[reg_type],
                registry
            ))
