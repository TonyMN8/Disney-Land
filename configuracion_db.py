from database import db
from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel
from models.tickets_model import TicketModel

def inicializar_db():
    try:
        db.connect(reuse_if_open=True)

        # Borrar tablas si existen.
        db.drop_tables([TicketModel, AtraccionModel, VisitanteModel], safe=True)
        print("INFO: Tablas eliminadas correctamente")

        # Crear tablas nuevas
        db.create_tables([VisitanteModel, AtraccionModel, TicketModel], safe=True)
        print("INFO: Tablas creadas correctamente")
    except Exception as e:
        print("ERROR al crear tablas:", e)
