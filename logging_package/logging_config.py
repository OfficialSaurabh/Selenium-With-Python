import logging
import logging.config

class LoggingConfig():
    def testlog(self):
        # Create Logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggingConfig.__name__)
        logging.debug('debug message')
        logging.info('info message')
        logging.warning('warnig message')
        logging.error('error message')
        logging.critical('critical message')

ff = LoggingConfig()
ff.testlog()