def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(f"Calculando Fibonacci({n})")
        resultado = Fibonacci(n-1) + Fibonacci(n-2)
        print(f"Fibonacci({n}) = {resultado}")
        return resultado


def FibinacciFor(n):
    secuencia = [0,1]
    if n == 0 :
        print("0")
    if n == 1:
        print("1")
    else:
        for i in range(2,n):
           
            secuencia.append(secuencia[i-1] + secuencia[i-2])
            print(f"{secuencia}")
        #return secuencia

FibinacciFor(6)