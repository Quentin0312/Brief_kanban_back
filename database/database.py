from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# bug fix: lancement serveur (except) migration (try)
try:
    from utils import getConfig
except:
    from .utils import getConfig

engine = create_engine('postgresql://' + getConfig('user') + ':' + getConfig('password') + '@localhost/' + getConfig('database'), echo=True)
# engine = create_engine('postgresql://postgres:azerty@localhost/briefKanban', echo=True)
session = sessionmaker(bind=engine)
session = session() # pq ?