from database import db
from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel

def inicializar_db():
    try:
        db.connect(reuse_if_open=True)  # evita errores si ya hay conexión
        
        # safe=True evita errores si ya existe
        db.create_tables([VisitanteModel], safe=True)  
        db.create_tables([AtraccionModel], safe=True)
        print("INFO: Tablas creadas correctamente")
    except Exception as e:
        print("ERROR al crear tablas:", e)
    finally:
        if not db.is_closed():
            db.close()
