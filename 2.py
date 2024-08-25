#Nuevo ejercicio 2 de Bicicletas

class Bicicleta:
    def __init__(self, tipo, precio_base):
        self.tipo = tipo
        self.precio_base = precio_base

    def calcular_costo_renta(self, horas):
        if self.tipo == "deportiva":
            return self.precio_base * 1.5 * horas
        else:  
            return self.precio_base * horas

    def mostrar_info(self):
        print(f"Tipo de Bicicleta: {self.tipo}")
        print(f"Precio Base por Hora: ${self.precio_base:.2f}")
        print("-" * 30)

def ingresar_bicicleta():
    print("Seleccione el tipo de bicicleta que desea registrar:")
    print("1. Deportiva")
    print("2. Tradicional")
    opcion = int(input("Ingrese el número correspondiente al tipo de bicicleta: "))

    if opcion == 1:
        tipo = "deportiva"
        precio_base = float(input("Ingrese el precio base por hora para bicicleta deportiva: "))
    elif opcion == 2:
        tipo = "tradicional"
        precio_base = float(input("Ingrese el precio base por hora para bicicleta tradicional: "))
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return ingresar_bicicleta()

    return Bicicleta(tipo=tipo, precio_base=precio_base)

def registrar_renta():
    bicicleta = ingresar_bicicleta()
    horas = float(input("Ingrese el número de horas de renta: "))
    cliente = input("Ingrese el nombre del cliente: ")
    
    costo_total = bicicleta.calcular_costo_renta(horas)
    
    print("\nDetalles de la renta:")
    print(f"Cliente: {cliente}")
    bicicleta.mostrar_info()
    print(f"Horas de Renta: {horas}")
    print(f"Costo Total de Renta: ${costo_total:.2f}")
    print("-" * 30)

def menu_principal():
    while True:
        print("Seleccione la opción que desea realizar:")
        print("1. Registrar renta de bicicleta")
        print("2. Salir")
        opcion = int(input("Ingrese el número correspondiente a la opción que desea realizar: "))

        if opcion == 1:
            registrar_renta()
        elif opcion == 2:
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


menu_principal()
