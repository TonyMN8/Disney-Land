# IMPORTACIONES.
# repositorios y modelos relacionados:
from repositories.visitante_repositories import VisitanteRepository
from repositories.atraccion_repositories import AtraccionRepository
from repositories.ticket_repositories import TicketRepository
from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel
from models.tickets_model import TicketModel
import json
from datetime import datetime

# ICONOS: https://symbl.cc/es

# Clase MenuVisitantes
# Tenemos la lista de las opciones de nuestra aplicación.

class MenuPrincipal:

    @staticmethod
    def menu_principal():
        while True:
            print("🎠 DISNEY LAND")
            print("\n1. MENU VISITANTES.")
            print("2. MENU ATRACCIONES.")
            print("3. MENU TICKETS")
            print("0. Cerrar el programa")
                
            opcion = input("\n➤  Selecciona una opcion: ").strip()
            print("")
                
            if opcion == "1":
                Visitantes.menu_visitantes()
            elif opcion == "2":
                Atracciones.menu_atracciones()
            elif opcion == "3":
                Tickets.menu_tickets()
            elif opcion == "0":
                break
            else:
                print("\nLa opcion que has introducido es invalida.")
                
            input("\n➤ Presiona Enter para continuar...")

# Clase Visitantes
# Agrupa toda la lógica relacionada con la gestión de visitantes:
# mostrar menú, crear, listar, buscar y eliminar visitantes
class Visitantes:

    # ____ MENU VISITANTES ____:
    @staticmethod
    def menu_visitantes():
        while True:
            print("👥 MENU: GESTION DE VISITANTES")
            print("\n1. Crear visitante.")
            print("2. Listar todos los visitantes.")
            print("3. Buscar visitante por email.")
            print("4. Eliminar visitante.")
            print("0. Volver al menú principal.")
            
            opcion = input("\n➤  Selecciona una opcion: ").strip()
            print("")
            
            if opcion == "1":
                Visitantes.crear_visitante()
            elif opcion == "2":
                Visitantes.listar_visitantes()
            elif opcion == "3":
                Visitantes.buscar_por_email()
            elif opcion == "4":
                Visitantes.eliminar_visitante()
            elif opcion == "0":
                break
            else:
                print("\nLa opcion que has introducido es invalida.")
            
            input("\n➤ Presiona Enter para continuar...")
    
    # ____ CREAR VISITANTE ____
    @staticmethod
    def crear_visitante():
        print("MENU VISITANTES: CREAR UN VISITANTE.")

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

            # Obtenemos el email mediante el modelo.
            email_existente =  VisitanteModel.get_or_none(VisitanteModel.email == email)
            # Validacion email repetido:
            if email_existente:
                print(f"ERROR: El email: {email} ya existe.")
            # Validacion '@' y '.':
            if "@" in email and "." in email:
                # Si el email contiene "@" y "." rompemos el bucle.
                break

            else:
                print("ERROR: El email debe contener '@' y '.'")
        
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
                
                # VALIDAR TIPO FAVORITO:
                while True:
                    tipo_favorito = input("Tipo favorito: ").strip()
                    if tipo_favorito:
                        break
                    else:
                        print("ERROR: Debes incluir un tipo favorito")

                # VALIDAR RESTRICCIONES:
                while True:
                    restricciones = input("Restricciones (Ejemplos: altura, vegano, panico extremo): ").strip()
                    if restricciones:
                        break
                    else:
                        print("ERROR: Debes incluir una restriccion")
                
                # Si introducimos una restriccion:
                if restricciones:
                    restricciones_coma = restricciones.split(",")
                    restricciones_lista = []
                    
                    # Añadimos las restricciones a la lista creada:
                    for recorrerRestricciones in restricciones_coma:
                        restricciones_lista.append(recorrerRestricciones)
                # En caso de no introducir nada, creamos una lista vacia.
                else:
                    restricciones_lista = []

                preferencias = {
                    "tipo_favorito": tipo_favorito,
                    "restricciones": restricciones_lista,
                    "historial_visitas": 0 # Al crear el visitante siempre tendra un historial de visitas vacio.
                }
                break # Salimos del bucle.
            
            elif  opt == "N":
                print("INFO: No incluyes preferencias al visitante.")
                preferencias = {
                    "tipo_favorito": "No especificado",
                    "restricciones": "Sin restriccion",
                    "historial_visitas": 0 # Al crear el visitante siempre tendra un historial de visitas vacio.
                }
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

    # ____ LISTAR TODOS LOS VISITANTES ____
    @staticmethod
    def listar_visitantes():
        listar_visitantes = VisitanteRepository.obtener_todos()
        if not listar_visitantes:
            return
        
        print("MENU VISITANTES: LISTA DE TODOS LOS VISITANTES:")

    # ____ BUSCAR POR EMAIL ____
    @staticmethod
    def buscar_por_email():
        email = input("Introduce el email del visitante: ").strip()
        VisitanteRepository.obtener_por_email(email)

    # ____ ELIMINAR VISITANTE ____
    @staticmethod
    def eliminar_visitante():
        listar_visitantes = VisitanteRepository.obtener_todos()

        if not listar_visitantes:
            return

        try:
            listar_visitantes()
            visitante_id = int(input("Introduce la ID del visitante que vas a liminar: "))
        except ValueError:
            print("ERROR: Debes ingresar una ID valida.")
            return

        # Confirmación antes de eliminar
        while True:
            confirm = input(f"Eliminar visitante con ID: {visitante_id}? (S)i / (N)o: ").strip().upper()
            if confirm == "S":
                VisitanteRepository.eliminar(visitante_id)
                break
            elif confirm == "N":
                print("INFO: Cancelas la operacion, no se ha eliminado el visitante.")
                break
            else:
                print("INFO: Debes responder (S)i / (N)o")

# Clase Atracciones
# Agrupa toda la lógica relacionada con la gestión de las atracciones:
# mostrar menú, crear, listar, buscar, eliminar atracciones, etc.
class Atracciones:
    # ____ MENU ATRACCIONES ____:
    @staticmethod
    def menu_atracciones():
        while True:
            print("🎡 MENU: GESTION DE ATRACCIONES")
            print("\n1. Crear una nueva atraccion.")
            print("2. Listar todas las atracciones.")
            print("3. Buscar atraccion por nombre.")
            print("4. Eliminar atraccion.")
            print("0. Volver al menú principal.")
            
            opcion = input("\n➤  Selecciona una opcion: ").strip()
            print("")
            
            if opcion == "1":
                Atracciones.crear_atraccion()
            elif opcion == "2":
                Atracciones.listar_atracciones()
            elif opcion == "3":
                Atracciones.buscar_nombre_atraccion()
            elif opcion == "4":
                Atracciones.eliminar_atraccion()
            elif opcion == "0":
                break
            else:
                print("\nLa opcion que has introducido es invalida.")
            
            input("\n➤ Presiona Enter para continuar...")
    
    # ____ VALIDAR HORA ____
    @staticmethod
    def validarHora(hora):
        try:
            return datetime.strptime(hora, "%H:%M").time()
        except Exception as e:
            print("ERROR:", e)


    # ____ CREAR ATRACCION ____
    @staticmethod
    def crear_atraccion():
        print("🎡 MENU ATRACCIONES: CREAR UNA ATRACCION.")

        # VALIDAR NOMBRE:
        while True:
            nombre = input("Nombre de la atracción: ").strip()

            # Obtenemos el nombre mediante el modelo.
            nombre_existente =  AtraccionModel.get_or_none(AtraccionModel.nombre == nombre)
            if nombre_existente:
                print(f"ERROR: El nombre de la atraccion: {nombre} ya existe.")

            # Si la variable nombre contiene algo, salimos del bucle.
            if nombre:
                break
            else:
                print("ERROR: El nombre no puede estar vacío")

        # VALIDAR TIPO:
        while True:
            tipo = input("Tipo de atracción (extrema, familiar, infantil, acuatica): ").strip().lower()
            # Si el tipo es igual a tipo in, salimos del bucle.
            if tipo in ["extrema", "familiar", "infantil", "acuatica", "acuática"]:
                break
            else:
                print("ERROR: Ingresa un tipo valido (extrema, familiar, infantil, acuatica)")

        # VALIDAR ALTURA (cm):
        while True:
            try:
                altura = int(input("Altura minima de la atraccion: "))
                # Si la altura es un INT y mayor a > 80.
                if altura > 80:
                    break
                else:
                    print("ERROR: La altura debe superior a 80cm")

            except Exception as e:
                print("ERROR: Introduce una altura valida.")

        # VALIDAR DETALLES:
        detalles = {}
        
        # VALIDAR DURACION (SEGUNDOS):      
        while True:
            try:
                duracion_atraccion = int(input("Duracion de la atraccion: "))
                if duracion_atraccion > 0:
                    detalles["duracion_segundos"] = duracion_atraccion
                    break
                else:
                    print("ERROR: La duracion debe ser mayor a 0")
            except Exception as e:
                print("ERROR: Introduce una duracion valida.")
        # VALIDAR CAPACIDAD POR TURNO:        
        while True:
            try:
                capacidad_turno = int(input("Capacidad de la atraccion: "))
                if capacidad_turno > 0:
                    detalles["capacidad_por_turno"] = capacidad_turno
                    break
                else:
                    print("ERROR: La capacidad de la atraccion debe ser mayor a 0")
            except Exception as e:
                print("ERROR: Introduce un valor valido, la capacidad debe ser mayor a 0.")

        # VALIDAR INTENSIDAD (MAYOR A 7):        
        while True:
            try:
                intensidad = int(input("Intensidad de la atraccion: "))
                if intensidad > 7:
                    detalles["intensidad"] = capacidad_turno
                    break
                else:
                    print("ERROR: La intensidad de la atraccion debe ser mayor a 7")
            except Exception as e:
                print("ERROR: Introduce un valor valido.")

        # VALIDAR CARACTERISTICAS: "looping", "caida_libre", "giro_360
        while True:
            print("Caracteristicas: looping, caida_libre, giro_360espirales, velocidad_baja, velocidad_alta, caida_agua, tobogan, carrusel")
            caracteristicas = input("Introduce una caracteristica: ").strip().lower()
            # Mas caracteristicas sacadas de internet: espirales, velocidad_baja, velocidad_alta, caida_agua, tobogan, carrusel
            if caracteristicas in ["looping", "caida_libre", "giro_360", "espirales", "velocidad_baja", "velocidad_alta", "caida_agua", "tobogan", "carrusel"]:
                caracteristicas_coma = caracteristicas.split(",")
                caracteristicas_lista = []

                # Añadimos las caracteristicas a la lista:
                for recorrerCaracteristicas in caracteristicas_coma:
                    caracteristicas_lista.append(recorrerCaracteristicas)
                    detalles ["caracteristicas"] = caracteristicas_lista
                break
            else:
                print("ERROR: Debes introducir una caracteristica valida: looping, caida_libre, giro_360.")

        # VALIDAR HORARIO:
        horarios = {}

        # Apertura.
        while True:
            apertura = input("Hora de apertura: ").strip()
            hora_apertura = Atracciones.validarHora(apertura)
            if hora_apertura:
                horarios["apertura"] = apertura
                break
            else:
                print("ERROR: La hora no es valida. Formato: HH:MM '09:30'")
        
        # Cierre.
        while True:
            cierre = input("Hora de cierre: ").strip()
            hora_cierre = Atracciones.validarHora(cierre)
            if hora_cierre:
                if hora_cierre > hora_apertura:
                    horarios["cierre"] = cierre
                    break
                else:
                    print("ERROR: La hora de cierre debe ser mayor que la hora de apertura.") 
            else:
                print("ERROR: La hora no es valida. [Formato]: HH:MM '09:30'")

       # VALIDAR HORARIOS DE MANTENIMIENTO:
        while True:
            horario_mantenimiento = []
            mantenimiento_1 = input("Primer horario del mantenimiento (Formato: HH:MM '09:30): ").strip()
            validar_mantenimiento_1 = Atracciones.validarHora(mantenimiento_1)
            mantenimiento_2 = input("Segundo horario del mantenimiento (Formato: HH:MM '09:30): ").strip()
            validar_mantenimiento_2 = Atracciones.validarHora(mantenimiento_2)

            if validar_mantenimiento_1 and validar_mantenimiento_2:
                if validar_mantenimiento_2 > validar_mantenimiento_1:
                    horario_mantenimiento.append(f"{mantenimiento_1}-{mantenimiento_2}")
                    break
                else:
                    print("ERROR: El mantenimiento no puede finalizar antes del primer horario.")     
            else:
                print("ERROR: La hora no es valida. Formato: HH:MM '09:30'")
        
        # Guardamos en el diccionario de horarios
        horarios["mantenimiento"] = horario_mantenimiento
        detalles["horarios"] = horarios

        # Atraccion activa si o no
        while True:
            atraccion_activa = input("Activar atraccion S(i)/ N(o): ").strip().upper()
            if atraccion_activa == "S":
                atraccion_activa = True
                break
            elif atraccion_activa == "N":
                atraccion_activa = False
                break
            else:
                print("ERROR: Introduce S(i) o N(o) para activar o no la atraccion.")
          
        try:
            # Creamos el visitante con el repositorio:
            AtraccionRepository.crear_atraccion(
                nombre=nombre,
                tipo=tipo,
                altura_minima=altura,
                detalles=detalles,
                activa=atraccion_activa
            )

        except Exception as e:
            print("ERROR: No se ha podido crear el visitante:", e)

    # ____ LISTAR TODAS LAS ATRACCIONES ____
    @staticmethod
    def listar_atracciones():
        listar_atracciones = AtraccionRepository.obtener_todos()
        if not listar_atracciones:
            return
        
        print("MENU ATRACCIONES: LISTA DE TODAS LAS ATRACCIONES:")

    # ____ BUSCAR POR NOMBRE DE LA ATRACCION ____
    @staticmethod
    def buscar_nombre_atraccion():
        nombre = input("Introduce el nombre de la atraccion: ").strip()
        AtraccionRepository.obtener_por_nombre(nombre)

    # ____ ELIMINAR ATRACCION ____
    @staticmethod
    def eliminar_atraccion():
        # Accedemos al repositorio de la atraccion, en el metodo obtener_todos.
        listar_atracciones = AtraccionRepository.obtener_todos()
        if listar_atracciones is False:
            return

        nombre_atraccion = input("Introduce el nombre de la atraccion que quieres eliminar: ").strip()
        # Confirmación antes de eliminar
        while True:
            confirm = input(f"Eliminar la atraccion con el nombre: {nombre_atraccion}? (S)i / (N)o: ").strip().upper()
            if confirm == "S":
                AtraccionRepository.eliminar(nombre_atraccion)
                break
            elif confirm == "N":
                print(f"INFO: Cancelas la operacion, no se ha eliminado la atraccion: {nombre_atraccion}.")
                break
            else:
                print("INFO: Debes responder (S)i / (N)o")

# Clase Tickets
# Agrupa toda la lógica relacionada con la gestión de tickets
class Tickets:

    # ____ MENU TICKETS ____
    @staticmethod
    def menu_tickets():
        while True:
            print("🧾 MENU: GESTION DE TICKETS")
            print("\n1. Crear ticket.")
            print("2. Listar todos los tickets.")
            print("3. Buscar ticket por ID.")
            print("4. Eliminar ticket.")
            print("0. Volver al menú principal.")
            
            opcion = input("\n➤ Selecciona una opcion: ").strip()
            print("")
            
            if opcion == "1":
                Tickets.crear_ticket()
            elif opcion == "2":
                Tickets.listar_tickets()
            elif opcion == "3":
                Tickets.buscar_ticket_id()
            elif opcion == "4":
                Tickets.eliminar_ticket()
            elif opcion == "0":
                break
            else:
                print("\nLa opcion que has introducido es invalida.")
            
            input("\n➤ Presiona Enter para continuar...")
