class Perro: 
    def __init__(self, nombre, edad, numerodueño, raza, peso, tipo):
        self.nombre = nombre
        self.edad = edad
        self.numerodueno = numerodueño
        self.raza = raza
        self.tipo = tipo
        self.peso = peso
        self.estado = "No atendido"

    def mostrar_info(self): 
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Número del dueño: {self.numerodueño}")
        print(f"Raza: {self.raza}")
        print(f"Tipo: {self.tipo}")
        print(f"Estado: {self.estado}")
        print("-" * 30)

def ingresar_perro():  
    nombre = input("Ingrese el nombre del perro: ")
    edad = input("Ingrese la edad del perro: ")
    numerodueno = input("Ingrese el número del dueño: ")
    raza = input("Ingrese la raza del perro: ")
    peso = float(input("Ingrese el peso del perro (en kg): "))
    if peso < 10: 
        tipo = "Pequeño"
    else:
        tipo = "Grande"
    perro = Perro(nombre, edad, numerodueno, raza, peso, tipo)  
    perro.estado = "Atendido" 
    return perro 

def mostrar_perros(): 
    print("\nPerros registrados:")
    for perro in perros:
        perro.mostrar_info()

def menu_principal(): #funcion para el menu principal
    while True:
        print("Seleccione la opción que desea realizar:")
        print("1. Registrar perro")
        print("2. Mostrar perros")
        print("3. Salir")
        opcion = int(input("Ingrese el número correspondiente a la opción que desea realizar: "))

        if opcion == 1:
            nuevo_perro = ingresar_perro()
            perros.append(nuevo_perro)
        elif opcion == 2:
            mostrar_perros()
        elif opcion == 3:
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Lista global para almacenar los perros
perros = []

# Ejecutar el menú principal
menu_principal()