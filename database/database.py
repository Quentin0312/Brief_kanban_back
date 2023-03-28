from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# try:
from utils import getConfig
# except:
#     from .utils import getConfig
# => bug potentiel ?

engine = create_engine('postgresql://' + getConfig('user') + ':' + getConfig('password') + '@localhost/' + getConfig('database'), echo=True)
# engine = create_engine('postgresql://postgres:azerty@localhost/briefKanban', echo=True)
session = sessionmaker(bind=engine)
session = session() # pq ?