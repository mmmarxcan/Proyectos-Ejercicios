#Implementa una función en Python que reciba una lista de enteros y devuelva una nueva lista con solo los números pares, ordenados de menor a mayor.
#Ejemplo: [5,2,8,1,4] → [2,4,8]

def Pares(lista):
    nuevalista = []
    mayor = 0
    for l in lista:
        if l % 2 == 0:
            nuevalista.append(l)
        nuevalista.sort()
                
    print(f"{nuevalista}")    
def ParesSinSort(lista):
    nuevaLista = []
    for l in lista:
        if l % 2 == 0:
            nuevaLista.append(l)
    n = len(nuevaLista)
    for i in range(n):
        for j in range(0, n-i-1):
            if nuevaLista[j] > nuevaLista[j+1]:
                nuevaLista[j], nuevaLista[j+1] = nuevaLista[j+1], nuevaLista[j]
    print(f"{nuevaLista}")

lista = [5,2,8,1,4]
#ParesSinSort(lista)
#Pares(lista)

#Crea una función recursiva que calcule el factorial de un número entero positivo.
#Ejemplo: factorial(5) → 120

def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n-1) 
#algo = Factorial(3)
#print(f"{algo}")


def Fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1 
        else:
            return Fibonacci(n-1) + Fibonacci(n-2)

#resultado = Fibonacci(2)
#print(f"{resultado}")

def Palindromo (palabra):
    palabra.lower()
    return palabra == palabra[::-1]

palabra = Palindromo("OSO")
print(f"{palabra}")