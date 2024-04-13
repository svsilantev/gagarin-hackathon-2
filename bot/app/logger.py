import logging.config
from rich.logging import RichHandler

def setUpLogger(logLevel: str):
    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "default": {
                "format": "%(message)s",
                "datefmt": "[%X]",
            }
        },
        "handlers": {
            "rich": {
                "level": logLevel,
                "formatter": "default",
                "class": "rich.logging.RichHandler",
                "rich_tracebacks": True,
            },
        },
        "root": {
            "level": logLevel,
            "handlers": ["rich"],
        },
    }

    logging.config.dictConfig(LOGGING_CONFIG)
