import hug
from database.database import session
from database.entity import Colonnes
from sqlalchemy import desc

# Enregistrement d'une nouvelle colonne
@hug.post('/')
def createColumn(body):
    nvleColonne = body['titreColonne']
    pos = int(body['pos'])
    nouvelleColonne = Colonnes(titreColonne = nvleColonne, pos = pos)  # Valeur titreColonne peut etre transmis dans la requete entrante
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

# Enregistrer les nvle pos des colonnes
@hug.put('/reorder')
def reorderColumn(body):
    # Datas
    idColonne = int(body['idColonne'])
    nvlePos = int(body['nvlePos'])

    # Vérif si nvle pos diff de l'ancienne
    # Pos départ à récup dans BDD, possibilité depuis le front envoyer requete que si différence
    anciennePos = session.query(Colonnes).filter(Colonnes.id == idColonne).with_entities(Colonnes.pos).scalar() 

    if anciennePos != nvlePos:
        # Colonne drop vers la droite
        if anciennePos < nvlePos:
            session.query(Colonnes).filter(anciennePos < Colonnes.pos, nvlePos >= Colonnes.pos).update({Colonnes.pos : Colonnes.pos - 1})
            session.commit()
        # Colonne drop vers la gauche
        elif anciennePos > nvlePos:
            session.query(Colonnes).filter(anciennePos > Colonnes.pos, nvlePos <= Colonnes.pos).update({Colonnes.pos : Colonnes.pos + 1})
            session.commit()
        # Enregistrer pos col déplacé
        session.query(Colonnes).filter(Colonnes.id == idColonne).update({"pos" : nvlePos})
        session.commit()
        return "changed"
    else:
        return "no change"


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