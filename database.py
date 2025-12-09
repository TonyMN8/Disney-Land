from peewee import PostgresqlDatabase
import os
from dotenv import load_dotenv

load_dotenv()

# Obtener variables de entorno
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 5432))  # por si no está definida

# Crear la conexión a Supabase
db = PostgresqlDatabase(
    DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    sslmode="require"  # obligatorio para Supabase
)

# Probar conexión
if __name__ == "__main__":
    try:
        db.connect()
        print("Conexión exitosa a Supabase!")
        db.close()
    except Exception as e:
        print("Error al conectar:", e)
