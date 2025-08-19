tareas = [
    {"titulo": "Estudiar Python", "estado": "pendiente"},
    {"titulo": "Lavar los platos", "estado": "completada"}
]

operaciones = [
    ("agregar", "Hacer la compra"),
    ("completar", "Estudiar Python"),
    ("pendientes", ),
    ("mostrar", )
]


def GestorDeTareas(tareas , operaciones):
    for operacion in operaciones:
        if operacion[0] == 'agregar':          
            enLista = False
            for tarea in tareas:
                if operacion[1].lower() == tarea['titulo'].lower():
                    print("Esta accion ya esta registrada")
                    enLista = True
            if not enLista:
                tareas.append({"titulo":operacion[1], "estado": "pendiente"})
                print("Accion Completada")
                print("")
        elif operacion[0] == 'completar':
            enLista = False
            for tarea in tareas:
                if operacion[1].lower() == tarea['titulo'].lower():
                    tarea['estado'] = 'completada'
                    enLista = True
            if not enLista:
                print("Accion no registada , favor de registrar primero")
        elif operacion[0] == 'pendientes':
            for tarea in tareas:
                if tarea['estado'].lower() == 'pendiente':
                    print("Tareas pendientes:")
                    print("-",tarea['titulo'])
            
        elif operacion[0] == 'mostrar':
            print("")
            print("Tareas actuales:")
            for tarea in tareas:
                print(f"{tarea['titulo']} → {tarea['estado']} ")


GestorDeTareas(tareas, operaciones)
