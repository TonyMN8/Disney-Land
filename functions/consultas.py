# IMPORTACIONES.
# repositorios y modelos relacionados:
from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel
from models.tickets_model import TicketModel
from peewee import fn

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

    # ATRACCIONES CON LOOPING Y CAIDA LIBRE
    @staticmethod
    def atracciones_caracteristicas():
        print("🧾 CONSULTA: Atracciones con 'looping' y 'caida_libre'")
        atracciones = AtraccionModel.select()
        atraccion_existente = False
        for recorrerAtracciones in atracciones:
            caracteristicas = recorrerAtracciones.detalles.get("caracteristicas", [])
            if "looping" in caracteristicas and "caida_libre" in caracteristicas:
                print(f"ID: {recorrerAtracciones.id} | Nombre: {recorrerAtracciones.nombre} | Caracteristicas: {', '.join(caracteristicas)}")
                atraccion_existente = True
        if not atraccion_existente:
            print("INFO: No hay atracciones con looping y caida libre")

    # TICKETS CON DESCUENTO "ESTUDIANTE"
    @staticmethod
    def tickets_descuento():
        print("🧾 CONSULTA: Tickets con descuento 'estudiante'")
        tickets = TicketModel.select()
        ticket_existente = False
        for recorrerTickets in tickets:
            descuentos = recorrerTickets.detalles_compra.get("descuentos_aplicados", [])
            if "estudiante" in descuentos:
                print(f"ID: {recorrerTickets.id} | Visitante: {recorrerTickets.visitante.nombre} | Precio: {recorrerTickets.detalles_compra.get('precio')}")
                ticket_existente = True
        if not ticket_existente:
            print("INFO: No hay tickets con descuento estudiante")

    # ATRACCIONES CON AL MENOS UN HORARIO DE MANTENIMIENTO
    @staticmethod
    def atracciones_mantenimiento():
        print("🧾 CONSULTA: Atracciones con al menos un horario de mantenimiento")
        atracciones = AtraccionModel.select()
        atraccion_existente = False
        for recorrerAtracciones in atracciones:
            mantenimiento = recorrerAtracciones.detalles.get("horarios", {}).get("mantenimiento", [])
            if len(mantenimiento) > 0:
                print(f"ID: {recorrerAtracciones.id} | Nombre: {recorrerAtracciones.nombre} | Mantenimiento: {', '.join(mantenimiento)}")
                atraccion_existente = True
        if not atraccion_existente:
            print("INFO: No hay atracciones con mantenimiento programado")

    # VISITANTES ORDENADORES POR CANTIDAD DE TICKETS
    @staticmethod
    def visitantes_por_tickets():
        print("🧾 CONSULTA: Visitantes ordenados por cantidad de tickets comprados")

        consulta = (VisitanteModel.select (VisitanteModel, fn.COUNT(TicketModel.id).alias("total_tickets"))
            .join(TicketModel)
            .group_by(VisitanteModel.id)
            .order_by(fn.COUNT(TicketModel.id).desc())
        )

        if not consulta:
            print("INFO: No hay visitantes con tickets")
            return

        for recorrerConsulta in consulta:
            print(
                f"ID: {recorrerConsulta.id} | "
                f"Nombre: {recorrerConsulta.nombre} | "
                f"Tickets comprados: {recorrerConsulta.total_tickets}"
            )

    # LAS 5 ATRACCIONES MAS VENDIDAS
    @staticmethod
    def atracciones_vendidas():
        print("🧾 CONSULTA: 5 Atracciones mas vendidas")

        consulta = (
            AtraccionModel.select(AtraccionModel, fn.COUNT(TicketModel.id).alias("total_tickets"))
            .join(TicketModel)
            .where(TicketModel.atraccion.is_null(False))
            .group_by(AtraccionModel.id)
            .order_by(fn.COUNT(TicketModel.id).desc()).limit(5)
        )

        if not consulta:
            print("INFO: No hay tickets vendidos para atracciones")
            return

        for recorrerConsulta in consulta:
            print(
                f"ID: {recorrerConsulta.id} | "
                f"Nombre: {recorrerConsulta.nombre} | "
                f"Tickets vendidos: {recorrerConsulta.total_tickets}"
            )

     # VISITANTES QUE HAN GASTADO MAS DE 100 EUROS
    @staticmethod
    def visitantes_mas_gastado():
        print("🧾 CONSULTA: Visitantes que han gastado mas de 100 euros")

        visitantes = VisitanteModel.select()
        visitante_existente = False

        for recorrerVisitantes in visitantes:
            total_gastado = 0

            # Recorremos los tickets del visitante
            for recorrerTickets in recorrerVisitantes.tickets:
                precio = recorrerTickets.detalles_compra.get("precio", 0)
                total_gastado += precio

            if total_gastado > 100:
                print(
                    f"ID: {recorrerVisitantes.id} | "
                    f"Nombre: {recorrerVisitantes.nombre} | "
                    f"Gastado: {total_gastado}€"
                )
                visitante_existente = True

        if not visitante_existente:
            print("INFO: No hay ningun visitante que supere los 100€ de gastos.")

    # ATRACCIONES COMPATIBLES
    @staticmethod
    def atracciones_compatibles():
        print("🧾 CONSULTA: Atracciones compatibles para un visitante")

        # Obtenemos todos los visitantes
        visitantes = VisitanteModel.select()
        if not visitantes:
            print("INFO: No hay visitantes registrados")
            return

        # Mostramos todos los visitantes para que el usuario seleccione
        for visitante in visitantes:
            print(f"ID: {visitante.id} | Nombre: {visitante.nombre}")

        # Pedimos el ID del visitante
        try:
            visitante_id = int(input("Introduce el ID del visitante: "))
        except ValueError:
            print("ERROR: Introduce un número válido.")
            return

        # Buscamos al visitante
        visitante = VisitanteModel.get_or_none(VisitanteModel.id == visitante_id)
        if not visitante:
            print("ERROR: Visitante no encontrado")
            return

        tipo_favorito = visitante.preferencias.get("tipo_favorito")
        altura_visitante = visitante.altura

        # Obtenemos todas las atracciones activas
        atracciones = AtraccionModel.select().where(AtraccionModel.activa == True)
        atraccion_existente = False

        for atraccion in atracciones:
            # Comprobamos tipo y altura
            if atraccion.tipo == tipo_favorito and altura_visitante >= atraccion.altura_minima:
                print(
                    f"ID: {atraccion.id} | "
                    f"Nombre: {atraccion.nombre} | "
                    f"Tipo: {atraccion.tipo} | "
                    f"Altura minima: {atraccion.altura_minima} cm"
                )
                atraccion_existente = True

        if not atraccion_existente:
            print("INFO: No hay atracciones compatibles para este visitante")

