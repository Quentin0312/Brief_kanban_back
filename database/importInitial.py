from entity import Colonnes
from entity import Taches
# from database.database import session
from database import session

# Colonnes-------------------

column1 = Colonnes(titreColonne = "À faire", pos = 1)
column2 = Colonnes(titreColonne = "En cours", pos = 2)
column3 = Colonnes(titreColonne = "Terminé", pos = 3)

session.add_all([column1,column2,column3])
session.commit()

# Taches----------------------- 


tache1 = Taches(titreTaches = "test 1", id_colonne = 1, pos = 2)
tache2 = Taches(titreTaches = "test 2", id_colonne = 1, pos = 1)
tache3 = Taches(titreTaches = "test autre", id_colonne = 2, pos = 1)


session.add_all([tache1, tache2, tache3])
session.commit()