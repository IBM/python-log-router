import logging
from logrouter.setup_logging import setup_logging
import threading
import os

setup_logging(os.path.join(os.path.dirname(__file__), "logging_conf.yaml"))
thread_logger = logging.getLogger(__name__)
thread_logger = logging.LoggerAdapter(thread_logger, extra={"should_log": True})

def f(x):
    for i in range(10):
        thread_logger.debug(f'a log: ({i+1}/{10})')

def run_threads():
    for i in range(2):
        t = threading.Thread(target=f, args=[i], name=f'thread_{i}')
        t.start()

if __name__=="__main__":
    logging.info(f'Starting script log_by_thread.py')
    logging.info('In yaml configuration, the field handlers.logrouter.discriminator is set to threadName')
    logging.info('This will make a different log file to be created for each thread')
    logging.info('This introductory logs are logged through the main thread')
    logging.info('In order to not to create a file for the main thread, a filter is used')
    logging.info('Threads are using a LoggingAdapter that adds a should_log=True to each log')
    logging.info("As these introductory logs doens't have that field, the filter will discard them (us)")   
    logging.info("You can use this mechanism to only create a handler for the logs you are interesed in")
    logging.info("see the logrouter.default_handler.py file for more details")
    run_threads()