import hug
from hug.middleware import CORSMiddleware
from controllers import colonne, tache

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api, allow_origins=['*'])) # allow_origins à restreindre pour le déploiement

api.extend(colonne, '/api/colonne')
api.extend(tache, '/api/tache')