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
    def __init__(self, id, level):
        file_name = os.path.join(id, f"{logging.getLevelName(level).lower()}.log")
        file_name = os.path.join(
            "logs",
            file_name)
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        super().__init__(file_name)

def get_class_from_path(kls: str):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m

class LogRouter(logging.Handler):
    """Class for routing the logs based on a discriminant
    """
    def __init__(self, discriminator: str, single_handler_class: str = None, handlers_dict: dict[str,str] = None):
        """__init__ method of LogRouter

        Args:
            discriminator (str): the LogRecord object attribute to group by logs 
            single_handler_class (str): the handler to use for each group of logs
            handlers_dict (str): dict with discriminant values as key and handler classes as values. If provided, the LogRouter will prioritize sending the logs to this handlers. If a discriminant value does not exist in the dict it will be handled by the single_class_handler instead. Each handler class can optionally accept a two arguments, the discriminant_id and the debugging level. 
        """
        super().__init__()
        self.handlers = {}
        self.discriminator = discriminator

        if single_handler_class is None and handlers_dict is None:
            raise Exception("Either single_handler_class or handlers_dict must be specified")
        if single_handler_class is not None:
            self.handler_class = get_class_from_path(single_handler_class)
        else: 
            self.handler_class = None
        if handlers_dict is not None:
            self.handlers_dict : dict[str, logging.Handler] = {}
            self.handlers_dict = {discriminant: get_class_from_path(handler_class) for (discriminant, handler_class) in handlers_dict.items()}
        else:
            self.handlers_dict = {}


    def __add_handler(self, discriminator_id: str):
        """Adds a handler to the handlers dict using _discriminator_id as its key

        Args:
            discriminator_id (str): The discriminator id 
        """
        if discriminator_id in self.handlers_dict:
            try:
                new_handler = self.handlers_dict[discriminator_id](discriminator_id, self.level)
            except TypeError as e:
                new_handler = self.handlers_dict[discriminator_id]()
        elif self.handler_class is not None:
            try:
                new_handler = self.handler_class(discriminator_id, self.level)
            except TypeError as e:
                new_handler = self.handler_class()
        else:
            raise Exception(f"The discriminant {discriminator_id} isn't handled by any handler. Consider specifying a single_handler_class or add the discriminant value to the handlers_dict")
        new_handler.setLevel(self.level)
        new_handler.setFormatter(self.formatter)
        self.handlers[discriminator_id] = new_handler


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