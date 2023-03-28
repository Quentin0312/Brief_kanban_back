from database import engine

from entity.colonnes import Colonnes, Base
from entity.taches import Taches, Base

Base.metadata.create_all(engine)