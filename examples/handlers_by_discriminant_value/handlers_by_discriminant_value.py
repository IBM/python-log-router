import logging
from logrouter.setup_logging import setup_logging
import os 

setup_logging(os.path.join(os.path.dirname(__file__), "logging_conf.yaml"))

if __name__=="__main__":
    logging.info(f'Starting script custom_handlers.py')
    logging.info('This example shows how to use a distinct handler class for different discriminant values')
    logging.info('You can specify the handlers_dict attribute in the handlers.logrouter')
    logging.info('The handlers dict has keys as discriminant values and values as handler classes')
    logging.info('For example, lets say you want to classify your logs by internal or external and handle them differently')
    logging.info('You would have to specify a handler class for each of them (or implement a custom one).')
    logging.info('In this example, we use a StreamHandler to manage logs with discriminant="internal" and a custom handler to manage logs with discriminant="external"')
    logging.info('The custom UserHandler will log under a folder called users_log')
    logging.info('Lets start using the discriminator...')
    logging.info('This log will be handled by the internal handler', extra={"log_type": 'internal'})
    logging.info('While this log will be handled by the external handler', extra={"log_type": 'external'})
    logging.info("And, finally, this one is going to throw an exception because it discriminant ins't managed by any handler!", extra={"log_type": "not_handled_discriminant"})