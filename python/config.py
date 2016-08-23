import configparser


if __name__=="__main__":
    config = configparser.ConfigParser()
    config.read("config.cfg")
    print(config["DEFAULT"]["file"])
