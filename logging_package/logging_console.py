import logging

class LoggerConsole():
    def testlog(self):
        # Create logger
        logger = logging.getLogger(LoggerConsole.__name__)
        logger.setLevel(logging.INFO)

        # Create console handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


        # Add formatter to ch
        chandler.setFormatter(formatter)

        # Add ch to logger
        logger.addHandler(chandler)

        # Log some messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warnig message')
        logger.error('error message')
        logger.critical('critical message')


ff = LoggerConsole()
ff.testlog()