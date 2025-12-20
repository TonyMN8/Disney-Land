# IMPORTACIONES.
# Modelo Base.
from models.base_model import BaseModel
# Modelos relacionados con otras clases:
from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel
# Dependencias
from peewee import * # type: ignore
from playhouse.postgres_ext import BinaryJSONField # type: ignore
from datetime import datetime

# Modelo que representa la tabla "atracciones".
# Hereda de BaseModel para usar la conexión a la base de datos.
class TicketModel(BaseModel):
    id = AutoField()
    visitante = ForeignKeyField(VisitanteModel, backref='tickets', on_delete='CASCADE')
    atraccion = ForeignKeyField(AtraccionModel, backref='tickets', null=True, on_delete='SET NULL')
    fecha_compra = DateTimeField(default=lambda: datetime.now().replace(microsecond=0)) # Truncamos los segundos, función encontrada en internet.
    fecha_visita = DateField()
    tipo_ticket = CharField(constraints=[Check("tipo_ticket IN ('general', 'colegio', 'empleado')")])
    detalles_compra = BinaryJSONField(null=True, default=lambda: {
        "precio": 0.0,
        "descuentos_aplicados": [],
        "servicios_extra": [],
        "metodo_pago": ""
    })
    usado = BooleanField(default=False)
    fecha_uso = DateTimeField(null=True)
    
    # Especificamos la tabla tickets en la base de datos.
    class Meta:
        table_name = 'tickets'