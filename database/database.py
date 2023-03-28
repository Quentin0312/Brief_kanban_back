from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# bug fix: lancement serveur (except) migration (try)
try:
    from utils import getConfig
except:
    from .utils import getConfig

# Utilisation des infos de connexion stocké dans le venv pour créer la session
engine = create_engine('postgresql://' + getConfig('user') + ':' + getConfig('password') + '@localhost/' + getConfig('database'), echo=True)
session = sessionmaker(bind=engine)
session = session() # pq ?