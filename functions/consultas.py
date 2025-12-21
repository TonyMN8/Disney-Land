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

 
