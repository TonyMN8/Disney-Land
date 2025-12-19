# IMPORTACIONES.
# Modelos relacionados con otras clases:
from models.atraccion_model import AtraccionModel

class AtraccionRepository:
    
    @staticmethod
    # METODO CREAR ATRACCION:
    def crear_atraccion(nombre, tipo, altura_minima, detalles):
        # Excepción por si falla a la hora de crear el visitante:
        try:
            atraccion = AtraccionModel.create(
                nombre=nombre,
                tipo=tipo,
                altura_minima=altura_minima,
                detalles=detalles
            )
            print(f"Se ha creado la atraccion ({atraccion.nombre}) de tipo: {atraccion.tipo}")
        except Exception as e:
            print(f"No se ha podido crear la atraccion:", e)



    # OBTENER TODAS LAS ATRACCIONES:
    def obtener_todos():
        atraccion = AtraccionModel.select()
        if atraccion:
            for recorrerAtraccion in atraccion:
                if recorrerAtraccion.detalles:
                    detalles_atraccion = recorrerAtraccion.detalles

                # Mostramos la atraccion:
                print(
                    f"ID: {recorrerAtraccion.id}, "
                    f"Nombre: {recorrerAtraccion.nombre}, "
                    f"Tipo: {recorrerAtraccion.tipo}, "
                    f"Altura minima: {recorrerAtraccion.altura_minima} cm, "
                    f"Duracion: {detalles_atraccion.get("duracion_segundos")}, "
                    f"Capacidad por Turno: {detalles_atraccion.get("capacidad_por_turno")}, "
                    f"Intensidad: {detalles_atraccion.get("intensidad")}, "
                    f"Caracteristicas: {detalles_atraccion.get("caracteristicas")}, "
                    f"Horarios: {detalles_atraccion.get("horarios")}, "
                    f"Activa: {recorrerAtraccion.activa}, "
                    f"Fecha de inaguracion: {recorrerAtraccion.fecha_inauguracion}"
                )
        else:
            print("INFO: No hay ninguna atraccion registrada.")
            return
        
    # OBTENER ATRACCION POR NOMBRE:
    def obtener_por_nombre(nombre):
        # Obtenemos el nombre mediante el modelo atraccion:
        atraccion = AtraccionModel.get_or_none(AtraccionModel.nombre == nombre)

        if atraccion:
            print(
                f"ID: {atraccion.id}, "
                f"Nombre: {atraccion.nombre}, "
                f"Tipo: {atraccion.tipo}, "
                f"Altura minima: {atraccion.altura_minima} cm, "
                f"Duracion: {atraccion.detalles.get("duracion_segundos")}, "
                f"Capacidad por Turno: {atraccion.detalles.get("capacidad_por_turno")}, "
                f"Intensidad: {atraccion.detalles.get("intensidad")}, "
                f"Caracteristicas: {atraccion.detalles.get("caracteristicas")}, "
                f"Horarios: {atraccion.detalles.get("horarios")}, "
                f"Activa: {atraccion.activa}, "
                f"Fecha de inaguracion: {atraccion.fecha_inauguracion}"
            )

        else:
            print(f"INFO: No hay ninguna atraccion registrada con el nombre {atraccion.nombre}.")
            return