from configuracion_db import inicializar_db
from database import conectar_db, cerrar_db
from menu.menu_visitantes import MenuVisitantes

def main():
    inicializar_db()
    conectar_db()
    menu = MenuVisitantes()
    menu.mostrar()
    cerrar_db()

if __name__ == "__main__":
    main()