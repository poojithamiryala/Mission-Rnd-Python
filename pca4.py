import p1.p2.m2
import p1.p3.m4
import p1.m1
import p1.m3
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('main.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.ERROR)
stream_handler.setLevel(logging.WARNING)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.info('Entering Main:{}')

logger.info('In Main:{}'.format("entering method f1"))
p1.m1.f1()
logger.info('In Main:{}'.format("exiting method f1"))

logger.info('In Main:{}'.format("entering method f2"))
p1.m1.f2()
logger.info('In Main:{}'.format("exiting method f2"))

logger.info('In Main:{}'.format("entering method f3"))
p1.p2.m2.f3()
logger.info('In Main:{}'.format("exiting method f3"))

logger.info('In Main:{}'.format("entering method f4"))
p1.p2.m2.f4()
logger.info('In Main:{}'.format("exiting method f4"))

logger.info('In Main:{}'.format("entering method f5"))
p1.m3.f5()
logger.info('In Main:{}'.format("exiting method f5"))

logger.info('In Main:{}'.format("entering method f6"))
p1.p3.m4.f6()
logger.info('In Main:{}'.format("exiting method f6"))


logger.info('Exiting main')