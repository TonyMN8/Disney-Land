from peewee import * # type: ignore
import envyte  # type: ignore
from playhouse.postgres_ext import PostgresqlExtDatabase  # type: ignore

db = PostgresqlExtDatabase(
    envyte.get("SUPABASE_DB_NAME"),
    host=envyte.get("SUPABASE_DB_HOST"),
    port=int(envyte.get("SUPABASE_DB_PORT")),
    user=envyte.get("SUPABASE_DB_USER"),
    password=envyte.get("SUPABASE_DB_PASSWORD")
)

def conectar_db():
    try:
        db.connect()
        print("BASE DE DATOS: Conexion con la base de datos")
    except Exception as e:
        print(f"DATABASE: ERROR al conectar: {e}")

def cerrar_db():
    try:
        if not db.is_closed():
            db.close()
            print("BASE DE DATOS: Conexión cerrada")
    except Exception as e:
        print(f"ERROR: No se ha podido cerrar la conexion de la base de datos:", e)