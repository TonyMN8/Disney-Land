from peewee import *
import envyte # type: ignore

db = PostgresqlDatabase(
    envyte.get("SUPABASE_DB_NAME"),       
    host=envyte.get("SUPABASE_DB_HOST"),             
    port=int(envyte.get("SUPABASE_DB_PORT")),
    user=envyte.get("SUPABASE_DB_USER"),
    password=envyte.get("SUPABASE_DB_PASSWORD")
)

try:
    db.connect()
    print("Conexión exitosa a la base de datos")
except Exception as e:
    print("Error al conectar:", e)
finally:
    if not db.is_closed():
        db.close()