import os
import unittest

from kfai_env.environment.register import Environment
from kfai_env.tests.utils.set_env import set_env


class TestEnvUnittest(unittest.TestCase):

    def test_load_env_local(self):
        e = Environment()
        e.load_env()
        assert os.getenv("TEST_ENV") == "hello world_local"

    def test_load_env_test(self):
        with set_env(ENV="TEST"):
            e = Environment()
            e.register_environment("TEST")
            e.load_env()
            assert os.getenv("TEST_ENV") == "hello world_test"
