from repositories.visitante_repositorie import VisitanteRepositorie
from repositories.atraccion_repositorie import AtraccionRepositorie
from repositories.ticket_repositorie import TicketRepositorie
import json
from datetime import datetime, date

def validar_email(email):
    """Validar formato de email"""
    return '@' in email and '.' in email

def validar_entero(valor, mensaje="Ingrese un número válido: "):
    """Validar que el input sea un entero"""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número entero")

def validar_float(valor, mensaje="Ingrese un número válido: "):
    """Validar que el input sea un float"""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número válido")

def validar_fecha(mensaje="Ingrese fecha (YYYY-MM-DD): "):
    """Validar formato de fecha"""
    while True:
        try:
            fecha_str = input(mensaje)
            return datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            print("Error: Formato de fecha inválido. Use YYYY-MM-DD")

# ============== FUNCIONES CRUD VISITANTES ==============

def crear_visitante_menu():
    """Menú para crear un visitante"""
    print("\n=== CREAR VISITANTE ===")
    nombre = input("Nombre: ")
    
    while True:
        email = input("Email: ")
        if validar_email(email):
            break
        print("Error: Email inválido")
    
    altura = validar_entero(None, "Altura (cm): ")
    
    print("\n¿Desea agregar preferencias? (s/n): ", end="")
    if input().lower() == 's':
        preferencias = {}
        preferencias['tipo_favorito'] = input("Tipo favorito (extrema/familiar/infantil/acuatica): ")
        
        restricciones = input("Restricciones (separadas por comas): ").split(',')
        preferencias['restricciones'] = [r.strip() for r in restricciones if r.strip()]
        
        preferencias['historial_visitas'] = []
        
        visitante = VisitanteRepositorie.crear_visitante(nombre, email, altura, preferencias)
    else:
        visitante = VisitanteRepositorie.crear_visitante(nombre, email, altura)
    
    if visitante:
        print(f"✓ Visitante creado con ID: {visitante.id}")
    else:
        print("✗ Error al crear visitante")

def listar_visitantes():
    """Listar todos los visitantes"""
    print("\n=== LISTA DE VISITANTES ===")
    visitantes = VisitanteRepositorie.obtener_todos_visitantes()
    
    if not visitantes:
        print("No hay visitantes registrados")
        return
    
    for v in visitantes:
        print(f"\nID: {v.id}")
        print(f"Nombre: {v.nombre}")
        print(f"Email: {v.email}")
        print(f"Altura: {v.altura} cm")
        print(f"Fecha registro: {v.fecha_registro}")
        if v.preferencias:
            print(f"Preferencias: {json.dumps(v.preferencias, indent=2)}")

def eliminar_visitante_menu():
    """Menú para eliminar un visitante"""
    print("\n=== ELIMINAR VISITANTE ===")
    visitante_id = validar_entero(None, "ID del visitante: ")
    
    if VisitanteRepositorie.eliminar_visitante(visitante_id):
        print("✓ Visitante eliminado exitosamente")
    else:
        print("✗ Error al eliminar visitante")

# ============== FUNCIONES CRUD ATRACCIONES ==============

def crear_atraccion_menu():
    """Menú para crear una atracción"""
    print("\n=== CREAR ATRACCIÓN ===a")
    nombre = input("Nombre: ")
    
    print("\nTipos disponibles: extrema, familiar, infantil, acuatica")
    tipo = input("Tipo: ")
    
    altura_minima = validar_entero(None, "Altura mínima (cm): ")
    
    print("\n¿Desea agregar detalles? (s/n): ", end="")
    if input().lower() == 's':
        detalles = {}
        detalles['duracion_segundos'] = validar_entero(None, "Duración (segundos): ")
        detalles['capacidad_por_turno'] = validar_entero(None, "Capacidad por turno: ")
        detalles['intensidad'] = validar_entero(None, "Intensidad (1-10): ")
        
        caracteristicas = input("Características (separadas por comas): ").split(',')
        detalles['caracteristicas'] = [c.strip() for c in caracteristicas if c.strip()]
        
        detalles['horarios'] = {
            'apertura': input("Hora apertura (HH:MM): "),
            'cierre': input("Hora cierre (HH:MM): "),
            'mantenimiento': []
        }
        
        atraccion = AtraccionRepositorie.crear_atraccion(nombre, tipo, altura_minima, detalles)
    else:
        atraccion = AtraccionRepositorie.crear_atraccion(nombre, tipo, altura_minima)
    
    if atraccion:
        print(f"✓ Atracción creada con ID: {atraccion.id}")
    else:
        print("✗ Error al crear atracción")

def listar_atracciones():
    """Listar todas las atracciones"""
    print("\n=== LISTA DE ATRACCIONES ===")
    atracciones = AtraccionRepositorie.obtener_todas_atracciones()
    
    if not atracciones:
        print("No hay atracciones registradas")
        return
    
    for a in atracciones:
        print(f"\nID: {a.id}")
        print(f"Nombre: {a.nombre}")
        print(f"Tipo: {a.tipo}")
        print(f"Altura mínima: {a.altura_minima} cm")
        print(f"Activa: {'Sí' if a.activa else 'No'}")
        if a.detalles:
            print(f"Detalles: {json.dumps(a.detalles, indent=2)}")

def cambiar_estado_atraccion_menu():
    """Cambiar estado de una atracción"""
    print("\n=== CAMBIAR ESTADO ATRACCIÓN ===")
    atraccion_id = validar_entero(None, "ID de la atracción: ")
    print("Estado: 1=Activa, 0=Inactiva")
    estado = validar_entero(None, "Nuevo estado: ")
    
    if AtraccionRepositorie.cambiar_estado_atraccion(atraccion_id, bool(estado)):
        print("✓ Estado cambiado exitosamente")
    else:
        print("✗ Error al cambiar estado")

def eliminar_atraccion_menu():
    """Eliminar una atracción"""
    print("\n=== ELIMINAR ATRACCIÓN ===")
    atraccion_id = validar_entero(None, "ID de la atracción: ")
    
    if AtraccionRepositorie.eliminar_atraccion(atraccion_id):
        print("✓ Atracción eliminada exitosamente")
    else:
        print("✗ Error al eliminar atracción")

# ============== FUNCIONES CRUD TICKETS ==============

def crear_ticket_menu():
    """Menú para crear un ticket"""
    print("\n=== CREAR TICKET ===")
    visitante_id = validar_entero(None, "ID del visitante: ")
    
    print("¿Es ticket general? (s/n): ", end="")
    es_general = input().lower() == 's'
    
    atraccion_id = None
    if not es_general:
        atraccion_id = validar_entero(None, "ID de la atracción: ")
    
    fecha_visita = validar_fecha("Fecha de visita (YYYY-MM-DD): ")
    
    print("\nTipos de ticket: general, colegio, empleado")
    tipo_ticket = input("Tipo de ticket: ")
    
    detalles_compra = {}
    detalles_compra['precio'] = validar_float(None, "Precio: ")
    
    descuentos = input("Descuentos aplicados (separados por comas): ").split(',')
    detalles_compra['descuentos_aplicados'] = [d.strip() for d in descuentos if d.strip()]
    
    servicios = input("Servicios extra (separados por comas): ").split(',')
    detalles_compra['servicios_extra'] = [s.strip() for s in servicios if s.strip()]
    
    detalles_compra['metodo_pago'] = input("Método de pago: ")
    
    ticket = TicketRepositorie.crear_ticket(
        visitante_id, fecha_visita, tipo_ticket, detalles_compra, atraccion_id
    )
    
    if ticket:
        print(f"✓ Ticket creado con ID: {ticket.id}")
    else:
        print("✗ Error al crear ticket")

def listar_tickets():
    """Listar todos los tickets"""
    print("\n=== LISTA DE TICKETS ===")
    tickets = TicketRepositorie.obtener_todos_tickets()
    
    if not tickets:
        print("No hay tickets registrados")
        return
    
    for t in tickets:
        print(f"\nID: {t.id}")
        print(f"Visitante ID: {t.visitante.id} - {t.visitante.nombre}")
        print(f"Atracción: {'General' if t.atraccion is None else t.atraccion.nombre}")
        print(f"Tipo: {t.tipo_ticket}")
        print(f"Fecha visita: {t.fecha_visita}")
        print(f"Usado: {'Sí' if t.usado else 'No'}")
        if t.detalles_compra:
            print(f"Detalles: {json.dumps(t.detalles_compra, indent=2)}")

def marcar_ticket_usado_menu():
    """Marcar un ticket como usado"""
    print("\n=== MARCAR TICKET USADO ===")
    ticket_id = validar_entero(None, "ID del ticket: ")
    
    if TicketRepositorie.marcar_ticket_usado(ticket_id):
        print("✓ Ticket marcado como usado")
    else:
        print("✗ Error al marcar ticket")

# ============== CONSULTAS ==============

def consultas_menu():
    """Menú de consultas"""
    while True:
        print("\n=== MENÚ DE CONSULTAS ===")
        print("1. Visitantes con preferencia extrema")
        print("2. Atracciones con intensidad > 7")
        print("3. Tickets colegio < 30€")
        print("4. Atracciones duración > 120 seg")
        print("5. Visitantes con problemas cardíacos")
        print("6. Atracciones con looping y caída libre")
        print("7. Tickets con descuento estudiante")
        print("8. Atracciones con mantenimiento")
        print("9. Visitantes por cantidad de tickets")
        print("10. Top 5 atracciones más vendidas")
        print("11. Visitantes que gastaron > 100€")
        print("12. Atracciones compatibles visitante")
        print("0. Volver")
        
        opcion = validar_entero(None, "\nSeleccione una opción: ")
        
        if opcion == 0:
            break
        elif opcion == 1:
            visitantes = VisitanteRepositorie.visitantes_con_preferencia_extrema()
            print(f"\nEncontrados {len(visitantes)} visitantes")
            for v in visitantes:
                print(f"- {v.nombre} ({v.email})")
        
        elif opcion == 2:
            atracciones = AtraccionRepositorie.atracciones_intensidad_mayor(7)
            print(f"\nEncontradas {len(atracciones)} atracciones")
            for a in atracciones:
                intensidad = a.detalles.get('intensidad', 'N/A')
                print(f"- {a.nombre} (Intensidad: {intensidad})")
        
        elif opcion == 3:
            tickets = TicketRepositorie.tickets_tipo_colegio_precio_menor(30)
            print(f"\nEncontrados {len(tickets)} tickets")
            for t in tickets:
                precio = t.detalles_compra.get('precio', 'N/A')
                print(f"- Ticket {t.id} - Precio: {precio}€")
        
        elif opcion == 4:
            atracciones = AtraccionRepositorie.atracciones_duracion_mayor(120)
            print(f"\nEncontradas {len(atracciones)} atracciones")
            for a in atracciones:
                duracion = a.detalles.get('duracion_segundos', 'N/A')
                print(f"- {a.nombre} (Duración: {duracion}s)")
        
        elif opcion == 5:
            visitantes = VisitanteRepositorie.visitantes_con_problemas_cardiacos()
            print(f"\nEncontrados {len(visitantes)} visitantes")
            for v in visitantes:
                print(f"- {v.nombre} ({v.email})")
        
        elif opcion == 6:
            atracciones = AtraccionRepositorie.atracciones_con_caracteristicas(['looping', 'caida_libre'])
            print(f"\nEncontradas {len(atracciones)} atracciones")
            for a in atracciones:
                print(f"- {a.nombre}")
        
        elif opcion == 7:
            tickets = TicketRepositorie.tickets_con_descuento('estudiante')
            print(f"\nEncontrados {len(tickets)} tickets")
            for t in tickets:
                print(f"- Ticket {t.id} - Visitante: {t.visitante.nombre}")
        
        elif opcion == 8:
            atracciones = AtraccionRepositorie.atracciones_con_mantenimiento()
            print(f"\nEncontradas {len(atracciones)} atracciones")
            for a in atracciones:
                print(f"- {a.nombre}")
        
        elif opcion == 9:
            visitantes = VisitanteRepositorie.visitantes_ordenados_por_tickets()
            print("\nVisitantes ordenados por tickets:")
            for v in visitantes:
                total = getattr(v, 'total_tickets', 0)
                print(f"- {v.nombre}: {total} tickets")
        
        elif opcion == 10:
            atracciones = AtraccionRepositorie.atracciones_mas_vendidas(5)
            print("\nTop 5 atracciones más vendidas:")
            for a in atracciones:
                total = getattr(a, 'total_tickets', 0)
                print(f"- {a.nombre}: {total} tickets")
        
        elif opcion == 11:
            visitantes = VisitanteRepositorie.visitantes_gastado_mas_de(100)
            print("\nVisitantes que gastaron más de 100€:")
            for v in visitantes:
                total = getattr(v, 'total_gastado', 0)
                print(f"- {v.nombre}: {total}€")
        
        elif opcion == 12:
            visitante_id = validar_entero(None, "ID del visitante: ")
            atracciones = AtraccionRepositorie.atracciones_compatibles_visitante(visitante_id)
            print(f"\nAtracciones compatibles:")
            for a in atracciones:
                print(f"- {a.nombre} ({a.tipo})")

# ============== MODIFICACIONES JSONB ==============

def modificaciones_jsonb_menu():
    """Menú de modificaciones JSONB"""
    while True:
        print("\n=== MODIFICACIONES JSONB ===")
        print("1. Cambiar precio de ticket")
        print("2. Eliminar restricción de visitante")
        print("3. Agregar característica a atracción")
        print("4. Agregar visita a historial")
        print("0. Volver")
        
        opcion = validar_entero(None, "\nSeleccione una opción: ")
        
        if opcion == 0:
            break
        elif opcion == 1:
            ticket_id = validar_entero(None, "ID del ticket: ")
            nuevo_precio = validar_float(None, "Nuevo precio: ")
            if TicketRepositorie.cambiar_precio_ticket(ticket_id, nuevo_precio):
                print("✓ Precio actualizado")
            else:
                print("✗ Error")
        
        elif opcion == 2:
            visitante_id = validar_entero(None, "ID del visitante: ")
            restriccion = input("Restricción a eliminar: ")
            if VisitanteRepositorie.eliminar_restriccion(visitante_id, restriccion):
                print("✓ Restricción eliminada")
            else:
                print("✗ Error")
        
        elif opcion == 3:
            atraccion_id = validar_entero(None, "ID de la atracción: ")
            caracteristica = input("Nueva característica: ")
            if AtraccionRepositorie.agregar_caracteristica(atraccion_id, caracteristica):
                print("✓ Característica agregada")
            else:
                print("✗ Error")
        
        elif opcion == 4:
            visitante_id = validar_entero(None, "ID del visitante: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            atracciones = validar_entero(None, "Número de atracciones visitadas: ")
            if VisitanteRepositorie.agregar_visita_historial(visitante_id, fecha, atracciones):
                print("✓ Visita agregada")
            else:
                print("✗ Error")