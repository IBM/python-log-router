import logging
from logrouter.setup_logging import setup_logging
import os 

setup_logging(os.path.join(os.path.dirname(__file__), "logging_conf.yaml"))

if __name__=="__main__":
    logging.info(f'Starting script simple_usage.py')
    logging.info('You can use a discriminator (an attribute of the LogRecord object) to route logs to different handlers')
    logging.info('Use the extra field of the log methods or a LoggerAdapter to set the discriminator in the LogRecord')
    logging.info('Set the discriminator name in the configuration yaml file: handlers.logrouter.discriminator')
    logging.info('For example: setting the discriminator to foo...')
    logging.info('will make this log to be routed to a file handler identified by i_am_unique', extra={"foo": 'i_am_unique'})
    logging.info('and this other will be routed to the a handler identified by more_than_unique', extra={"foo": 'more_than_unique'})
    logging.info('You can find the log files under the /logs folder.')