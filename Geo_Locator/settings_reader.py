import json
import os

class SettingsReader:
    def fetch(self):
        base_path = os.path.dirname(__file__)
        config_path = os.path.join(base_path, "config.json")

        with open(config_path) as file:
            return json.load(file)