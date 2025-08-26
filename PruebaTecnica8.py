salas = [
    {"nombre": "Sala A", "capacidad": 5, "reservas": []},
    {"nombre": "Sala B", "capacidad": 10, "reservas": []}
]


def mostrar_salas(diccionario):
    for d in diccionario:
        print(f"Nombre: {d['nombre']} - Capacidad: {d['capacidad']}  \rReserva : [{d['reservas']}]\n")
    

#

def reservar_sala(diccionario, sala, horario, cantidad):
    for d in diccionario:
        if d['nombre'].lower() == sala.lower():
            for r in d['reservas']:
                if r['horario'] == horario:
                    print("Ya hay una reserva en ese horario")
                    return
            if cantidad <= d['capacidad']:
                d['reservas'].append({
                    "horario": horario,
                    "personas": cantidad
                })
                print("Reserva realizada")
            else:
                print("No hay espacio suficiente")
            return
    print("No se encontro la sala")
    
def cancelar_reserva(diccionario, sala, horario):
    for d in diccionario:
        if d['nombre'].lower() == sala.lower():
            for r in d['reservas']:
                if r["horario"] == horario:
                    d['reservas'].remove(r)
                    print("Reserva cancelada")
                    return
            print(" No existe esa reserva")
            return
    print("No se encontró la sala")

def listar_reservas(diccionario):
    for d in diccionario:
        print(f"Reservas en {d['nombre']}:")
        if d['reservas']:
            for r in d['reservas']:
                print(f"- {r['horario']} ({r['personas']} personas)")
        else:
            print("No hay reservas")
        print("")


reservar_sala(salas, "Sala A", "10:00-11:00", 4)   
reservar_sala(salas, "Sala A", "10:00-11:00", 2)   
mostrar_salas(salas)

cancelar_reserva(salas, "Sala A", "10:00-11:00")  
listar_reservas(salas)