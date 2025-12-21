# IMPORTACIONES.
# repositorios y modelos relacionados:
from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel
from models.tickets_model import TicketModel

# Clase Consultas
class Consultas:
    # VISITANTES CON PREFERENCIA POR ATRACCIONES "EXTREMAS"
    @staticmethod
    def preferencia_extrema():
        print("🧾 CONSULTA: Visitantes con preferencia por atracciones extremas")
        visitantes = VisitanteModel.select()
        visitante_existente = False

        for recorrerVisitantes in visitantes:
            if recorrerVisitantes.preferencias.get("tipo_favorito") == "extrema":
                print(f"ID: {recorrerVisitantes.id} | Nombre: {recorrerVisitantes.nombre} | Email: {recorrerVisitantes.email} | Altura: {recorrerVisitantes.altura} cm")
                visitante_existente = True
        if not visitante_existente:
            print("INFO: No hay visitantes con preferencia extrema")

    # ATRACCIONES CON INTENSIDAD > 7
    @staticmethod
    def atracciones_intensidad():
        print("🧾 CONSULTA: Atracciones con intensidad mayor a 7")
        atracciones = AtraccionModel.select()
        atraccion_existente = False
        for recorrerAtracciones in atracciones:
            intensidad = recorrerAtracciones.detalles.get("intensidad", 0)
            if intensidad > 7:
                print(f"ID: {recorrerAtracciones.id} | Nombre: {recorrerAtracciones.nombre} | Intensidad: {intensidad}")
                atraccion_existente = True
        if not atraccion_existente:
            print("INFO: No hay atracciones con intensidad mayor a 7")

    # TICKETS DE COLEGIO CON PRECIO MENOR A 30
    @staticmethod
    def tickets_colegio():
        print("🧾 CONSULTA: Tickets tipo colegio con precio menor a 30")
        tickets = TicketModel.select()
        ticket_existente = False
        for recorrerTickets in tickets:
            precio = recorrerTickets.detalles_compra.get("precio", 0)
            if recorrerTickets.tipo_ticket == "colegio" and precio < 30:
                print(f"ID: {recorrerTickets.id} | Visitante: {recorrerTickets.visitante.nombre} | Precio: {precio}")
                ticket_existente = True
        if not ticket_existente:
            print("INFO: No hay tickets tipo colegio con precio menor a 30")

    # ATRACCIONES CON DURACION MAYOR A 120 SEGUNDOS
    @staticmethod
    def atracciones_duracion():
        print("🧾 CONSULTA: Atracciones con duracion mayor a 120 segundos")
        atracciones = AtraccionModel.select()
        atraccion_existente = False
        for recorrerAtracciones in atracciones:
            duracion = recorrerAtracciones.detalles.get("duracion_segundos", 0)
            if duracion > 120:
                print(f"ID: {recorrerAtracciones.id} | Nombre: {recorrerAtracciones.nombre} | Duracion: {duracion} seg")
                atraccion_existente = True
        if not atraccion_existente:
            print("INFO: No hay atracciones con duracion mayor a 120 seg")

