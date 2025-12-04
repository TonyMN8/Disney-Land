from peewee import Model
from creacion_tablas import db

class BaseModel(Model):
    class Meta:
        database = db