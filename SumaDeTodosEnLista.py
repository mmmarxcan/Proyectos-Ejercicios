numeros = [10, 20, 5, 7, 3]


def SumaListaFor(numeros):
    sumar = 0
    for n in numeros:
        sumar += n
    return sumar

def SumarListaSum(numeros):
    return sum(numeros)

print("Suma de todos los números en la lista:", SumarListaSum(numeros))
print("Suma de todos los números en la lista:", SumaListaFor(numeros))