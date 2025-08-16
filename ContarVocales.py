def ContarVocales(palabra):
    contador = 0
    palabras = 'aeiou'
    for pal in palabra.lower():
        if pal in palabras:
            contador += 1
    print("Número de vocales:", contador)

ContarVocales("Programación en Python")