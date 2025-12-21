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
        # Recorremos los visitantes para mostrarlos.
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
        # Retornamos los visitantes:
        return visitantes

    # OBTENER UN VISITANTE POR SU CORREO ELECTRÓNICO
    @staticmethod
    def obtener_por_email(visitante_correo):
        visitantes = VisitanteModel.select().where(VisitanteModel.email == visitante_correo)
        if not visitantes:
            print(f"ERROR: No existe ningun visitante registrado con ese correo: {visitante_correo}")
            return None
        # Recorremos al visitante.
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
        # Retornamos los visitantes:
        return visitantes

    # ELIMINAR UN VISITANTE POR SU ID:
    @staticmethod
    def eliminar(visitante_id):
        try:
            visitante = VisitanteModel.get(VisitanteModel.id == visitante_id)
            visitante.delete_instance()
            print(f"INFO: El visitante: {visitante.nombre} ha sido eliminado.")
        except Exception:
            print(f"INFO: El visitante con ID: {visitante_id} no ha sido encontrado.")

    # ANADIR UNA NUEVA VISITA AL HISTORIAL DEL VISITANTE
    @staticmethod
    def anadir_visita(visitante_id, fecha, atracciones_visitadas):

        # Buscamos al visitante por ID
        visitante = VisitanteModel.get_or_none(VisitanteModel.id == visitante_id)
        if not visitante:
            print(f"ERROR: No existe un visitante con ID {visitante_id}")
            return

        # Aseguramos que 'preferencias' sea un diccionario
        preferencias = visitante.preferencias
        if not preferencias:
            preferencias = {}

        # Si no existe el historial, lo creamos
        if "historial_visitas" not in preferencias:
            preferencias["historial_visitas"] = []

        # Creamos la nueva visita
        nueva_visita = {
            "fecha": fecha,
            "atracciones_visitadas": atracciones_visitadas
        }

        # Intentamos añadir la visita al historial
        try:
            preferencias["historial_visitas"].append(nueva_visita)
        except Exception:
            # Si falla, reiniciamos la lista y añadimos la visita
            preferencias["historial_visitas"] = [nueva_visita]

        # Guardamos los cambios
        visitante.preferencias = preferencias
        visitante.save()

        print("INFO: Se ha añadido correctamente la visita al historial del visitante.")



