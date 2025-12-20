# IMPORTACIONES.
# Modelos relacionados con otras clases:
from models.atraccion_model import AtraccionModel

class AtraccionRepository:
    
    @staticmethod
    # METODO CREAR ATRACCION:
    def crear_atraccion(nombre, tipo, altura_minima, detalles, activa):
        # Excepción por si falla a la hora de crear el visitante:
        try:
            atraccion = AtraccionModel.create(
                nombre=nombre,
                tipo=tipo,
                altura_minima=altura_minima,
                detalles=detalles,
                activa=activa
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
                # Línea principal: ID, Nombre, Tipo, Altura
                print(
                    f"_____________________________________________________________________________________________"
                    f"🎡 ID: {recorrerAtraccion.id} | "
                    f"Nombre: {recorrerAtraccion.nombre} | "
                    f"Tipo: {recorrerAtraccion.tipo} | "
                    f"Altura mínima: {recorrerAtraccion.altura_minima} cm"
                )
                # Línea de detalles: Duración, Capacidad, Intensidad, Características, Horarios, Activa, Fecha
                print(f"Duración: {detalles_atraccion.get('duracion_segundos', 'N/A')} seg | "
                    f"Capacidad: {detalles_atraccion.get('capacidad_por_turno', 'N/A')} por turno | "
                    f"Intensidad: {detalles_atraccion.get('intensidad', 'N/A')} | "
                    f"Características: {detalles_atraccion.get('caracteristicas', 'N/A')} | "
                    f"Horarios: {detalles_atraccion.get('horarios', {})}"
                )

                 # Línea de detalles: Duración, Capacidad, Intensidad, Características, Horarios, Activa, Fecha
                print(f"Activa: {recorrerAtraccion.activa} | "
                    f"Fecha de inauguración: {recorrerAtraccion.fecha_inauguracion}"
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
        
    # ELIMINAR UNA ATRACCION POR SU NOMBRE:
    @staticmethod
    def eliminar(nombre):
        atraccion = AtraccionModel.get_or_none(AtraccionModel.nombre == nombre)
        eliminado = False
        for recorrerAtraccion in atraccion:
            recorrerAtraccion.delete_instance()
            print(f"INFO: La atraccion: {recorrerAtraccion.nombre} ha sido eliminada.")
            eliminado = True
        if not eliminado:
            print(f"INFO: La atraccion con nombre: {nombre} no existe.")