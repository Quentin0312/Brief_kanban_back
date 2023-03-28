import hug
from database.database import session
from database.entity import Colonnes
from sqlalchemy import desc

# Enregistrement d'une nouvelle colonne
@hug.post('/')
def createColumn():
    nouvelleColonne = Colonnes(titreColonne = "Nouvelle colonne")  # Valeur titreColonne peut etre transmis dans la requete entrante
    # Pour la pos, d'abord recup la dernière pos puis +1 (eviter requete=> info doit être présent dans la requete entrante)
    session.add(nouvelleColonne)
    session.commit()

    # Recup de l'id
    id = session.query(Colonnes).order_by(desc(Colonnes.id)).with_entities(Colonnes.id).first()

    return id[0]

# Récup liste des colonnes
@hug.get('/')
def getColumn():
    queryColonne = session.query(Colonnes).order_by(Colonnes.pos).with_entities(Colonnes.id, Colonnes.titreColonne)
    return queryColonne

# ----------Brouillon-----------------


# @hug.put('/')
# def modifyColumn(body):
#     columnTitle = body['columnTitle']
#     return columnTitle + " put"

# @hug.get('/{column_id}')
# def getColumn(column_id:int):
#     return str(column_id) + " get"

# @hug.get('/')
# def getColumn():
#     queryColonne = session.query(Colonnes).order_by(Colonnes.pos).with_entities(Colonnes.titreColonne)
#     listeColonne = []
#     for elt in queryColonne:
#         for subelt in elt:
#             listeColonne.append(subelt)
#     print("=================>",listeColonne)
#     return listeColonne

# @hug.post('/')
# def createColumn(body):
#     columnTitle = body['columnTitle']
#     return columnTitle + " post"