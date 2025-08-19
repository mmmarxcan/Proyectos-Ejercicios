contactos = [
    {"nombre": "Ana", "telefono": "123456"},
    {"nombre": "Luis", "telefono": "987654"}
]

operaciones = [
    ("agregar", "Carlos", "555555"),
    ("buscar", "Luis"),
    ("editar", "Ana", "111111"),
    ("eliminar", "Luis"),
    ("mostrar", )
]


def GestorDeContactos(contactos , operaciones):
    for operacion in operaciones:
        if operacion[0] == 'agregar':
            flag = False
            for contacto in contactos:
                if contacto['nombre'].lower() == operacion[1].lower():
                    print("Encontrado")
                    flag = True
            if not flag:
                contactos.append({'nombre': operacion[1], 'telefono': operacion[2]})
                print(f"{operacion[1]} Agregado Correctamente")
        elif operacion[0] == 'buscar':
            for contacto in contactos:
                flag = False
                if contacto['nombre'].lower() == operacion[1].lower():
                    flag = True
                    print("")
                    print("Usuario encontrado")
                    print(f"{contacto}")
                    break
            if not flag:
                print("Usuario no encontrado")
            
        elif operacion[0] == 'editar':
            flag = False
            for contacto in contactos:
                if contacto['nombre'].lower() == operacion[1].lower():
                    print("")
                    print("Usiaro encontrado")
                    contacto['telefono'] = operacion[2]
                    print("telefono actualizado",contacto['telefono'])
                    flag = True
                    break
            if not flag:
                print("Usuario no Encontrado")
        elif operacion[0] == 'eliminar':
            flag = False
            for contacto in contactos:
                if contacto['nombre'].lower() == operacion[1].lower():
                    print("")
                    print("Usiaro encontrado")
                    contactos.remove(contacto)
                    flag = True
                    break
            if not flag:
                print("Usuario no encontrado")
                
        elif operacion[0] == 'mostrar':
            print("\nLista de contactos:")
            for contacto in contactos:
                print(f"{contacto}")

GestorDeContactos(contactos, operaciones)