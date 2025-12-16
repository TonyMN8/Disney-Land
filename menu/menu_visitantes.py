from repositories.visitante_repositories import VisitanteRepository
import json

# Menu para gestionar los visitantes:
class MenuVisitantes:

    # Esctructura base:
    def mostrar(self):
        while True:
            print("👥 MENU: GESTION DE VISITANTES")
            print("\n1. Crear visitante.")
            print("2. Listar todos los visitantes.")
            print("2. Buscar visitante por email.")
            print("3. Eliminar visitante.")
            print("0. Volver al menú principal.")
            
            opcion = input("\n➤  Selecciona una opcion: ").strip()
            print("")
            
            if opcion == "1":
                self._crear_visitante()
           
            elif opcion == "0":
                break
            else:
                print("\nLa opcion que has introducido es invalida.")
            
            input("\n➤ Presiona Enter para continuar...")
    
    # METODO AL CREAR EL VISITANTE:
    def _crear_visitante (self):
        print("MENU: CREAR UN VISITANTE.")

        # VALIDAR NOMBRE:
        while True:
            nombre = input("Nombre del visitante: ").strip()
            if nombre:
                # Si nombre contiene "nombre" rompemos el bucle.
                break
            else:
                print("ERROR: El nombre no puede estar vacio")

        # VALIDAR EMAIL:
        while True:
            email = input("Email del visitante: ").strip()
            if "@" in email and "." in email:
                # Si el email contiene "@" y "." rompemos el bucle.
                break
            else:
                print("ERROR: El email debe contener @ y .")
        
        # VALIDAR ALTURA (cm):
        while True:
            try:
                altura = int(input("Altura del visitante: "))
                # Si la altura es un INT y mayor a > 10.
                if altura > 10:
                    break
                else:
                    print("ERROR: La altura debe superior a 10cm")

            except Exception as e:
                print("ERROR: Introduce una altura valida")
                
        # PREFERENCIAS:
        preferencias = None
        while True:
            opt = input("Ingresar preferencias al visitante (S)i / (N)o: ").strip().upper()

            # En caso de querer preferencias:
            if opt == "S":
                tipo_favorito = input("Tipo favorito: ").strip()
                restricciones = input("Restricciones (Ejemplos: altura, vegano, panico extremo): ").strip()
                # Si introducimos una restriccion:
                if restricciones:
                    restricciones_coma = restricciones.split(",")
                    restricciones_lista = []
                    
                    # Añadimos las restricciones a la lista creada:
                    for recorrerRestricciones in restricciones_lista:
                        restricciones_lista.append(recorrerRestricciones)
                # En caso de no introducir nada, creamos una lista vacia.
                else:
                    restricciones_lista = []

                preferencias = {
                    "tipo_favorito": tipo_favorito,
                    "restricciones": restricciones,
                    "historial_visitas": [] # Al crear el visitante siempre tendra un historial de visitas vacio.
                }
                break # Salimos del bucle.
            
            elif  opt == "N":
                print("INFO: No incluyes preferencias al visitante.")
                break # Salimos del bucle.
            else:
                print("INFO: Debes responder (S)i / (N)o")
        try:
            # Creamos el visitante con el repositorio:
            VisitanteRepository.crear_visitante(
                nombre=nombre,
                email=email,
                altura=altura,
                preferencias=preferencias
            )

        except Exception as e:
            print("ERROR: No se ha podido crear el visitante:", e)