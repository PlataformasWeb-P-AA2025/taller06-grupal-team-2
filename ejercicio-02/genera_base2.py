from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Paises(Base):
    __tablename__ = 'paises'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname = Column(Integer)
    itu = Column(String)
    lenguajes = Column(String)
    independiente = Column(String)

    def __repr__(self):
        return f"<Pais(nombre={self.nombre}, continente={self.continente}, capital={self.capital}, dial={self.dial}, lenguajes={self.lenguajes})>"

Base.metadata.create_all(engine)

