import hug

from database.database import session
from database.entity import Taches

@hug.get('/')
def getTask():
    queryTask = session.query(Taches).with_entities(Taches.id_colonne, Taches.titreTaches)

    return queryTask