inventario = {
    "manzanas": 10,
    "naranjas": 5,
    "plátanos": 8
}


def GestorDeInventario(inventario , operaciones):
    for operacion , producto , cantidad in operaciones:
        ##print (operacion , producto , cantidad)
        if producto in inventario:
            if operacion == 'agregar':
                inventario[producto] += cantidad
            elif operacion == 'retirar':
                if inventario[producto] < cantidad:
                    inventario[producto] = 0
                else:
                    inventario[producto] -= cantidad                    
        else:
            inventario[producto] = cantidad
    
    return inventario

    
    """
            print("\nse hace algo")
            print ("Manzanas",inventario['manzanas'])
        elif operacion == 'retirar':
            print ('\nse retira algo')"""   
            
            
            
inventario = {"manzanas": 10, "naranjas": 5, "plátanos": 8}
operaciones = [("agregar", "manzanas", 3), 
               ("retirar", "plátanos", 10), 
               ("agregar", "kiwis", 4)]

GestorDeInventario(inventario , operaciones)