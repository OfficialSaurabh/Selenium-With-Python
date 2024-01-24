import logging
import logging_package.custom_logger as cl

class CustomLogging2():

    log = cl.customLogger(logging.DEBUG)
    def method1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warnig message')
        self.log.error('error message')
        self.log.critical('critical message')
    def method2(self):
        m2l = cl.customLogger(logging.DEBUG)
        m2l.debug('debug message')
        m2l.info('info message')
        m2l.warning('warnig message')
        m2l.error('error message')
        m2l.critical('critical message')

    def method3(self):
        m3log = cl.customLogger(logging.INFO)
        m3log.debug('debug message')
        m3log.info('info message')
        m3log.warning('warnig message')
        m3log.error('error message')
        m3log.critical('critical message')


ff = CustomLogging2()
ff.method1()
ff.method2()
ff.method3()