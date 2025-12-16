# INFO: base_model.py 
'''
(*) Importamos la clase base Model de Peewee, es el ORM que usaremos para...
... definir modelos (tablas) de la base de datos.
'''
from peewee import Model
from database import db

 # Defimos la clase BaseModel, es una clase base que heredará de peewee.
    # Esta clase se usará como padre para todos los modelos de la aplicación.
    
class BaseModel(Model):
    class Meta:
        database = db