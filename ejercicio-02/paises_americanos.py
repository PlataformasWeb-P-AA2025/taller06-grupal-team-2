from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_base2 import Paises
from genera_base2 import engine

Session = sessionmaker(bind=engine)
session = Session()

# se consulta la tabla paises
# se filtran los paises americanos
paises_americanos = session.query(Paises).filter(or_(Paises.continente=="SA", Paises.continente=="NA")).order_by(Paises.nombre).all()
print(paises_americanos)