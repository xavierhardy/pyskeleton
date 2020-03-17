#!/usr/bin/env python
"""
Small skeleton Python-3 application trying to follow good practices such as automatic code formatting, unit testing,
separations of concerns, linting and typing.
"""

from logging import getLogger, Logger, Handler
from sys import argv
from typing import Sequence

from pyskeleton.config import configure_app
from pyskeleton.config_parser import parse_arguments

LOGGER = getLogger(__name__)


def main(args: Sequence[str] = None, logger: Logger = None, handler: Handler = None):
    """
    Do stuff
    """
    if args is None:
        args = argv[1:]

    if logger is None:
        logger = LOGGER

    config = parse_arguments(*args)
    configure_app(config, logger, handler=handler)

    logger.debug("hello world with debug level")
    logger.info("hello world with info level")
    logger.warning("hello world with warning level")
    logger.error("hello world with error level")
    logger.critical("hello world with critical level")


if __name__ == "__main__":
    main(argv, LOGGER)
