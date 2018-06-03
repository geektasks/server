import os
import configparser


def create_config(path):

    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "ip", "10.72.72.30")
    config.set("Settings", "port", "8000")

    config.add_section("Database")
    config.set("Database", "username", "serv_root")
    config.set("Database", "password", "srv18180")
    config.set("Database", "host", "10.72.72.30")
    config.set("Database", "db", "serverdb")

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
    path = "../settings.ini"
    create_config(path)
