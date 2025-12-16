# IMPORTACIONES.
# Modelos relacionados con otras clases:
from models.visitante_model import VisitanteModel
from models.tickets_model import TicketModel
# Dependencias
from peewee import * # type: ignore
from datetime import date
''' Extensiones y utilidades adicionales para trabajar con JSON: '''
from playhouse.postgres_ext import BinaryJSONField # type: ignore

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

        try:
            visitante = VisitanteModel.create(
                nombre=nombre,
                email=email,
                altura=altura,
                preferencias=preferencias
            )
            print(f"INFO: Visitante creado: {visitante.nombre}")
        except Exception as e:
            print(f"ERROR: No se ha podido crear el visitante: {e}")

    # OBTENER TODOS LOS VISITANTES:
    @staticmethod
    def obtener_todos():
        visitantes = VisitanteModel.select()
        if visitantes:
            for recorrerVisitantes in visitantes:
                print(f"ID: {recorrerVisitantes.id} - Nombre: {recorrerVisitantes.nombre} - Email: {recorrerVisitantes.email}")
        else:
            print("No hay visitantes registrados.")
   
    # OBTENER UN VISITANTE POR SU CORREO ELECTRONICO:
    @staticmethod
    def obtener_por_id(visitante_correo):
        visitantes = VisitanteModel.select().where(VisitanteModel.email == visitante_correo)
        encontrado = False
        for recorrerVisitantes in visitantes:
            print(f"Visitante encontrado: {recorrerVisitantes.nombre} - Email: {recorrerVisitantes.email}")
            encontrado = True
        if not encontrado:
            print(f"INFO: No existe ningun visitante registrado con el correo: {visitante_correo}")

    # ELIMINAR UN VISITANTE POR SU ID:
    @staticmethod
    def eliminar(visitante_id):
        visitantes = VisitanteModel.select().where(VisitanteModel.id == visitante_id)
        eliminado = False
        for recorrerVisitantes in visitantes:
            recorrerVisitantes.delete_instance()
            print(f"INFO: El visitante: {recorrerVisitantes.nombre} ha sido eliminado.")
            eliminado = True
        if not eliminado:
            print(f"INFO: El visitante con ID: {visitante_id} no ha sido encontrado.")