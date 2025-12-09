from models.atraccion_model import AtraccionModel
from peewee import *
from playhouse.postgres_ext import *

class AtraccionRepositorie:
    
    @staticmethod
    def crear_atraccion(nombre, tipo, altura_minima, detalles=None):
        """Crear una nueva atracción"""
        try:
            atraccion = AtraccionModel.create(
                nombre=nombre,
                tipo=tipo,
                altura_minima=altura_minima,
                detalles=detalles or {}
            )
            return atraccion
        except Exception as e:
            print(f"Error al crear atracción: {e}")
            return None
    
    @staticmethod
    def obtener_todas_atracciones():
        """Obtener todas las atracciones"""
        try:
            return list(AtraccionModel.select())
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    @staticmethod
    def obtener_atracciones_activas():
        """Obtener atracciones activas"""
        try:
            return list(AtraccionModel.select().where(AtraccionModel.activa == True))
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    @staticmethod
    def obtener_atraccion_por_id(atraccion_id):
        """Obtener una atracción por ID"""
        try:
            return AtraccionModel.get_by_id(atraccion_id)
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    @staticmethod
    def cambiar_estado_atraccion(atraccion_id, activa):
        """Cambiar el estado activo/inactivo de una atracción"""
        try:
            atraccion = AtraccionModel.get_by_id(atraccion_id)
            atraccion.activa = activa
            atraccion.save()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    @staticmethod
    def eliminar_atraccion(atraccion_id):
        """Eliminar una atracción"""
        try:
            atraccion = AtraccionModel.get_by_id(atraccion_id)
            atraccion.delete_instance()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    @staticmethod
    def atracciones_intensidad_mayor(intensidad):
        """Atracciones con intensidad mayor a X"""
        try:
            return list(AtraccionModel.select().where(
                AtraccionModel.detalles['intensidad'].cast('int') > intensidad
            ))
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    @staticmethod
    def atracciones_duracion_mayor(segundos):
        """Atracciones con duración mayor a X segundos"""
        try:
            return list(AtraccionModel.select().where(
                AtraccionModel.detalles['duracion_segundos'].cast('int') > segundos
            ))
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    @staticmethod
    def atracciones_con_caracteristicas(caracteristicas):
        """Atracciones que tengan todas las características especificadas"""
        try:
            query = AtraccionModel.select()
            for caracteristica in caracteristicas:
                query = query.where(
                    AtraccionModel.detalles['caracteristicas'].cast('text').contains(caracteristica)
                )
            return list(query)
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    @staticmethod
    def atracciones_con_mantenimiento():
        """Atracciones con al menos un horario de mantenimiento"""
        try:
            return list(AtraccionModel.select().where(
                AtraccionModel.detalles['horarios']['mantenimiento'].exists()
            ))
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    @staticmethod
    def agregar_caracteristica(atraccion_id, caracteristica):
        """Añadir una nueva característica al array de características"""
        try:
            atraccion = AtraccionModel.get_by_id(atraccion_id)
            detalles = atraccion.detalles or {}
            caracteristicas = detalles.get('caracteristicas', [])
            
            if caracteristica not in caracteristicas:
                caracteristicas.append(caracteristica)
                detalles['caracteristicas'] = caracteristicas
                atraccion.detalles = detalles
                atraccion.save()
                return True
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    @staticmethod
    def atracciones_mas_vendidas(limite=5):
        """Obtener las X atracciones más vendidas"""
        try:
            from models.ticket_model import TicketModel
            
            return list(
                AtraccionModel
                .select(AtraccionModel, fn.COUNT(TicketModel.id).alias('total_tickets'))
                .join(TicketModel, JOIN.LEFT_OUTER)
                .where(TicketModel.atraccion.is_null(False))
                .group_by(AtraccionModel)
                .order_by(fn.COUNT(TicketModel.id).desc())
                .limit(limite)
            )
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    @staticmethod
    def atracciones_compatibles_visitante(visitante_id):
        """Atracciones compatibles para un visitante"""
        try:
            from models.visitante_model import VisitanteModel
            
            visitante = VisitanteModel.get_by_id(visitante_id)
            tipo_favorito = visitante.preferencias.get('tipo_favorito', '')
            
            query = AtraccionModel.select().where(
                (AtraccionModel.activa == True) &
                (AtraccionModel.altura_minima <= visitante.altura)
            )
            
            if tipo_favorito:
                query = query.where(AtraccionModel.tipo == tipo_favorito)
            
            return list(query)
        except Exception as e:
            print(f"Error: {e}")
            return []