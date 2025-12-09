from peewee import *
import envyte # type: ignore

db = PostgresqlDatabase(
    envyte.get("SUPABASE_DB_NAME"),       
    host=envyte.get("SUPABASE_DB_HOST"),             
    port=int(envyte.get("SUPABASE_DB_PORT")),
    user=envyte.get("SUPABASE_DB_USER"),
    password=envyte.get("SUPABASE_DB_PASSWORD")
)
def conectar_db():
    """Conectar a la base de datos"""
    try:
        db.connect()
        print("✓ Conexión exitosa a la base de datos")
        return True
    except Exception as e:
        print(f"✗ Error al conectar: {e}")
        return False

def cerrar_db():
    """Cerrar la conexión a la base de datos"""
    if not db.is_closed():
        db.close()
        print("✓ Conexión cerrada")