import logging
from pathlib import Path
import logging.handlers

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
        fmt="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    module_log_file = log_dir / f"{module_name}.log"

    module_handler = logging.handlers.TimedRotatingFileHandler(
        filename=module_log_file,
        when="midnight",
        interval=1,
        backupCount=3
    )

    module_handler.setFormatter(formatter)
    logger.addHandler(module_handler)

    return logger