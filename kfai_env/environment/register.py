import os
from pathlib import Path

from dotenv import load_dotenv


class Environment:
    _possible_environments = {'LOCAL': [".local.env", ".local.env.local"]}

    def __init__(self, env_base_path: str = "./"):
        self._env_base_path = env_base_path

    def register_environment(self, env_name: str):
        # does this env exist?
        if env_name in self._possible_environments:
            return

        self._possible_environments[env_name] = [
            f".{env_name.lower()}.env",
            f".{env_name.lower()}.env.local",
        ]

    def environments(self):
        return self._possible_environments

    def load_env(self):
        # if no ENV is set, we are running in local development
        env = os.getenv("ENV", "LOCAL")
        for env_file_name in self._possible_environments[env]:
            intended_path_to_load = Path(self._env_base_path, env_file_name)
            print(intended_path_to_load)
            load_dotenv(dotenv_path=intended_path_to_load, verbose=True, override=True)