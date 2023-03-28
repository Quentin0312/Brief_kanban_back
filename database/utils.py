import configparser

def getConfig(name):
    config = configparser.ConfigParser()
    config.read('.env/pyvenv.cfg')

    return config.get('env', name)