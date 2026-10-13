import json
from pathlib import Path


# Stateless utility class; the static method provides configuration without requiring an instance.
class ConfigReader:

    @staticmethod
    def get_config(env):
        config_path = Path(__file__).resolve().parent.parent / "config" / "config.json"

        with open(config_path) as file:
            config = json.load(file)

        return config[env]