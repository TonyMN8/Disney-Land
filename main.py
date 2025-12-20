from configuracion_db import inicializar_db
from database import conectar_db, cerrar_db
from functions.funciones import MenuPrincipal

def main():
    inicializar_db() 
    conectar_db()
    
    try:
        MenuPrincipal.menu_principal() 
    except Exception as e:
        print("ERROR:", e)
    finally:
        cerrar_db()

if __name__ == "__main__":
    main()