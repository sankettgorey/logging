import logging
import logging.handlers
from pathlib import Path

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

main_log_file = log_dir / "main.log"



def get_logger(module_name: str) -> logging.Logger:

    logger = logging.getLogger(module_name)

    if logger.handlers:
        return logger
    
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter(
        fmt = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # main handler
    main_handler = logging.handlers.TimedRotatingFileHandler(
        filename=main_log_file,
        # maxBytes=5 * 1024 * 1024
    )

    main_handler.setFormatter(formatter)

    module_log_file = log_dir / f"{module_name}.log"
    module_handler = logging.handlers.TimedRotatingFileHandler(
        filename=module_log_file,
        # maxBytes= 5 * 1024 * 1024,
        backupCount=3
    )

    module_handler.setFormatter(formatter)

    logger.addHandler(module_handler)
    logger.addHandler(main_handler)

    return logger
