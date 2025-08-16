texto = "Hola hola mundo mundo mundo"


def ContarPalabras(texto):
    palabras = texto.split()
    contador = {}
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in contador:
            contador[palabra] +=1
        else:
            contador[palabra] = 1
    print("Palabra - Cantidad")
    print(f"{contador}")

ContarPalabras(texto)