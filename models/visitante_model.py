# IMPORTACIONES.
# Modelo Base.
from models.base_model import BaseModel
# Dependencias
from peewee import * # type: ignore
from playhouse.postgres_ext import BinaryJSONField # type: ignore
from datetime import datetime

# Modelo que representa la tabla "atracciones".
# Hereda de BaseModel para usar la conexión a la base de datos.
class VisitanteModel(BaseModel):
    id = AutoField()
    nombre = CharField(null=False)
    email = CharField(unique=True)
    altura = IntegerField()
    fecha_registro = DateTimeField(default=lambda: datetime.now().replace(microsecond=0)) # Truncamos los segundos, función encontrada en internet. 
    preferencias = BinaryJSONField(null=True, default=lambda: {
        "tipo_favorito": "",
        "restricciones": [],
        "historial_visitas": []
    })
    
    # Especificamos la tabla visitantes en la base de datos.
    class Meta:
        table_name = 'visitantes'
