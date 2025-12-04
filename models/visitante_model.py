from models.basemodel import BaseModel
from peewee import *
from playhouse.postgres_ext import *
from datetime import datetime

class VisitanteModel(BaseModel):
    id = PrimaryKeyField(AutoField=True)
    nombre = CharField(null=False)
    email = CharField(unique = True, constraints=[Check("email LIKE '%@%'")])
    altura = IntegerField()
    fecha_registro = DateField(datetime.now())
    preferencias = BinaryJSONField(null=True, default={
        "tipo_favorito" : "",
        "restricciones" : [""],
        "historial_visitas" : 
        [
            {"fecha": "", "atracciones_visitadas": ""}
        ]  
    })