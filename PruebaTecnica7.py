salas = [
    {"nombre": "Sala A", "capacidad": 10, "reservas": ["09:00-10:00"]},
    {"nombre": "Sala B", "capacidad": 20, "reservas": []}
]

operaciones = [
    ("reservar", "Sala A", "10:00-11:00"),
    ("reservar", "Sala A", "09:00-10:00"),
    ("cancelar", "Sala B", "11:00-12:00"),
    ("mostrar", "Sala A")
]


def ReservaDeSalas(salas, operaciones):
    for operacion in operaciones:
        if operacion[0] == 'reservar':
            flag = False
            print(f"{operacion}")
            for sala in salas:
                print(f"{sala}")


ReservaDeSalas(salas, operaciones)
