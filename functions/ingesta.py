import random
from datetime import datetime, timedelta, date
from repositories.visitante_repositories import VisitanteRepository
from repositories.atraccion_repositories import AtraccionRepository
from repositories.ticket_repositories import TicketRepository
from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel

def ingesta_masiva():
    # -----------------------------
    # 1️⃣ Generar 200 visitantes
    # -----------------------------
    nombres = ["Mateo", "Sofía", "Lucas", "Valeria", "Martín", "Emma", "Hugo", "Lucía",
               "Daniel", "Julia", "Martina", "Leo", "Alejandro", "Camila", "Pablo", "Valentina",
               "Diego", "Gabriela", "Gonzalo", "Mía", "Antonio", "María", "Manuel", "Carlos",
               "Laura", "Elena", "Adrián", "Clara", "Raúl", "Daniela", "Rubén", "Paula", "David",
               "Sara", "Mario", "Carla", "Javier", "Andrea", "Óscar", "Natalia", "Luis", "Irene",
               "Miguel", "Alba", "Ramiro", "Iker", "Matea", "Noah", "Oliver", "Amelia", "Isabella"]
    apellidos = ["García", "Martínez", "Rodríguez", "López", "Sánchez", "Pérez", "Gómez",
                 "Fernández", "Díaz", "Moreno", "Alonso", "Romero", "Torres", "Ruiz", "Ramírez",
                 "Vargas", "Ortiz", "Castillo"]
    tipos_favoritos = ["extrema", "familiar", "infantil", "acuatica"]
    restricciones_posibles = ["problemas_cardiacos", "embarazo", "miedo_altura", "ninguna"]

    for _ in range(200):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        nombre_completo = f"{nombre} {apellido}"
        email = f"{nombre.lower()}.{apellido.lower()}{random.randint(1,9999)}@mail.com"
        altura = random.randint(90, 200)
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
        VisitanteRepository.crear_visitante(nombre_completo, email, altura, preferencias)

    # -----------------------------
    # 2️⃣ Generar 30 atracciones con nombres reales
    # -----------------------------
    nombres_atracciones = [
        "Shambhala", "Red Force", "Batman Gotham City Escape", "Dragon Khan", "Furius Baco",
        "Hurakan Condor", "Stampida", "Sea Odyssey", "Silver Star", "Tibidabo Express",
        "Montaña Rusa", "Superman el Último Escape", "Blue Fire", "Kingda Ka", "Top Thrill Dragster",
        "The Smiler", "Nemesis", "Oblivion", "Expedition GeForce", "Black Mamba",
        "Intimidator 305", "Magnum XL-200", "Goliath", "El Toro", "Bizarro", "Leviathan",
        "Hydra the Revenge", "Steel Vengeance", "Maverick", "Twisted Colossus"
    ]

    tipos_atraccion = ["extrema", "familiar", "infantil", "acuatica"]
    caracteristicas_posibles = ["looping", "caida_libre", "giro_360", "tranquilo", "paisaje",
                                "tobogán", "columpios", "agua", "oscuridad", "vuelo"]

    for nombre in nombres_atracciones:
        tipo = random.choice(tipos_atraccion)
        altura_minima = random.randint(80, 180)
        duracion = random.randint(30, 300)
        capacidad = random.randint(10, 50)
        intensidad = random.randint(1, 10)
        caracteristicas = random.sample(caracteristicas_posibles, k=random.randint(1, 4))
        horarios = {
            "apertura": f"{random.randint(8, 11)}:00",
            "cierre": f"{random.randint(18, 23)}:00",
            "mantenimiento": [
                f"{random.randint(12, 16)}:00-{random.randint(12, 16)}:30"
            ] if random.random() > 0.5 else []
        }
        detalles = {
            "duracion_segundos": duracion,
            "capacidad_por_turno": capacidad,
            "intensidad": intensidad,
            "caracteristicas": caracteristicas,
            "horarios": horarios
        }
        activa = random.choice([True, True, True, False])
        AtraccionRepository.crear_atraccion(nombre, tipo, altura_minima, detalles, activa)

    # -----------------------------
    # 3️⃣ Generar tickets optimizados
    # -----------------------------
    visitantes = list(VisitanteModel.select())
    atracciones = list(AtraccionModel.select())
    tipos_ticket = ["general", "colegio", "empleado"]
    descuentos_posibles = ["estudiante", "early_bird"]
    servicios_posibles = ["fast_pass", "comida_incluida", "foto_recuerdo"]

    for visitante in visitantes:
        for _ in range(random.randint(0, 3)):
            atraccion = random.choice(atracciones + [None])
            fecha_visita = date.today() + timedelta(days=random.randint(0, 90))
            tipo_ticket = random.choice(tipos_ticket)
            detalles_compra = {
                "precio": round(random.uniform(5, 100), 2),
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

    print("✅ Ingesta masiva completada: 200 visitantes, 30 atracciones, tickets generados.")
