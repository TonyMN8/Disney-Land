from repositories.visitante_repositories import VisitanteRepositories
import json

# Menu para gestionar los visitantes:
class MenuVisitantes:

    # Esctructura base:
    def mostrar(self):
        while True:
 
            print("👥 MENU: GESTION DE VISITANTES")
            print("\n1. Crear visitante")
            print("2. Listar todos los visitantes")
            print("2. Buscar visitante por email.")
            print("3. Eliminar visitante")
            print("0. Volver al menú principal")
            
            opcion = input("\n➤  Selecciona una opcion: ").strip()
            
            if opcion == "1":
                print("METODO INCOMPLETO")
                # self._crear_visitante()
           
            elif opcion == "0":
                break
            else:
                print("\nLa opcion que has introducido es invalida.")
            
            input("\n➤ Presiona Enter para continuar...")
    
    # AÑADIR METODOS, CREAR, ETC.
  