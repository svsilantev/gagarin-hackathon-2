import yaml
import os
import sys


def MustLoad() -> dict:
    # TODO: ADD ABILITY TO GET PATH FROM ENV
    config_path = "C:/Users/maus1/PycharmProjects/gagarin-hackathon/bot/config/config.yaml"
    if not os.path.exists(config_path):
        print("Config file doesn't exist")
        sys.exit(1)

    f = open(config_path, 'r')
    config = yaml.safe_load(f)

    return config
