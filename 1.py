
#Nuevo ejercicio 1 de Hamburguesas y Gaseosas

class Producto:
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio: ${self.precio:.2f}")
        print("-" * 30)

class Orden:
    def __init__(self):
        self.productos = []
        self.total = 0.0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.precio

    def mostrar_orden(self):
        print("\nOrden del cliente:")
        for producto in self.productos:
            producto.mostrar_info()
        print(f"Total a pagar: ${self.total:.2f}")
        print("-" * 30)

def ingresar_producto(tipo):
    if tipo == "hamburguesa":
        tipo_hamburguesa = input("Ingrese el tipo de hamburguesa (res/pollo): ").strip().lower()
        if tipo_hamburguesa == "res":
            nombre = "Hamburguesa de Res"
            precio = 5.00
        elif tipo_hamburguesa == "pollo":
            nombre = "Hamburguesa de Pollo"
            precio = 4.50
        else:
            print("Tipo de hamburguesa no válido.")
            return None
    elif tipo == "gaseosa":
        tamaño_gaseosa = input("Ingrese el tamaño de la gaseosa (pequeño/grande): ").strip().lower()
        if tamaño_gaseosa == "pequeño":
            nombre = "Gaseosa Pequeña"
            precio = 1.50
        elif tamaño_gaseosa == "grande":
            nombre = "Gaseosa Grande"
            precio = 2.50
        else:
            print("Tamaño de gaseosa no válido.")
            return None
    else:
        print("Tipo de producto no válido.")
        return None

    return Producto(nombre, tipo, precio)

def registrar_orden():
    orden = Orden()
    while True:
        tipo_producto = input("Ingrese el tipo de producto (hamburguesa/gaseosa) o 'fin' para cancelar: ").strip().lower()
        if tipo_producto == "fin":
            break
        producto = ingresar_producto(tipo_producto)
        if producto:
            orden.agregar_producto(producto)
    return orden

def menu_principal():
    while True:
        print("Seleccione la opción que desea realizar:")
        print("1. Registrar nueva orden")
        print("2. Salir")
        opcion = int(input("Ingrese el número correspondiente a la opción que desea realizar: "))

        if opcion == 1:
            orden = registrar_orden()
            orden.mostrar_orden()
            while True:
                try:
                    pago = float(input("Ingrese con cuánto va a pagar: $"))
                    if pago < orden.total:
                        print("El monto ingresado es insuficiente. Por favor, intente de nuevo.")
                    else:
                        cambio = pago - orden.total
                        print(f"Su cambio es: ${cambio:.2f}")
                        break
                except ValueError:
                    print("Ingrese un monto válido.")
        elif opcion == 2:
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu_principal()