import json

def AnalizarTexto(texto):
    diccionario = {}
    frecuencia = {}
    textoLimpio = texto.split()
    contador = 0
    contadorCaracteres = 0
    palabraMaslarga = max(textoLimpio, key=len).strip(".,:;")
    
    for x in textoLimpio:
        contador += 1
        palabra  = x.lower().strip(".,:;")
        contadorCaracteres += len(palabra)
        
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    diccionario["total_palabras"] = contador
    diccionario["total_caracteres"] = contadorCaracteres
    diccionario["palabra_mas_larga"] = palabraMaslarga
    diccionario['frecuencia de palabras'] = frecuencia
    print(json.dumps(diccionario, indent=4, ensure_ascii=False))



texto = "Python es un lenguaje de programación. Python es poderoso y flexible."
AnalizarTexto(texto)


# ouput 
"""{
    "total_palabras": 10,
    "total_caracteres": 56,
    "palabra_mas_larga": "programación",
    "frecuencia_palabras": {
        "python": 2,
        "es": 2,
        "un": 1,
        "lenguaje": 1,
        "de": 1,
        "programación": 1,
        "poderoso": 1,
        "y": 1,
        "flexible": 1
    }
}"""