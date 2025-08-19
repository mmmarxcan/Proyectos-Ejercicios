estudiantes = [
    {"nombre": "Ana", "calificaciones": [90, 85, 88]},
    {"nombre": "Luis", "calificaciones": [70, 75, 80]},
    {"nombre": "María", "calificaciones": [100, 95, 98]}
]



def GestionarEstudiantes(estudiantes , operaciones):
    for operacion in operaciones:
        if operacion[0] == 'nota':
            encontrado = False
            for estudiante in estudiantes:
                if estudiante['nombre'] == operacion[1]:
                    estudiante['calificaciones'].append(operacion[2])
                    encontrado = True
            if not encontrado:
                estudiantes.append({"nombre":operacion[1] , "calificaciones":[operacion[2]]})
            print (f"\n{estudiantes}")
        
        elif operacion[0] == 'promedio':
            encontrado = False
            suma = 0
            for estudiante in estudiantes:
                if estudiante['nombre'] == operacion[1]:
                    encontrado = True
                    for calificacion in estudiante['calificaciones']:
                        suma += calificacion 
                        cantida = len(estudiante['calificaciones'])
                    promedio = suma / cantida
                    print (f"\nEl promedio de {estudiante['nombre']} : {promedio}")

            if not encontrado:
                print("\nEl estudiante no ha sido encontrado , o no esta registrado")
        
        elif operacion[0] == 'agregar':
            encontrado = False
            for estudiante in estudiantes:
                if estudiante['nombre'] == operacion[1]:
                    encontrado = True
            if not encontrado:
                estudiantes.append({"nombre": operacion[1],"calificaciones": []})
            else:
                print (f"El estudiante {operacion[1]} ya esta registrado")
        elif operacion[0] == 'mostrar':
            for estudiante in estudiantes:
                if estudiante['nombre'] == operacion[1]:
                    print(f"\n {estudiante['nombre']} → [{estudiante['calificaciones']}] ")
           

operaciones = [
    ("nota", "Ana", 92),
    ("promedio", "Ana"),
    ("agregar", "Pedro"),
    ("nota", "Pedro", 85),
    ("mostrar", "Pedro")
]

GestionarEstudiantes(estudiantes , operaciones)
print ("a") 