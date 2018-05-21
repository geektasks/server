import os
import configparser


def create_config(path):

    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "ip", "")
    config.set("Settings", "port", "8000")

    with open(path, "w") as config_file:
        config.write(config_file)

def get_config(path):
    if not os.path.exists(path):
        create_config(path)
    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, setting):
    config = get_config(path)
    value = config.get(section, setting)
    return value

if __name__ == "__main__":
    path = "settings.ini"
    create_config(path)