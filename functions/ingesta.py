# INGESTA CREADA CON IA

import random
from datetime import date, datetime, timedelta
from repositories.visitante_repositories import VisitanteRepository
from repositories.atraccion_repositories import AtraccionRepository
from repositories.ticket_repositories import TicketRepository
from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel

def ingesta_masiva():
    # -----------------------------
    # 1️⃣ Generar 200 visitantes
    # -----------------------------
    tipos_favoritos = ["extrema", "familiar", "infantil", "acuatica"]
    restricciones_posibles = ["problemas_cardiacos", "embarazo", "miedo_altura", "ninguna"]

    for i in range(1, 201):
        nombre = f"Visitante_{i}"
        email = f"visitante{i}@parque.com"
        altura = random.randint(90, 200)  # altura entre 90 y 200 cm
        preferencias = {
            "tipo_favorito": random.choice(tipos_favoritos),
            "restricciones": random.sample(restricciones_posibles, k=random.randint(0, 2)),
            "historial_visitas": [
                {
                    "fecha": (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d"),
                    "atracciones_visitadas": random.randint(1, 15)
                } for _ in range(random.randint(0, 5))
            ]
        }
        VisitanteRepository.crear_visitante(nombre, email, altura, preferencias)

    # -----------------------------
    # 2️⃣ Generar 20 atracciones
    # -----------------------------
    tipos_atraccion = ["extrema", "familiar", "infantil", "acuatica"]
    caracteristicas_posibles = ["looping", "caida_libre", "giro_360", "tranquilo", "paisaje", "tobogán", "columpios", "agua", "oscuridad", "vuelo"]

    for i in range(1, 21):
        nombre = f"Atraccion_{i}"
        tipo = random.choice(tipos_atraccion)
        altura_minima = random.randint(80, 180)
        duracion = random.randint(30, 300)  # segundos
        capacidad = random.randint(10, 50)
        intensidad = random.randint(1, 10)
        caracteristicas = random.sample(caracteristicas_posibles, k=random.randint(1, 4))
        horarios = {
            "apertura": f"{random.randint(8, 11)}:00",
            "cierre": f"{random.randint(18, 23)}:00",
            "mantenimiento": [f"{random.randint(12, 16)}:00-{random.randint(12, 16)}:30"] if random.random() > 0.5 else []
        }
        detalles = {
            "duracion_segundos": duracion,
            "capacidad_por_turno": capacidad,
            "intensidad": intensidad,
            "caracteristicas": caracteristicas,
            "horarios": horarios
        }
        activa = random.choice([True, True, True, False])  # mayoría activas
        AtraccionRepository.crear_atraccion(nombre, tipo, altura_minima, detalles, activa)

    # -----------------------------
    # 3️⃣ Generar tickets aleatorios
    # -----------------------------
    visitantes = list(VisitanteModel.select())
    atracciones = list(AtraccionModel.select())
    tipos_ticket = ["general", "colegio", "empleado"]
    descuentos_posibles = ["estudiante", "early_bird", "ninguno"]
    servicios_posibles = ["fast_pass", "comida_incluida", "foto_recuerdo"]

    for visitante in visitantes:
        # Cada visitante puede tener entre 1 y 10 tickets
        for _ in range(random.randint(0, 4)):
            atraccion = random.choice(atracciones + [None])  # Algunos tickets generales
            fecha_visita = date.today() + timedelta(days=random.randint(0, 90))
            tipo_ticket = random.choice(tipos_ticket)
            detalles_compra = {
                "precio": round(random.uniform(0, 100), 2),
                "descuentos_aplicados": random.sample(descuentos_posibles, k=random.randint(0, 2)),
                "servicios_extra": random.sample(servicios_posibles, k=random.randint(0, 2)),
                "metodo_pago": random.choice(["efectivo", "tarjeta", "paypal"])
            }
            TicketRepository.crear_ticket(
                visitante=visitante,
                atraccion=atraccion,
                fecha_visita=fecha_visita,
                tipo_ticket=tipo_ticket,
                detalles_compra=detalles_compra,
                usado=random.choice([True, False])
            )

    print("✅ Ingesta masiva completada: 200 visitantes, 20 atracciones y tickets asociados.")