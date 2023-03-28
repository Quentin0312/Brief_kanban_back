from .base import Base
from sqlalchemy import Column, Integer, String

class Colonnes(Base):
    __tablename__ = 'colonnes' # modif __ __

    id = Column(Integer, primary_key=True, autoincrement=True)
    titreColonne = Column(String)
    pos = Column(Integer) # Ajouter contrainte d'unicité

