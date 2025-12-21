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
    @staticmethod
    def obtener_todos():
        atraccion = AtraccionModel.select()
        if atraccion:
            for recorrerAtraccion in atraccion:
                detalles_atraccion = recorrerAtraccion.detalles
                horarios = detalles_atraccion.get("horarios", {})
                caracteristicas = detalles_atraccion.get('caracteristicas', [])

                # Nombre, tipo y altura:
                print("───────────────────────────────────────────────────────────────────────────────")
                print(  f"🎡 ATRACCIÓN ID: {recorrerAtraccion.id} | "
                        f"Nombre: {recorrerAtraccion.nombre} | "
                        f"Tipo: {recorrerAtraccion.tipo} | "
                        f"Altura mínima: {recorrerAtraccion.altura_minima} cm")
                
                # Detalles
                print(f"(-) Duración: {detalles_atraccion.get('duracion_segundos', 0)} seg | "
                      f"Capacidad por turno: {detalles_atraccion.get('capacidad_por_turno', 0)} | "
                      f"Intensidad: {detalles_atraccion.get('intensidad', 0)} | "
                      f"Caracteristicas: {', '.join(caracteristicas) if caracteristicas else 'Ninguna'}"
                    )
                # Horarios
                print("  - Horarios:")
                print(f"      Apertura: {horarios.get('apertura', 'N/A')}")
                print(f"      Cierre: {horarios.get('cierre', 'N/A')}")
                mantenimiento = horarios.get('mantenimiento', [])
                print(f"      Mantenimiento: {', '.join(mantenimiento) if mantenimiento else 'Ninguno'}")
                
                # Estado y fecha
                print(f"(-) Estado: {'Activa' if recorrerAtraccion.activa else 'Inactiva'}")
                print(f"(-) Fecha de inauguración: {recorrerAtraccion.fecha_inauguracion}")
                print("───────────────────────────────────────────────────────────────\n")
  
        else:
            print("INFO: No hay ninguna atraccion registrada.")
            return False # Retorno False en caso de que no haya atracciones.

    # OBTENER ATRACCION POR NOMBRE:
    def obtener_por_nombre(nombre):
        # Obtenemos el nombre mediante el modelo atraccion:
        atraccion = AtraccionModel.get_or_none(AtraccionModel.nombre == nombre)
        if atraccion:
                detalles_atraccion = atraccion.detalles
                horarios = detalles_atraccion.get("horarios", {})
                caracteristicas = detalles_atraccion.get('caracteristicas', [])

                # Nombre, tipo y altura:
                print("───────────────────────────────────────────────────────────────────────────────")
                print(  f"🎡 ATRACCIÓN ID: {atraccion.id} | "
                        f"Nombre: {atraccion.nombre} | "
                        f"Tipo: {atraccion.tipo} | "
                        f"Altura mínima: {atraccion.altura_minima} cm")
                
                # Detalles
                print(f"(-) Duración: {detalles_atraccion.get('duracion_segundos', 0)} seg | "
                      f"Capacidad por turno: {detalles_atraccion.get('capacidad_por_turno', 0)} | "
                      f"Intensidad: {detalles_atraccion.get('intensidad', 0)} | "
                      f"Caracteristicas: {', '.join(caracteristicas) if caracteristicas else 'Ninguna'}"
                    )
                # Horarios
                print("  - Horarios:")
                print(f"      Apertura: {horarios.get('apertura', 'N/A')}")
                print(f"      Cierre: {horarios.get('cierre', 'N/A')}")
                mantenimiento = horarios.get('mantenimiento', [])
                print(f"      Mantenimiento: {', '.join(mantenimiento) if mantenimiento else 'Ninguno'}")
                
                # Estado y fecha
                print(f"(-) Estado: {'Activa' if atraccion.activa else 'Inactiva'}")
                print(f"(-) Fecha de inauguración: {atraccion.fecha_inauguracion}")
                print("───────────────────────────────────────────────────────────────\n")

        else:
            print("INFO: No hay ninguna atraccion registrada.")
            return
        
    # ELIMINAR UNA ATRACCION POR SU NOMBRE:
    @staticmethod
    def eliminar(nombre):
        atraccion = AtraccionModel.get_or_none(AtraccionModel.nombre == nombre)
        if atraccion:
            atraccion.delete_instance()
            print(f"INFO: La atraccion: {atraccion.nombre} ha sido eliminada.")
        else:
            print(f"INFO: La atraccion con nombre: {nombre} no existe.")

    # CAMBIAR EL ESTADO DE LA ATRACCION
    @staticmethod
    def cambiar_estado(nombre):
        # Buscamos la atracción por nombre en la base de datos
        atraccion = AtraccionModel.get_or_none(AtraccionModel.nombre == nombre)
        
        if atraccion:
            atraccion.activa = not atraccion.activa # Invertimos el valor.
            atraccion.save()  # Guardamos en la base de datos.
            
            if atraccion.activa:
                print(f"INFO: La atraccion: {nombre} ha sido activada")
            else:
                print(f"INFO: La atraccion: {nombre} se encuentra desactivada o inactiva.")
        
        else:
            print(f"ERROR: No se encontro ninguna atraccion con el nombre: {nombre}")