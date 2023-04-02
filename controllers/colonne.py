import hug
from database.database import session
from database.entity import Colonnes
from sqlalchemy import desc

# Récup liste des colonnes
@hug.get('/')
def getColumn():
    queryColonne = session.query(Colonnes).order_by(Colonnes.pos).with_entities(Colonnes.id, Colonnes.titreColonne)
    return queryColonne

# Enregistrement d'une nouvelle colonne
@hug.post('/')
def createColumn(body):
    # Datas
    nvleColonne = body['titreColonne']
    pos = int(body['pos'])

    # Requete SQL
    nouvelleColonne = Colonnes(titreColonne = nvleColonne, pos = pos)
    session.add(nouvelleColonne)
    session.commit()

    # Recup de l'id
    id = session.query(Colonnes).order_by(desc(Colonnes.id)).with_entities(Colonnes.id).first()

    return id[0]

# Modifier le titre de la colonne
@hug.put('/{idColonne}')
def modifyTitle(body, idColonne):
    # Datas
    nvTitre = body['newTitle']

    session.query(Colonnes).filter(Colonnes.id == idColonne).update({ Colonnes.titreColonne : nvTitre })
    session.commit()

    return 'ok'

# Enregistrer les nvle pos des colonnes
@hug.put('/reorder')
def reorderColumn(body):
    # Datas
    idColonne = int(body['idColonne'])
    nvlePos = int(body['nvlePos'])

    # Vérif si nouvelle pos diff de l'ancienne
    anciennePos = session.query(Colonnes).filter(Colonnes.id == idColonne).with_entities(Colonnes.pos).scalar() 
    # Pos départ récup depuis BDD, possibilité envoyer depuis le front
    # Aussi possible envoyer requete depuis le front qui si modif !

    if anciennePos != nvlePos:
        # Colonne drop vers la droite
        if anciennePos < nvlePos:
            session.query(Colonnes).filter(anciennePos < Colonnes.pos, nvlePos >= Colonnes.pos).update({Colonnes.pos : Colonnes.pos - 1})
            session.commit()
        # Colonne drop vers la gauche
        elif anciennePos > nvlePos:
            session.query(Colonnes).filter(anciennePos > Colonnes.pos, nvlePos <= Colonnes.pos).update({Colonnes.pos : Colonnes.pos + 1})
            session.commit()

        # Enregistrer nouvelle pos col
        session.query(Colonnes).filter(Colonnes.id == idColonne).update({"pos" : nvlePos})
        session.commit()
        
        return "changed"
    
    else:
        return "no change"