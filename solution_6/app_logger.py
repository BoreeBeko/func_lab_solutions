import logging


def get(name: str, mode: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(f"{__name__}.log", mode=mode)
    handler.setFormatter(logging.Formatter("%(name)s [%(asctime)s: %(levelname)s] %(message)s"))
    logger.addHandler(handler)

    return logger
