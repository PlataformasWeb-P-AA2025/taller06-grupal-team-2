from sqlalchemy.orm import sessionmaker
from genera_base2 import Paises
import requests as request
import json
from genera_base2 import engine



Session = sessionmaker(bind=engine) # se crea la clase Session
session = Session() 


# se lee el archivo json
url = "https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json"
archivo = request.get(url)

datos_json = archivo.json()

# se crea la tabla paises
for d in datos_json:
    try:
        p = Paises(
            nombre=d.get('CLDR display name'),
            capital=d.get('Capital'),
            continente=d.get('Continent'),
            dial=d.get('Dial'),
            geoname=d.get('Geoname ID'),
            itu=d.get('ITU'),
            lenguajes=d.get('Languages'),
            independiente=d.get('is_independent')
        )
        session.add(p)
    except Exception as e:
        print(f"Error con el país {d.get('CLDR display name')}: {e}") # Manejo de excepciones
    session.add(p)

# confirmar transacciones

session.commit()
