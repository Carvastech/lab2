class dispositivo: 
    def __init__(self, marca, modelo, anofabricacion, paisproveniencia,precio, resolucion):
        self.marca = marca
        self.modelo = modelo
        self.anofabricacion = anofabricacion
        self.paisproveniencia = paisproveniencia
        self.precio = precio
        self.resolucion = resolucion
    def mostrar_info(self): 
        print("-" * 30)
        print(f"Marca: {self.marca}")
        print(f"Moedelo: {self.modelo}")
        print(f"Ano fabricacion: {self.anofabricacion}")
        print(f"Pais de Proveniencia: {self.paisproveniencia}")
        print(f"Precio de venta: ${self.precio}")
        print(f"resolucion: {self.resolucion}")
        print("-" * 30)

def ingresar_datos(): 
    marca = input("Ingrese la marca del dispositivo: ")
    modelo = input("Ingrese el modelo del dispositivo: ")
    anofabricacion = input("Ingrese el año de fabricacion del dispositivo: ")
    paisproveniencia = input("Ingrese el pais de proveniencia del dispositivo: ")
    precio_compra = float(input("Ingrese el precio de compra del dispositivo: $"))
    precio = calcular_precio(precio_compra)
    resolucion = input("Ingrese la resolucion de la pantalla del dispositivo:")
    return dispositivo(marca, modelo, anofabricacion, paisproveniencia, precio,resolucion)

def calcular_precio(precio_compra, margen = 1.7): 
    precio = precio_compra * margen
    return precio

dispositivos = [] 

def mostrar_dispositivos(dispositivos): 
    print("\ndispositivos registrados:")
    for dispositivos in dispositivos:
        dispositivos.mostrar_info()

def menu_principal(): 
    print("-" * 30)
    while True:
        opcion = int(input("Ingrese la opcion que desea hacer: \n Opcion 1: Ingresar dispositivo \n Opcion 2: Mostrar dispositivo \n Opcion 3: Salir \n"))
        if opcion == 1:
            nuevo_dispositivo = ingresar_datos()
            dispositivos.append(nuevo_dispositivo)
        elif opcion == 2:
            mostrar_dispositivos(dispositivos)
        if opcion == 3:
            print("Gracias por utilizar el sistema")
            break
        print("-" * 30)

menu_principal()