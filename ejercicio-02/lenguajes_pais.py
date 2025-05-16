from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_base2 import Paises

from genera_base2 import engine

Session = sessionmaker(bind=engine)
session = Session()


paises = session.query(Paises).filter(Paises.lenguajes!=None).order_by(Paises.nombre).all()

for p in paises:
    print(p.nombre, "-", p.lenguajes)