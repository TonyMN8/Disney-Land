# IMPORTACIONES.
# Modelo Base.
from models.base_model import BaseModel
# Dependencias
from peewee import * # type: ignore
from playhouse.postgres_ext import BinaryJSONField # type: ignore
from datetime import date

# Modelo que representa la tabla "atracciones".
# Hereda de BaseModel para usar la conexión a la base de datos.
class AtraccionModel(BaseModel):
    id = AutoField()
    nombre = CharField(unique=True, null=False)
    tipo = CharField(constraints=[Check("tipo IN ('extrema', 'familiar', 'infantil', 'acuatica')")])
    altura_minima = IntegerField()
    detalles = BinaryJSONField(null=True, default=lambda: {
        "duracion_segundos": 0,
        "capacidad_por_turno": 0,
        "intensidad": 0,
        "caracteristicas": [],
        "horarios": {
            "apertura": "",
            "cierre": "",
            "mantenimiento": []
        }
    })
    activa = BooleanField(default=True)
    fecha_inauguracion = DateField(default=date.today)
    
     # Especificamos la tabla atracciones en la base de datos.
    class Meta:
        table_name = 'atracciones'