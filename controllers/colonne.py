import hug
from database.database import session
from database.entity import Colonnes

@hug.post('/')
def createColumn(body):
    columnTitle = body['columnTitle']
    return columnTitle + " post"

@hug.put('/')
def modifyColumn(body):
    columnTitle = body['columnTitle']
    return columnTitle + " put"

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

@hug.get('/')
def getColumn():
    queryColonne = session.query(Colonnes).order_by(Colonnes.pos).with_entities(Colonnes.id, Colonnes.titreColonne)
    # listeColonne = []
    # for elt in queryColonne:
    #     for subelt in elt:
    #         listeColonne.append(subelt)
    # print("=================>",listeColonne)
    return queryColonne