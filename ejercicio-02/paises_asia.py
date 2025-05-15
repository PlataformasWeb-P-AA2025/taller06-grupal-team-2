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
# se filtran los paises asiaticos en orden de dial
paises_asiaticos = session.query(Paises).filter(Paises.continente=="AS").order_by(Paises.dial).all()
print(paises_asiaticos)