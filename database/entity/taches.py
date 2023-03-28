from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Taches(Base):
    __tablename__ = 'taches'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titreTaches = Column(String)
    id_colonne = Column(Integer, ForeignKey('colonnes.id'))
    pos = Column(Integer) #Ajouter contrainte d'unicité