from logger_practice import get_logger
import service

logger = get_logger(__name__)

logger.info("Starting application")
service.do_something()
