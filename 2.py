class Articulo: 
    def __init__(self, tipo, marca, precio_compra, precio_venta):
        self.tipo = tipo
        self.marca = marca
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta

    def mostrar_info(self): 
        print(f"Artículo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Precio de Compra: ${self.precio_compra}")
        print(f"Precio de Venta: ${self.precio_venta}")
        print("-" * 30)

def calcular_precio_venta(precio_compra, margen=1.30): 
    return precio_compra * margen

def ingresar_articulo(): 
    print("Seleccione el tipo de artículo que desea registrar:")
    print("1. Cuaderno")
    print("2. Lápiz")
    opcion = int(input("Ingrese el número correspondiente al tipo de artículo: "))
    
    if opcion == 1:
        tipo = input("Ingrese el tipo de cuaderno (e.g., '50 hojas', '100 hojas'): ")
        marca = "HOJITAS"
    elif opcion == 2:
        tipo = input("Ingrese el tipo de lápiz (e.g., 'grafito', 'colores'): ")
        marca = "RAYAS"
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return ingresar_articulo()

    precio_compra = float(input(f"Ingrese el precio de compra para {tipo} ({marca}): "))
    precio_venta = calcular_precio_venta(precio_compra)
    return Articulo(tipo=tipo, marca=marca, precio_compra=precio_compra, precio_venta=precio_venta)


articulos = []


while True:
    articulos.append(ingresar_articulo())
    
    continuar = input("¿Desea ingresar otro artículo? (s/n): ").strip().lower()
    if continuar == 'n':
        break


print("\nArtículos registrados:")
for articulo in articulos:
    articulo.mostrar_info()
