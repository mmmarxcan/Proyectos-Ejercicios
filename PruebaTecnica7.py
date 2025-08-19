salas = [
    {"nombre": "Sala A", "capacidad": 5, "reservas": []},
    {"nombre": "Sala B", "capacidad": 10, "reservas": []}
]

operaciones = [
    ("mostrar", ),
    ("reservar", "Sala A", "10:00-11:00", 4),
    ("reservar", "Sala A", "10:00-11:00", 2),
    ("reservar", "Sala B", "12:00-13:00", 8),
    ("cancelar", "Sala A", "10:00-11:00"),
    ("mostrar", )
]


def ReservaDeSalas(salas, operaciones):
    for operacion in operaciones:
        if operacion[0] == 'reservar':
            flag = False
            for sala in salas:
                if sala['nombre'].lower() == operacion[1].lower():
                    flag = True
                    hora = operacion[2]
                    reserva = operacion[3]
                    
                    if 'reservas_detalle' not in sala:
                        sala['reservas_detalle'] = {}

                    if hora not in sala['reservas_detalle']:
                        sala['reservas_detalle'][hora] = 0

                    # Comprobar capacidad disponible
                    if sala['reservas_detalle'][hora] + reserva > sala['capacidad']:
                        print(f"No hay espacio suficiente en {sala['nombre']} para {reserva} personas a las {hora}")
                    else:
                        sala['reservas_detalle'][hora] += reserva
                        print(f"Reservado {reserva} personas en {sala['nombre']} a las {hora}")
            if not flag:
                print("No se ha encontrado la sala")
        if operacion[0] == 'mostrar':
            print("\nSalas disponibles:")
            for sala in salas:
                reservas = sala.get('reservas_detalle', {})
                if reservas:
                    reservas_str = ", ".join([f"{hora}: {cantidad} personas" for hora, cantidad in reservas.items()])
                else:
                    reservas_str = "Sin reservas"
                print(f"{sala['nombre']} (Capacidad: {sala['capacidad']}) → Reservas: {reservas_str}")

        
ReservaDeSalas(salas, operaciones)
