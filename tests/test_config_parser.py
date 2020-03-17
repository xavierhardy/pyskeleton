import unittest
from logging import INFO
from unittest import TestCase

from pyskeleton.config import Config
from pyskeleton.config_parser import parse_arguments


class ConfigTest(TestCase):
    def test_parsing_default_config(self):
        config = parse_arguments()
        expected = Config({"log_level": INFO // 10, "verbose": False})
        self.assertEqual(expected, config)

    def test_parsing_verbose_config(self):
        config = parse_arguments("--verbose")
        expected = Config({"log_level": INFO // 10, "verbose": True})
        self.assertEqual(expected, config)

    def test_parsing_verbose_short_config(self):
        config = parse_arguments("-v")
        expected = Config({"log_level": INFO // 10, "verbose": True})
        self.assertEqual(expected, config)

    def test_parsing_log_level_config(self):
        config = parse_arguments("-l", "3")
        expected = Config({"log_level": 3, "verbose": False})
        self.assertEqual(expected, config)

    def test_parsing_invalid_config(self):
        self.assertRaises(SystemExit, parse_arguments, "-l", "3", "-v")


if __name__ == "__main__":
    unittest.main()
