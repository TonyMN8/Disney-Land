from database import db
from models.visitante_model import VisitanteModel

def inicializar_db():
    try:
        db.connect(reuse_if_open=True)  # evita errores si ya hay conexión
        db.create_tables([VisitanteModel], safe=True)  # safe=True evita errores si ya existe
        print("INFO: Tablas creadas correctamente")
    except Exception as e:
        print("ERROR al crear tablas:", e)
    finally:
        if not db.is_closed():
            db.close()
