"""
Utility module for parsing command-line arguments
"""

from argparse import ArgumentParser
from logging import INFO

from pyskeleton.config import Config


def parse_arguments(*args: str) -> Config:
    """
    Parse arguments and configures what needs to be.
    """
    argument_parser = ArgumentParser("pyskeleton", description="Example application")
    logging_arg_group = argument_parser.add_mutually_exclusive_group()
    logging_arg_group.add_argument(
        "-v", "--verbose", action="store_true", help="Enable debug logging"
    )
    logging_arg_group.add_argument(
        "-l",
        "--log_level",
        type=int,
        default=INFO // 10,
        help="Enable a specific level of logging (1: DEBUG, 5: CRITICAL, default: INFO)",
    )

    return Config(argument_parser.parse_args(args).__dict__)
