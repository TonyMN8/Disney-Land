from configuracion_db import inicializar_db
from database import conectar_db, cerrar_db
from functions.ingesta import ingesta_masiva
from functions.funciones import MenuPrincipal

def main():
    conectar_db()
    inicializar_db()

    try:
        ingesta_masiva()
        MenuPrincipal.menu_principal()
    except Exception as e:
        print("ERROR en la ingesta:", e)
    finally:
        cerrar_db()

if __name__ == "__main__":
    main()
