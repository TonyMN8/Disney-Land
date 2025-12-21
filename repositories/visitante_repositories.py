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
        if visitantes:
            for recorrerVisitantes in visitantes:
                if recorrerVisitantes.preferencias:
                    preferencia = recorrerVisitantes.preferencias
                # Mostramos el visitante:
                print(
                    f"ID: {recorrerVisitantes.id}, "
                    f"Nombre: {recorrerVisitantes.nombre}, " 
                    f"Email: {recorrerVisitantes.email}, "
                    f"Altura: {recorrerVisitantes.altura} cm, "
                    f"Fecha de registro: {recorrerVisitantes.fecha_registro}, "
                    f"Tipo favorito: {preferencia.get('tipo_favorito')}, "
                    f"Restricciones: {preferencia.get('restricciones')}, "
                    f"Historial visitas: {preferencia.get('historial_visitas')}"
                    )
                
            return visitantes
        else:
            print("INFO: No hay ningun visitante registrado.")
            return 
   
    # OBTENER UN VISITANTE POR SU CORREO ELECTRONICO:
    @staticmethod
    def obtener_por_email(visitante_correo):
        visitantes = VisitanteModel.select().where(VisitanteModel.email == visitante_correo)
        if visitantes:
            for recorrerVisitantes in visitantes:
                if recorrerVisitantes.preferencias:
                    preferencia = recorrerVisitantes.preferencias
                # Mostramos el visitante:
                print(
                    f"ID: {recorrerVisitantes.id}, "
                    f"Nombre: {recorrerVisitantes.nombre}, " 
                    f"Email: {recorrerVisitantes.email}, "
                    f"Altura: {recorrerVisitantes.altura} cm, "
                    f"Fecha de registro: {recorrerVisitantes.fecha_registro}, "
                    f"Tipo favorito: {preferencia.get('tipo_favorito')}, "
                    f"Restricciones: {preferencia.get('restricciones')}, "
                    f"Historial visitas: {preferencia.get('historial_visitas')}"
                    )
        else:
            print(f"INFO: No existe ningun visitante registrado con el correo: {visitante_correo}")
            return

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

