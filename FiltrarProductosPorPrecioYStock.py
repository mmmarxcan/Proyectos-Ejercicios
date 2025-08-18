productos = [
    {"nombre": "Producto A", "precio": 50, "stock": 10},
    {"nombre": "Producto B", "precio": 120, "stock": 5},
    {"nombre": "Producto C", "precio": 30, "stock": 0},
    {"nombre": "Producto D", "precio": 80, "stock": 2}
]


def Filtro(productos):
    for p in productos:
        if p['stock'] > 0 and p['precio'] < 100:
            print(f"Nombre: {p['nombre']}, Precio: {p['precio']}, Stock: {p['stock']}")
    
Filtro(productos)   