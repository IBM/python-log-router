import os
import logging

class InternalLogsHandler(logging.FileHandler):
    """The default handler of the routed logs. 
    It extends from FileHandler. The log file is located under 'logs/[discriminant_id]/[log_level].log'
    """
    def __init__(self, id, level):
        file_name = os.path.join(id, f"{logging.getLevelName(level).lower()}.log")
        file_name = os.path.join(
            "internal_logs",
            file_name)
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        super().__init__(file_name)

class ExternalLogsHandler(logging.FileHandler):
    """The default handler of the routed logs. 
    It extends from FileHandler. The log file is located under 'logs/[discriminant_id]/[log_level].log'
    """
    def __init__(self, id, level):
        file_name = os.path.join(id, f"{logging.getLevelName(level).lower()}.log")
        file_name = os.path.join(
            "external_logs",
            file_name)
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        super().__init__(file_name)