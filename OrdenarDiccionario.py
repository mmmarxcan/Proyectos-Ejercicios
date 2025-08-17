personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Carlos", "edad": 20},
    {"nombre": "Maria", "edad": 27}
]

def OrdenarPorEdad(personas):
    sorted_personas = sorted(personas, key=lambda x: x['edad'])
    for persona in sorted_personas:
        print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}")

OrdenarPorEdad(personas)