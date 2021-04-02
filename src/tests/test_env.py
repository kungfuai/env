import unittest

from src.environment.register import Environment


class TestEnvUnittest(unittest.TestCase):

    def test_load_env(self):
        e = Environment()
        e.register_environment("TEST")
        e.load_env()

