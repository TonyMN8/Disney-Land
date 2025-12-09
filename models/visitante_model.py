# importamos el modelo base:
from models.base_model import BaseModel
# importamos las dependencias.
from peewee import *
from playhouse.postgres_ext import BinaryJSONField
from datetime import datetime

class VisitanteModel(BaseModel):
    id = AutoField()
    nombre = CharField(null=False)
    email = CharField(unique=True, constraints=[Check("email LIKE '%@%'")])
    altura = IntegerField()
    fecha_registro = DateTimeField(default=datetime.now)
    preferencias = BinaryJSONField(null=True, default=lambda: {
        "tipo_favorito": "",
        "restricciones": [""],
        "historial_visitas": [
            {"fecha": "", "atracciones_visitadas": ""}
        ]
    })
