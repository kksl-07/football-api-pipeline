import logging
from logging import Logger


def get_logger(log_level: str) -> Logger:
    """
    Provides an object to keep track of logs within the pipeline

    Args:
        log_level (str)

    Returns:
        Logger
    """
    logger = logging.getLogger(__file__)
    logger.setLevel(getattr(logging, log_level.upper()))

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(getattr(logging, log_level.upper()))
    # create formatter and add it to the handlers
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    return logger
