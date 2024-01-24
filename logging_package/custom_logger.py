import inspect
import logging

def customLogger(loglevel):

    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("{0}.log" .format(loggerName), mode='w')
    fileHandler.setLevel(loglevel)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fileHandler)

    return logger