from database import conectar_db, cerrar_db
from crear_tablas import crear_tablas
from menu.funciones import *

def mostrar_menu_principal():
    """Mostrar menú principal"""
    print("\n" + "="*50)
    print("  SISTEMA DE GESTIÓN - PARQUE DE ATRACCIONES")
    print("="*50)
    print("\n--- GESTIÓN DE VISITANTES ---")
    print("1. Crear visitante")
    print("2. Listar visitantes")
    print("3. Eliminar visitante")
    print("\n--- GESTIÓN DE ATRACCIONES ---")
    print("4. Crear atracción")
    print("5. Listar atracciones")
    print("6. Cambiar estado atracción")
    print("7. Eliminar atracción")
    print("\n--- GESTIÓN DE TICKETS ---")
    print("8. Crear ticket")
    print("9. Listar tickets")
    print("10. Marcar ticket como usado")
    print("11. Listar tickets de un visitante")
    print("12. Listar tickets de una atracción")
    print("13. Visitantes con ticket para atracción")
    print("\n--- CONSULTAS Y REPORTES ---")
    print("14. Consultas especializadas")
    print("15. Modificaciones JSONB")
    print("\n--- SISTEMA ---")
    print("0. Salir")
    print("="*50)

def main():
    """Función principal"""
    print("\n¡Bienvenido al Sistema de Gestión del Parque de Atracciones!")
    
    # Conectar a la base de datos
    if not conectar_db():
        print("No se pudo conectar a la base de datos. Saliendo...")
        return
    
    # Crear tablas si no existen
    print("\nVerificando tablas...")
    crear_tablas()
    
    while True:
        try:
            mostrar_menu_principal()
            opcion = validar_entero(None, "\nSeleccione una opción: ")
            
            if opcion == 0:
                print("\n¡Gracias por usar el sistema! Hasta pronto.")
                break
            
            elif opcion == 1:
                crear_visitante_menu()
            
            elif opcion == 2:
                listar_visitantes()
            
            elif opcion == 3:
                eliminar_visitante_menu()
            
            elif opcion == 4:
                crear_atraccion_menu()
            
            elif opcion == 5:
                listar_atracciones()
            
            elif opcion == 6:
                cambiar_estado_atraccion_menu()
            
            elif opcion == 7:
                eliminar_atraccion_menu()
            
            elif opcion == 8:
                crear_ticket_menu()
            
            elif opcion == 9:
                listar_tickets()
            
            elif opcion == 10:
                marcar_ticket_usado_menu()
            
            elif opcion == 11:
                visitante_id = validar_entero(None, "ID del visitante: ")
                tickets = TicketRepositorie.obtener_tickets_visitante(visitante_id)
                print(f"\nTickets del visitante (Total: {len(tickets)}):")
                for t in tickets:
                    atraccion = 'General' if t.atraccion is None else t.atraccion.nombre
                    print(f"- Ticket {t.id}: {atraccion} - {t.fecha_visita}")
            
            elif opcion == 12:
                atraccion_id = validar_entero(None, "ID de la atracción: ")
                tickets = TicketRepositorie.obtener_tickets_atraccion(atraccion_id)
                print(f"\nTickets de la atracción (Total: {len(tickets)}):")
                for t in tickets:
                    print(f"- Ticket {t.id}: Visitante {t.visitante.nombre} - {t.fecha_visita}")
            
            elif opcion == 13:
                atraccion_id = validar_entero(None, "ID de la atracción: ")
                visitantes = TicketRepositorie.obtener_visitantes_con_ticket_atraccion(atraccion_id)
                print(f"\nVisitantes con ticket (Total: {len(visitantes)}):")
                for v in visitantes:
                    print(f"- {v.nombre} ({v.email})")
            
            elif opcion == 14:
                consultas_menu()
            
            elif opcion == 15:
                modificaciones_jsonb_menu()
            
            else:
                print("\n✗ Opción no válida. Intente de nuevo.")
            
            input("\nPresione Enter para continuar...")
        
        except KeyboardInterrupt:
            print("\n\n¡Operación cancelada por el usuario!")
            break
        except Exception as e:
            print(f"\n✗ Error inesperado: {e}")
            input("\nPresione Enter para continuar...")
    
    # Cerrar conexión
    cerrar_db()

if __name__ == "__main__":
    main()