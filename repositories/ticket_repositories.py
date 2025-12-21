# IMPORTACIONES
from models.tickets_model import TicketModel
from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel

from datetime import datetime, date

# ICONOS: https://symbl.cc/es
class TicketRepository:
    @staticmethod
    # METODO CREAR TICKET
    def crear_ticket(visitante, atraccion, fecha_visita, tipo_ticket, detalles_compra, usado=False, fecha_uso=None):
        try:
            ticket = TicketModel.create(
                visitante=visitante,
                atraccion=atraccion,
                fecha_visita=fecha_visita,
                tipo_ticket=tipo_ticket,
                detalles_compra=detalles_compra,
                usado=usado,
                fecha_uso=fecha_uso
            )
            print(f"Se ha creado el ticket ID: {ticket.id} para el visitante {visitante.nombre}")
        except Exception as e:
            print(f"ERROR: No se ha podido crear el ticket:", e)

    # OBTENER TODOS LOS TICKETS
    @staticmethod
    def obtener_todos():
        tickets = TicketModel.select()
        if tickets:
            for ticket in tickets:
                detalles = ticket.detalles_compra

                print(f"🧾 TICKET ID: {ticket.id} | Visitante: {ticket.visitante.nombre} | "
                      f"Atraccion: {ticket.atraccion.nombre if ticket.atraccion else 'N/A'} | "
                      f"Tipo: {ticket.tipo_ticket}")
                
                print(f"(-) Fecha compra: {ticket.fecha_compra} | Fecha visita: {ticket.fecha_visita}")
                print(f"(-) Usado: {'Si' if ticket.usado else 'No'} | Fecha uso: {ticket.fecha_uso if ticket.fecha_uso else 'N/A'}")
                
                print(f"(-) Detalles de compra: Precio {detalles.get('precio', 0.0)} | "
                      f"Descuentos: {', '.join(detalles.get('descuentos_aplicados', [])) if detalles.get('descuentos_aplicados') else 'Ninguno'} | "
                      f"Servicios extra: {', '.join(detalles.get('servicios_extra', [])) if detalles.get('servicios_extra') else 'Ninguno'} | "
                      f"Metodo pago: {detalles.get('metodo_pago', 'N/A')}")
            # Retornamos los tickets:
            return tickets
        else:
            print("INFO: No hay tickets registrados.")
            return False

    # OBTENER TICKET POR ID
    @staticmethod
    def obtener_por_id(ticket_id):
        ticket = TicketModel.get_or_none(TicketModel.id == ticket_id)
        if ticket:
            detalles = ticket.detalles_compra
            print(f"🧾 TICKET ID: {ticket.id} | Visitante: {ticket.visitante.nombre} | "
                  f"Atraccion: {ticket.atraccion.nombre if ticket.atraccion else 'N/A'} | "
                  f"Tipo: {ticket.tipo_ticket}")
                
            print(f"(-) Fecha compra: {ticket.fecha_compra} | Fecha visita: {ticket.fecha_visita}")
            print(f"(-) Usado: {'Si' if ticket.usado else 'No'} | Fecha uso: {ticket.fecha_uso if ticket.fecha_uso else 'N/A'}")
                
            print(f"(-) Detalles de compra: Precio {detalles.get('precio', 0.0)} | "
                      f"Descuentos: {', '.join(detalles.get('descuentos_aplicados', [])) if detalles.get('descuentos_aplicados') else 'Ninguno'} | "
                      f"Servicios extra: {', '.join(detalles.get('servicios_extra', [])) if detalles.get('servicios_extra') else 'Ninguno'} | "
                      f"Metodo pago: {detalles.get('metodo_pago', 'N/A')}")
        else:
            print(f"INFO: No existe un ticket con ID: {ticket_id}")

    # ELIMINAR TICKET POR ID
    @staticmethod
    def eliminar(ticket_id):
        ticket = TicketModel.get_or_none(TicketModel.id == ticket_id)
        if ticket:
            ticket.delete_instance()
            print(f"INFO: El ticket ID: {ticket_id} ha sido eliminado.")
        else:
            print(f"INFO: No existe un ticket con ID: {ticket_id}")

    # MARCAR TICKET COMO USADO
    @staticmethod
    def ticket_usado(ticket_id):
        ticket = TicketModel.get_or_none(TicketModel.id == ticket_id)
        while True:
            if ticket:
                if ticket.usado:
                    print("INFO: El ticket ya esta usado.")
                    return
                else:
                    # Cambiamos las propiedades en memoria.
                    ticket.usado = True # Ticket usado = True
                    ticket.fecha_uso = datetime.now().replace(microsecond=0) # Cambiamos la fecha.
                    ticket.save() # Guardamos los cambios en la base de datos.

                    print(f"INFO: El Ticket con ID {ticket_id} ha sido marcado como usado.")
                    break
            else:
                print(f"ERROR: No existe un ticket con ID: {ticket_id}")
                return
    
    # TICKETS DE UN VISITANTE ESPECIFICO
    @staticmethod
    def obtener_por_visitante(visitante_id):
        visitante = VisitanteModel.get_or_none(VisitanteModel.id == visitante_id)
        if not visitante:
            print(f"INFO: No existe el visitante con ID: {visitante_id}")
            return False

        tickets = TicketModel.select().where(TicketModel.visitante == visitante)
        if tickets.exists():
            print(f"🧾 Tickets del visitante {visitante.nombre}:")
            for recorrerTickets in tickets:
                detalles = recorrerTickets.detalles_compra or {}
                atraccion_nombre = recorrerTickets.atraccion.nombre if recorrerTickets.atraccion else "Atraccion eliminada"
                print(
                    f"ID Ticket: {recorrerTickets.id} | "
                    f"Atraccion: {atraccion_nombre} | "
                    f"Tipo: {recorrerTickets.tipo_ticket} | "
                    f"Precio: {detalles.get('precio',0.0)} | "
                    f"Usado: {'Si' if recorrerTickets.usado else 'No'}"
                )
            return tickets
        else:
            print(f"INFO: El visitante {visitante.nombre} no tiene tickets registrados.")
            return False

    # TICKETS DE UNA ATRACCION ESPECIFICA
    @staticmethod
    def obtener_por_atraccion(atraccion_id):
        atraccion = AtraccionModel.get_or_none(AtraccionModel.id == atraccion_id)
        if not atraccion:
            print(f"ERROR: No existe la atraccion con ID: {atraccion_id}")
            return False

        tickets = TicketModel.select().where(TicketModel.atraccion == atraccion)
        if tickets.exists():
            print(f"🧾 Tickets vendidos para {atraccion.nombre}:")
            for recorrerTicket in tickets:
                detalles = recorrerTicket.detalles_compra or {}
                visitante_nombre = recorrerTicket.visitante.nombre if recorrerTicket.visitante else "Visitante eliminado"
                print(
                    f"ID Ticket: {recorrerTicket.id} | "
                    f"Visitante: {visitante_nombre} | "
                    f"Tipo: {recorrerTicket.tipo_ticket} | "
                    f"Precio: {detalles.get('precio',0.0)} | "
                    f"Usado: {'Si' if recorrerTicket.usado else 'No'}"
                )
            return tickets
        else:
            print(f"INFO: No se ha vendido ningun Ticket para la atraccion: {atraccion.nombre}.")
            return False

    # CAMBIAR EL PRECIO DE UN TICKET.
    @staticmethod
    def cambiar_precio(ticket_id, nuevo_precio):
        ticket = TicketModel.get_or_none(TicketModel.id == ticket_id)
        if not ticket:
            print(f"ERROR: No existe un ticket con ID: {ticket_id}")
            return
        
        # Cambiamos las propiedades en memoria.
        detalles = ticket.detalles_compra
        detalles["precio"] = nuevo_precio # Cambiamos el precio
        ticket.detalles_compra = detalles  # Guardamos los cambios en el modelo
        ticket.save() 
        print(f"El precio del ticket ID: {ticket_id} ha sido cambiado: {nuevo_precio}$")