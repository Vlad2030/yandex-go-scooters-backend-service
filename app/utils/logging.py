from loguru import logger


def set_basic_logger() -> None:
    return logger.add(sink="./logs.log", enqueue=False,
                      backtrace=False, catch=False)