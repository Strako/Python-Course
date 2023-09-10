from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Cambia los valores para que coincidan con tu configuración de PostgreSQL
DATABASE_URL = "postgresql://usuario:contraseña@localhost/nombre_de_la_base_de_datos"

# Crear una instancia de motor para la base de datos PostgreSQL
engine = create_engine(DATABASE_URL, echo=True)

# Declarar una clase base para las clases de tabla
Base = declarative_base()

# Definir una clase que represente una tabla
class Persona(Base):
    __tablename__ = 'personas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)

    def __repr__(self):
        return f"Persona(id={self.id}, nombre='{self.nombre}', edad={self.edad})"

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Agregar una persona a la base de datos
nueva_persona = Persona(nombre='Juan', edad=25)
session.add(nueva_persona)
session.commit()

# Consultar personas y mostrar resultados
personas = session.query(Persona).all()
print("Personas en la base de datos:")
for persona in personas:
    print(persona)

# Cerrar la sesión
session.close()