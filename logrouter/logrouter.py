import os
import logging

class DefaultFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        # Example, filter by a LogRecord attribute
        try:
            return getattr(record, 'should_log')
        except Exception:
            return False


class DefaultHandler(logging.FileHandler):
    """The default handler of the routed logs. 
    It extends from FileHandler. The log file is located under 'logs/[discriminant_id]/[log_level].log'
    """
    def __init__(self, id, level, formatter):
        file_name = os.path.join(id, f"{logging.getLevelName(level).lower()}.log")
        file_name = os.path.join(
            "logs",
            file_name)
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        super().__init__(file_name)
        self.setLevel(level)
        self.setFormatter(formatter)

def get_class_from_path(kls):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m


def get_class_from_name(kls):
    return globals()[kls]


class LogRouter(logging.Handler):
    """Class for routing the logs based on a discriminant
    """
    def __init__(self, discriminator: str, single_handler_class: logging.Handler):
        """__init__ method of LogRouter

        Args:
            discriminator (str): the LogRecord object attribute to group by logs 
            single_handler_class (logging.Handler): the handler to use for each group of logs
        """
        super().__init__()
        self.handlers = {}
        self.discriminator = discriminator
        self.handlerClass = get_class_from_path(single_handler_class)

    def __add_handler(self, discriminator_id: str):
        """Adds a handler to the handlers dict using _discriminator_id as its key


        Args:
            discriminator_id (str): The discriminator id 
        """
        self.handlers[discriminator_id] = self.handlerClass(discriminator_id, self.level, self.formatter)

    def emit(self, record: logging.LogRecord):
        """Emits the log to a handler based on the discriminator_id
        If the handler doesn't exist, it creates one

        Args:
            record (logging.LogRecord): the log object
        """
        try:
            discriminator_id = str(getattr(record, self.discriminator))
        except Exception:
            # if discriminator is not present, return
            return
        if discriminator_id not in self.handlers:
            self.__add_handler(discriminator_id)
        self.handlers[discriminator_id].handle(record)
