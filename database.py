from peewee import * # type: ignore
import envyte  # type: ignore

db = PostgresqlDatabase(
    envyte.get("SUPABASE_DB_NAME"),
    host=envyte.get("SUPABASE_DB_HOST"),
    port=int(envyte.get("SUPABASE_DB_PORT")),
    user=envyte.get("SUPABASE_DB_USER"),
    password=envyte.get("SUPABASE_DB_PASSWORD")
)

def conectar_db():
    # Conexion a la base de datos, modo de prueba: # Tony
    try:
        db.connect()
        print("Conexion con la base de datos")
    except Exception as e:
        print(f"Error al conectar: {e}")

def cerrar_db():
    try:
        if not db.is_closed():
            db.close()
            print("BASE DE DATOS: Conexión cerrada")
        else:
            print("BASE DE DATOS: La conexión ya estaba cerrada")
    except Exception as e:
        print("ERROR: No se ha podido cerrar la conexion de la base de datos.")

# Llamadas a la conexion y al cierre temporal, esto se debe cambiar:
conectar_db()
cerrar_db()