import hug
from controllers import colonne, tache
api = hug.API(__name__)

api.extend(colonne, '/api/colonne')
# api.extend(tache, '/api/tache')