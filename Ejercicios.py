calificaciones = {
    "Ana": 85,
    "Luis": 90,
    "María": 78,
    "Pedro": 92,
    "Sofía": 88
}


def Promedio(listas):
    suma = 0
    for lista in listas.values():
        suma += lista
    cantidadCali = len(calificaciones)
    promedio = suma /  cantidadCali
    print(f"Promedio: {promedio}")

    mejor = max(listas, key=listas.get)
    peor = min(listas, key=listas.get)
    print(f"Calificación más alta: {listas[mejor]} ({mejor})")
    print(f"Calificación más baja: {listas[peor]} ({peor})")
#Promedio(calificaciones)

def Lista():
    lista = input("Introduce los numeros separados por un espacio:")
    ListaCompleta = []
    pares = []
    impares = []

    nuevalista =[int(l) for l in  lista.split(" ")]
    for l in nuevalista:
        if l % 2 == 0:
            pares.append(l)
        else:
            impares.append(l)
    ListaCompleta = nuevalista
    
    print(f"Lista completa: {nuevalista}")
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")  
    
Lista()