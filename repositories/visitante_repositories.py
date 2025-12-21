# IMPORTACIONES.
# Modelos relacionados con otras clases:
from models.visitante_model import VisitanteModel
from models.tickets_model import TicketModel
# from models.tickets_model import TicketModel

class VisitanteRepository:
    
    # METODO CREAR VISITANTE:
    @staticmethod 
    def crear_visitante(nombre, email, altura, preferencias=None): # Preferencias puede ser none.
        if preferencias is None:
            preferencias = {
                "tipo_favorito": "",
                "restricciones": [],
                "historial_visitas": []
            }
        # Excepción por si falla a la hora de crear el visitante:
        try:
            visitante = VisitanteModel.create(
                nombre=nombre,
                email=email,
                altura=altura,
                preferencias=preferencias
            )
            print(f"INFO: Se ha creado el visitante: ({visitante.nombre}) con correo: {visitante.email}")
        except Exception as e:
            print(f"ERROR: No se ha podido crear el visitante: {e}")
    
    # OBTENER TODOS LOS VISITANTES:
    @staticmethod
    def obtener_todos():
        visitantes = VisitanteModel.select()
        if not visitantes:
            print("INFO: No hay visitantes registrados.")
            return
        
        for recorrerVisitantes in visitantes:
            pref = recorrerVisitantes.preferencias or {"tipo_favorito": "", "restricciones": [], "historial_visitas": []}
            print(f"ID: {recorrerVisitantes.id} | Nombre: {recorrerVisitantes.nombre} | Email: {recorrerVisitantes.email}")
            print(f"Altura: {recorrerVisitantes.altura} cm")
            print(f"Fecha registro: {recorrerVisitantes.fecha_registro} | Tipo favorito: {pref.get('tipo_favorito', '')}")
            print(f"Restricciones: {', '.join(pref.get('restricciones', [])) or 'Ninguna'}")
            
            historial = pref.get("historial_visitas", [])
            if historial:
                print("Historial visitas:")
                for recorrerHistorial in historial:
                    print(f"  {recorrerHistorial['fecha']} - {recorrerHistorial['atracciones_visitadas']} atracciones")
            else:
                print("Historial visitas: Ninguno")
            print("------------------------------")
        
        return visitantes

    # OBTENER UN VISITANTE POR SU CORREO ELECTRÓNICO
    @staticmethod
    def obtener_por_email(visitante_correo):
        visitantes = VisitanteModel.select().where(VisitanteModel.email == visitante_correo)
        if not visitantes:
            print(f"ERROR: No existe ningun visitante registrado con ese correo: {visitante_correo}")
            return None

        for recorrerVisitantes in visitantes:
            pref = recorrerVisitantes.preferencias or {"tipo_favorito": "", "restricciones": [], "historial_visitas": []}
            print(f"ID: {recorrerVisitantes.id} | Nombre: {recorrerVisitantes.nombre} | Email: {recorrerVisitantes.email}")
            print(f"Altura: {recorrerVisitantes.altura} cm")
            print(f"Fecha registro: {recorrerVisitantes.fecha_registro} | Tipo favorito: {pref.get('tipo_favorito', '')}")
            print(f"Restricciones: {', '.join(pref.get('restricciones', [])) or 'Ninguna'}")

            historial = pref.get("historial_visitas", [])
            if historial:
                print("Historial visitas:")
                for h in historial:
                    print(f"  {h['fecha']} - {h['atracciones_visitadas']} atracciones")
            else:
                print("Historial visitas: Ninguno")
            print("------------------------------")

        return visitantes

    # ELIMINAR UN VISITANTE POR SU ID:
    @staticmethod
    def eliminar(visitante_id):
        # Seleccionamos todos los visitantes
        visitantes = VisitanteModel.select().where(VisitanteModel.id == visitante_id)
        eliminado = False # Control si se elimina un visitante
        for recorrerVisitantes in visitantes:
            recorrerVisitantes.delete_instance() # Eliminamos el visitante y todos sus tickets asociados
            print(f"INFO: El visitante: {recorrerVisitantes.nombre} ha sido eliminado.")
            eliminado = True
        if not eliminado:
            print(f"INFO: El visitante con ID: {visitante_id} no ha sido encontrado.")

