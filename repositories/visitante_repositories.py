from creacion_tablas import inicializar_base # type: ignore
from models.visitante_model import VisitanteModel
from repositories.visitante_repositories import VisitanteRepositorie
from datetime import datetime

# Inicializar las tablas (solo la primera vez o si quieres reiniciar)
# Cambia reiniciar=False si no quieres borrar los datos existentes
inicializar_base([VisitanteModel], reiniciar=False)

# Ejemplo 1: Crear un visitante simple
visitante1 = VisitanteRepositorie.crear_visitante(
    nombre="Juan Pérez",
    email="juan.perez@example.com",
    altura=175
)

if visitante1:
    print(f"Visitante creado: {visitante1.nombre} (ID: {visitante1.id})")

# Ejemplo 2: Crear un visitante con preferencias personalizadas
visitante2 = VisitanteRepositorie.crear_visitante(
    nombre="María García",
    email="maria.garcia@example.com",
    altura=160,
    preferencias={
        "tipo_favorito": "Montaña rusa",
        "restricciones": ["altura_minima"],
        "historial_visitas": [
            {
                "fecha": "2024-01-15",
                "atracciones_visitadas": ["Roller Coaster", "Casa del Terror"]
            }
        ]
    }
)

if visitante2:
    print(f"✓ Visitante creado: {visitante2.nombre} (ID: {visitante2.id})")

# Ejemplo 3: Consultar un visitante
visitante_consultado = VisitanteRepositorie.obtener_visitante_por_email("juan.perez@example.com")
if visitante_consultado:
    print(f"\n--- Información del visitante ---")
    print(f"Nombre: {visitante_consultado.nombre}")
    print(f"Email: {visitante_consultado.email}")
    print(f"Altura: {visitante_consultado.altura} cm")
    print(f"Fecha registro: {visitante_consultado.fecha_registro}")
    print(f"Preferencias: {visitante_consultado.preferencias}")

# Ejemplo 4: Listar todos los visitantes
print("\n--- Todos los visitantes ---")
todos = VisitanteRepositorie.obtener_todos_visitantes()
for v in todos:
    print(f"- {v.nombre} ({v.email})")