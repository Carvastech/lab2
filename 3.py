class Auto: 
    def __init__(self, modelo,tipo, marca, año, kilometraje, precio, color, transmision, placa, traccion):
        self.modelo = modelo
        self.tipo = tipo
        self.marca = marca
        self.ano = año
        self.precio = precio
        self.color = color
        self.kilometraje = kilometraje
        self.transmision = transmision
        self.placa = placa
        self.traccion = traccion
        self.capacidad = "5 pasajeros"
        self.ruedas = "4 ruedas"


    def mostrar_info(self): 
        print("-" * 30)
        print(f"modelo: {self.modelo}")
        print(f"marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Año: {self.ano}")
        print(f"color: {self.color}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Ruedas: {self.ruedas}")
        print(f"transmision: {self.transmision}")
        print(f"placa: {self.placa}")
        print(f"Kilometraje: {self.kilometraje}")
        print(f"Precio de Venta: ${self.precio}")
        print("-" * 30)

def ingresar_autos():
    modelo = input("Ingrese el modelo del auto: ")
    tipo = input("Ingrese el tipo del auto: ")
    marca = input("Ingrese la marca del auto: ")
    año = int(input("Ingrese el año del auto: "))
    kilometraje = int(input("Ingrese el kilometraje del auto: "))
    precio = float(input(f"Ingrese el precio de compra del auto {modelo}: $"))
    color = input("Ingrese el color del auto: ")
    transmision = input("Ingrese la transmision del auto: ")
    placa = input("Ingrese la placa del auto: ")
    traccion = input("Ingrese la traccion del auto: ")
    PendingDeprecationWarning = calcular_precio(precio)
    return Auto(modelo, tipo, marca, año, kilometraje, precio, color, transmision, placa, traccion)

def calcular_precio(precio, margen=1.4):
    precio = precio * margen
    return precio


autos = []

def mostrar_autos(autos):
    print("\nAutos registrados:")
    for autos in autos:
        autos.mostrar_info()


def menu_principal(): 
    while True:
        opcion = int(input("Ingrese la opcion que desea hacer: \n Opcion 1: Ingresar auto \n Opcion 2: Mostrar Autos \n Opcion 3: Salir \n"))
        if opcion == 1:
            nuevo_auto = ingresar_autos()
            autos.append(nuevo_auto)
        elif opcion == 2:
            mostrar_autos(autos)
        if opcion == 3:
            print("Gracias por utilizar el sistema")
            break

menu_principal() 
