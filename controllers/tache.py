import hug
from database.database import session
from database.entity import Taches

# Récup la liste des taches
@hug.get('/')
def getTask():
    queryTask = session.query(Taches).order_by(Taches.pos).with_entities(Taches.id_colonne, Taches.titreTaches, Taches.pos)

    return queryTask
