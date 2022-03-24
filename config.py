import logging
import logging.handlers

logger = logging.getLogger('logger')
formatter = logging.Formatter(fmt='service-control[%(process)d]: %(levelname)s: %(message)s')
handler = logging.handlers.SysLogHandler(address='/dev/log')
handler.formatter = formatter
logger.setLevel(logging.INFO)
logger.addHandler(handler)


SRV = 'chronyd'
