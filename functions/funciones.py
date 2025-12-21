# IMPORTACIONES.
# repositorios y modelos relacionados:
from repositories.visitante_repositories import VisitanteRepository
from repositories.atraccion_repositories import AtraccionRepository
from repositories.ticket_repositories import TicketRepository
from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel

# Clase consultas:
from functions.consultas import Consultas

import json
from datetime import datetime

# ICONOS: https://symbl.cc/es

# Clase MenuVisitantes
# Tenemos la lista de las opciones de nuestra aplicación.

class MenuPrincipal:

    @staticmethod
    def menu_principal():
        while True:
            print("───────────────────────────────────────────────────────────────────────────────")
            print("🎠 PARQUE DE ATRACCIONES: DISNEY LAND")
            print("1. MENU VISITANTES.")
            print("2. MENU ATRACCIONES.")
            print("3. MENU TICKETS.")
            print("4. MENU CONSULTAS.")
            print("0. CERRAR EL PROGRAMA.")
            print("───────────────────────────────────────────────────────────────────────────────")
            print("© 2025 TonyMN8.")
            opcion = input("\n➤  Selecciona una opcion: ").strip()
            print("")
                
            if opcion == "1":
                Visitantes.menu_visitantes()
            elif opcion == "2":
                Atracciones.menu_atracciones()
            elif opcion == "3":
                Tickets.menu_tickets()
            elif opcion == "4":
                MenuConsultas.menu_consultas()
            elif opcion == "0":
                break
            else:
                print("\nLa opcion que has introducido es invalida.")
                
            input("\n➤ Presiona Enter para continuar...")

class MenuConsultas:
    @staticmethod
    def menu_consultas():
        while True:
            print("🔍 MENU: CONSULTAS")
            print("01. Visitantes con preferencia por atracciones extremas.")
            print("02. Atracciones con intensidad mayor a 7.")
            print("03. Tickets tipo colegio con precio menor a 30.")
            print("04. Atracciones con duracion mayor a 120 segundos.")
            print("05. Atracciones con (looping) y (caida libre).")
            print("06. Tickets con descuento (estudiante).")
            print("07. Atracciones con al menos un horario de mantenimiento.")
            print("08. Visitantes ordenados por cantidad total de tickets comprados.")
            print("09. (5) Atracciones mas vendidas.")
            print("10. Visitantes que han gastado mas de 100€.")
            print("11. Atracciones comparibles para un visitante.")
            print("0. Volver al menu principal.")
            
            opcion = input("\n➤ Selecciona una opcion: ").strip()
            print("")
            
            if opcion == "1":
                Consultas.preferencia_extrema()
            elif opcion == "2":
                Consultas.atracciones_intensidad()
            elif opcion == "3":
                Consultas.tickets_colegio()
            elif opcion == "4":
                Consultas.atracciones_duracion()
            elif opcion == "5":
                Consultas.atracciones_caracteristicas()
            elif opcion == "6":
                Consultas.tickets_descuento()
            elif opcion == "7":
                Consultas.atracciones_mantenimiento()
            elif opcion == "8":
                Consultas.visitantes_por_tickets()
            elif opcion == "9":
                Consultas.atracciones_vendidas()
            elif opcion == "10":
                Consultas.visitantes_mas_gastado()
            elif opcion == "11":
                Consultas.atracciones_compatibles()
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
            print("5. Añadir visita al historial del visitante.")
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
            elif opcion == "5":
               Visitantes.anadir_visita()
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

        while True:
            email = input("Email del visitante: ").strip()

            # Obtenemos el email mediante el modelo.
            email_existente = VisitanteModel.get_or_none(VisitanteModel.email == email)

            # Validación email repetido:
            if email_existente:
                print(f"ERROR: El email: {email} ya existe.")
            # Validación '@' y '.':
            elif "@" not in email or "." not in email:
                print("ERROR: El email debe contener '@' y '.'")
            else:
                # Si pasa ambas validaciones, rompemos el bucle
                break
        
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
        print("MENU VISITANTES: LISTA DE TODOS LOS VISITANTES:")
        listar_visitantes = VisitanteRepository.obtener_todos()
        if not listar_visitantes:
            return
    
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
    
    # METODOS NO RELACIONADOS CON EL CRUD:
    # ANADIR VISITA AL HISTORIAL DE UN VISITANTE
    @staticmethod
    def anadir_visita():
        # Mostramos todos los visitantes
        visitantes = VisitanteRepository.obtener_todos()
        if not visitantes:
            print("INFO: No hay visitantes registrados.")
            return
        
        while True:
            try:
                visitante_id = int(input("Introduce la ID del visitante: "))
                break
            except Exception:
                print("ERROR: Introduce una ID valida.")

        # Fecha de la visita
        while True:
            fecha = input("Introduce la fecha de la visita (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(fecha, "%Y-%m-%d")
                break
            except Exception:
                print("ERROR: Fecha no valida. Formato correcto: YYYY-MM-DD")

        # Numero de atracciones visitadas
        while True:
            try:
                atracciones_visitadas = int(input("Numero de atracciones visitadas: "))
                if atracciones_visitadas >= 0:
                    break
                else:
                    print("ERROR: El numero no puede ser negativo.")
            except Exception:
                print("ERROR: Introduce un numero valido.")

        # Llamamos al repositorio
        VisitanteRepository.anadir_visita(
            visitante_id,
            fecha,
            atracciones_visitadas
        )

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
            print("5. Cambiar el estado de la atraccion.")
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
            elif opcion == "5":
                Atracciones.cambiar_estado()
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

    # METODOS NO RELACIONADOS CON EL CRUD:
    # MARCAR TICKET COMO USADO
    @staticmethod
    def cambiar_estado():
         # Accedemos al repositorio de los tickets
        listar_atraccion = AtraccionRepository.obtener_todos()
        if listar_atraccion is False:
            return
        
        while True:
            nombre_atraccion = input("Introduce el nombre de la atraccion: ")
            AtraccionRepository.cambiar_estado(nombre_atraccion)
            break

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
            print("5. Marcar ticket.")
            print("6. Mostrar tickets de los visitantes.")
            print("7. Mostrar tickets de una atraccion.")
            print("8. Cambiar el precio de un ticket. ")
            print("0. Volver al menú principal.")
            
            opcion = input("\n➤ Selecciona una opcion: ").strip()
            print("")
            
            if opcion == "1":
                Tickets.crear_ticket()
            elif opcion == "2":
                Tickets.listar_tickets()
            elif opcion == "3":
                Tickets.buscar_id_ticket()
            elif opcion == "4":
                Tickets.eliminar_ticket()
            elif opcion == "5":
                Tickets.marcar_ticket()
            elif opcion == "6":
                Tickets.tickets_visitante()
            elif opcion == "7":
                Tickets.tickets_atraccion()
            elif opcion == "8":
                Tickets.cambiar_precio_ticket()
            elif opcion == "0":
                break
            else:
                print("\nLa opcion que has introducido es invalida.")
            
            input("\n➤ Presiona Enter para continuar...")

 # ____ CREAR TICKET ____ 
    @staticmethod
    def crear_ticket():
        print("🧾 MENU TICKETS: CREAR UN TICKET.")

        # SELECCIONAR AL VISITANTE
        listar_visitantes = VisitanteRepository.obtener_todos()
        if listar_visitantes is False:
            return

        try:
            visitante_id = int(input("Introduce el ID del visitante: "))
        except ValueError:
            print("ERROR: Ingresa un ID valido.")
            return

        visitante = VisitanteModel.get_or_none(VisitanteModel.id == visitante_id)
        if not visitante:
            print("ERROR: No se ha encontrado el visitante.")
            return

        # SELECCIONAR LA ATRACCION:
        listar_atracciones = AtraccionRepository.obtener_todos()
        if not listar_atracciones:
            print("ERROR: No hay atracciones registradas.")
            return

        while True:
            try:
                atraccion_id = int(input("Introduce la ID de la atraccion: "))
                atraccion = AtraccionModel.get_or_none(AtraccionModel.id == atraccion_id)
                if atraccion:
                    break
                else:
                    print("ERROR: La atraccion no existe.")

            except Exception as e:
                print("ERROR: Ingresa un ID valido.")

        # Tipo de ticket
        while True:
            tipo_ticket = input("Tipo de ticket (general, colegio, empleado): ").strip().lower()
            if tipo_ticket in ["general", "colegio", "empleado"]:
                break
            else:
                print("ERROR: Debes introducir un tipo de ticket valido: General, colegio o empleado.")

        # Fecha visita
        while True:
            fecha_visita_input = input("Fecha de visita (YYYY-MM-DD): ").strip()
            try:
                fecha_visita = datetime.strptime(fecha_visita_input, "%Y-%m-%d").date()
                break
            except:
                print("ERROR: La fecha no es valida. Formato: YYYY-MM-DD '2012-12-05'")

        # Detalles de compra
        detalles_compra = {}
        while True:
            try:
                detalles_compra["precio"] = float(input("Precio: "))
                break
            except ValueError:
                print("ERROR: Ingresa un precio valido. Formato: 15.30")

        # Descuentos aplicados.
        while True:
            agregar_descuentos = input("Aplicar descuentos (S)i / (N)o: ").strip().upper()
            if agregar_descuentos == "SI":
                descuentos = input("Introduce los descuentos (Estudiante o Early Bird) separados por coma: ").strip().lower()
                lista_descuentos = []
                descuentos_validos = ["estudiante", "early bird"]

                # Recorremos cada descuento ingresado
                for recorrerDescuento in descuentos.split(","):
                    recorrerDescuento = recorrerDescuento.strip()
                    if recorrerDescuento not in descuentos_validos:
                        print(f"ERROR: Introduce un descuento válido.")
                        break
                    else:
                        lista_descuentos.append(recorrerDescuento)
                # Si los descuentos son validos:
                else:
                    detalles_compra["descuentos_aplicados"] = lista_descuentos
                    break  # Salimos del while

            elif agregar_descuentos == "NO":
                detalles_compra["descuentos_aplicados"] = []
                break
            else:
                print("ERROR: Debes responder Si o No.")

        # Servicios extra fast_pass", "comida_incluida
        while True:
            agregar_servicio = input("Agregar servicios extra (S)i / (N)o: ").strip().upper()
            if agregar_servicio == "SI":
                servicios = input("Introduce los servicios extra (Fast Pass o Comida Incluida): ").strip().lower()
                lista_servicios = []
                servicios_validos = ["fast pass", "comida incluida"]

                # Recorremos cada servicio ingresado
                for recorrerServicio in servicios.split(","):
                    recorrerServicio = recorrerServicio.strip()
                    if recorrerServicio not in servicios_validos:
                        print(f"ERROR: Introduce un servicio valido.")
                        break 
                    else:
                        lista_servicios.append(recorrerServicio)
                # Si los servicios son validos:
                else:
                    detalles_compra["servicios_extra"] = lista_servicios
                    break

            elif agregar_servicio == "NO":
                detalles_compra["servicios_extra"] = []
                break
            else:
                print("ERROR: Debes responder Si o No.")

        # VALIDAR METODO DE PAGO
        while True:
            metodo_pago = input("Metodo de pago (Tarjeta o Efectivo): ").strip().lower()
            if metodo_pago in ["tarjeta", "efectivo"]:
                detalles_compra["metodo_pago"] = metodo_pago
                break
            else:
                print("ERROR: Debes introducir 'Tarjeta' o 'Efectivo'")

        # Creamos el repositorio despues de pasar todas las validaciones:
        TicketRepository.crear_ticket(
            visitante=visitante,
            atraccion=atraccion,
            fecha_visita=fecha_visita,
            tipo_ticket=tipo_ticket,
            detalles_compra=detalles_compra
        )

    # ____ LISTAR TODOS LOS TICKETS ____
    @staticmethod
    def listar_tickets():
        listar_tickets = TicketRepository.obtener_todos()
        if not listar_tickets:
            return

        print("🧾 MENU TICKETS: LISTA DE TODOS LOS TICKETS:")

    # ____ BUSCAR TICKET POR ID ____
    @staticmethod
    def buscar_id_ticket():
        try:
            id_ticket = int(input("Introduce la ID del ticket: ").strip())
            TicketRepository.obtener_por_id(id_ticket)
        except Exception:
            print("ERROR: Introduce un ID correcto.")

    # ____ ELIMINAR TICKET ____
    @staticmethod
    def eliminar_ticket():
        # Accedemos al repositorio de los tickets
        listar_tickets = TicketRepository.obtener_todos()
        if listar_tickets is False:
            return
        
        while True:
            id = input("Introduce la ID del ticket que quieres eliminar: ").strip()
            
            # Validamos el ID
            if not id.isdigit():
                print("ERROR: Introduce un ID correcto.")
            else:
                id_ticket = int(id)
                confirm = input(f"Eliminar el ticket ID: {id_ticket}? (S)i / (N)o: ").strip().upper()
                
                if confirm == "S":
                    TicketRepository.eliminar(id_ticket)
                    break  # Salimos al eliminar
                elif confirm == "N":
                    print(f"INFO: Cancelas la operación, no se ha eliminado el ticket ID: {id_ticket}.")
                    break # Salimos al cancelar
                else:
                    print("INFO: Debes responder (S)i / (N)o")
    
    # METODOS NO RELACIONADOS CON EL CRUD:
    # MARCAR TICKET COMO USADO
    @staticmethod
    def marcar_ticket():
        while True:
            try:
                ticket_id = int(input("Introduce la ID del ticket: "))
                TicketRepository.ticket_usado(ticket_id)
                break

            except Exception:
                print("ERROR: Introduce un ID correcto.")
    
    # OBTENER LOS TICKETS DE UN VISITANTE
    @staticmethod
    def tickets_visitante():
        print("🧾 CONSULTA: Tickets de un visitante específico")
        visitantes = VisitanteRepository.obtener_todos()
        if not visitantes:
            print("INFO: No hay visitantes registrados.")
            return
        
        try:
            visitante_id = int(input("Introduce el ID del visitante: ").strip())
        except ValueError:
            print("ERROR: Introduce un ID correcto.")
            return
        
        TicketRepository.obtener_por_visitante(visitante_id)

    # OBTENER LOS TICKETS DE UNA ATRACCION
    @staticmethod
    def tickets_atraccion():
        print("🧾 CONSULTA: Tickets vendidos para una atraccion")
        # Listamos todas las atracciones
        atracciones = AtraccionRepository.obtener_todos()
        if not atracciones:
            print("INFO: No hay atracciones registradas.")
            return
        
        while True:
            atraccion_id_input = input("Introduce el ID de la atraccion: ").strip()
            if not atraccion_id_input.isdigit():
                print("ERROR: Introduce un ID correcto.")
            else:
                atraccion_id = int(atraccion_id_input)
                # Llamamos al repositorio si la ID es valida:
                TicketRepository.obtener_por_atraccion(atraccion_id)
                break

    # CAMBIAR PRECIO DE UN TICKET
    @staticmethod
    def cambiar_precio_ticket():
        tickets = TicketRepository.obtener_todos() # Mostramos todos los tickets
        if not tickets:
            print("INFO: No hay tickets.")
            return
        
        while True:
            try:
                ticket_id = int(input("Introdue la ID del ticket: "))
                nuevo_precio = float(input("Introduce el nuevo precio: "))
                break
            except Exception:
                print("ERROR: Ingresa un numero valido.")

        TicketRepository.cambiar_precio(ticket_id, nuevo_precio)