import hug
from hug.middleware import CORSMiddleware
from controllers import colonne, tache

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api, allow_origins=['*'])) # allow_origins à restreindre pour le déploiement

baseUrl = "/api"

api.extend(colonne, baseUrl + '/colonne')
api.extend(tache, baseUrl + '/tache')