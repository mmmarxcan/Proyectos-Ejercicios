numeros = [4, 5, 2, 4, 9, 2, 1, 5, 6]

def ListaUnicos(numeros):
    sinRepetir = []
    for num in numeros:
        if num not in sinRepetir:
            sinRepetir.append(num)
    
    print("Números únicos:", sinRepetir)

ListaUnicos(numeros)