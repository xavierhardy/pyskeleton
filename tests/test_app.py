import unittest
from io import StringIO
from logging import getLogger, StreamHandler
from unittest import TestCase

from pyskeleton.cli import main


class CliTest(TestCase):
    def test_cli_default_config(self):
        with StringIO() as stream:
            logger = getLogger("CliTest.test_cli_default_config")

            main([], logger, handler=StreamHandler(stream))
            expected = (
                "hello world with info level\n"
                "hello world with warning level\n"
                "hello world with error level\n"
                "hello world with critical level\n"
            )
            self.assertEqual(expected, stream.getvalue())

    def test_cli_verbose_config(self):
        with StringIO() as stream:
            logger = getLogger("CliTest.test_cli_verbose_config")

            main(["--verbose"], logger, handler=StreamHandler(stream))
            expected = (
                "hello world with debug level\n"
                "hello world with info level\n"
                "hello world with warning level\n"
                "hello world with error level\n"
                "hello world with critical level\n"
            )
            self.assertEqual(expected, stream.getvalue())

    def test_cli_log_level_config(self):
        with StringIO() as stream:
            logger = getLogger("CliTest.test_cli_log_level_config")

            main(["-l", "4"], logger, handler=StreamHandler(stream))
            expected = "hello world with error level\nhello world with critical level\n"
            self.assertEqual(expected, stream.getvalue())


if __name__ == "__main__":
    unittest.main()
