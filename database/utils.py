import configparser

# Permet de récupérer les infos de connexion stocké dans le venv
def getConfig(name):
    config = configparser.ConfigParser()
    config.read('.env/pyvenv.cfg')

    return config.get('env', name)