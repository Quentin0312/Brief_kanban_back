import hug
from database.database import session
from database.entity import Taches
from sqlalchemy import desc

# Récup la liste des taches
@hug.get('/')
def getTask():
    queryTask = session.query(Taches).order_by(Taches.pos).with_entities(Taches.id_colonne, Taches.titreTaches, Taches.pos, Taches.id)

    return queryTask

# Modif titre d'une tache
@hug.put('/{idTache}')
def modifyTaskTitle(body, idTache):
    # Data
    newTitle = body['newTitle']

    # Modification
    session.query(Taches).filter(Taches.id == int(idTache)).update({ Taches.titreTaches : newTitle })
    session.commit()
    return 'ok'

# Ajouter une tache
@hug.post('/')
def addTask(body):
    # Datas
    titreTache = body['titreTache']
    idColonne = int(body['idColonne'])
    pos = int(body['pos'])

    # Modification
    nouvelleTache = Taches(titreTaches = titreTache, id_colonne = idColonne, pos = pos)
    session.add(nouvelleTache)
    session.commit()

    # Récup de l'id
    derId = session.query(Taches).order_by(desc(Taches.id)).with_entities(Taches.id).first()
    derId = derId[0]


    return {"derId" : derId, 'titreTache' : titreTache, 'idColonne' : idColonne, 'pos' : pos}

# Modifie id_colonne et pos
@hug.put('/reorder')
def modifyColumnId(body):

    # Datas
    targetColumnId = int(body['targetColumnId'])
    taskId = int(body['taskId'])
    sourceColumnId = int(body['sourceColumnId'])
    posCibleTache = int(body['posCibleTache'])

    # Récup precedante pos
    posPrecedante = session.query(Taches).filter_by(id = taskId).with_entities(Taches.pos).scalar()
    session.commit()
    # Possiblité de récup depuis le front pour limiter les requete vers BDD

    # Modif id_colonne
    if targetColumnId != sourceColumnId:
        session.query(Taches).filter(Taches.id == taskId).update({"id_colonne": targetColumnId})
        # session.commit()
    
    # Si changement de colonne
    if targetColumnId != sourceColumnId:
        # Modifier pos des taches dans la colonne source
        session.query(Taches).filter(Taches.id_colonne == sourceColumnId, Taches.pos > posPrecedante).update({Taches.pos: Taches.pos - 1})

        # Modifier pos des taches dans la colonne cible
        session.query(Taches).filter(Taches.id_colonne == targetColumnId, Taches.pos >= posCibleTache).update({Taches.pos: Taches.pos + 1})
        # session.commit()
    
    # Tache drop vers le haut sans changement de colonne
    elif posPrecedante > posCibleTache:
        session.query(Taches).filter(Taches.id_colonne == sourceColumnId, posPrecedante > Taches.pos , posCibleTache <= Taches.pos ).update({Taches.pos: Taches.pos + 1})
        # session.commit()

    # Tache drop vers le bas sans changement de colonne
    elif posPrecedante < posCibleTache:
        session.query(Taches).filter(Taches.id_colonne == sourceColumnId, posPrecedante < Taches.pos , posCibleTache >= Taches.pos ).update({Taches.pos: Taches.pos - 1})
        # session.commit()

    # Enregistrement nouvel pos
    session.query(Taches).filter(Taches.id == taskId).update({"pos": posCibleTache})
    
    # Commit de toutes les modifs
    session.commit()

    return 'ok'