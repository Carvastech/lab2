#Nuevo ejercicio 4 de Promedio

class Estudiante:
    def __init__(self, nombre, codigo, lab1, lab2, parcial):
        self.nombre = nombre
        self.codigo = codigo
        self.lab1 = lab1
        self.lab2 = lab2
        self.parcial = parcial

    def calcular_promedio(self):
        
        promedio = (self.lab1 * 0.30) + (self.lab2 * 0.30) + (self.parcial * 0.40)
        return promedio

    def determinar_estado(self):
        
        promedio = self.calcular_promedio()
        return "Aprobado" if promedio >= 60 else "Reprobado"

    def mostrar_info(self):
        promedio = self.calcular_promedio()
        estado = self.determinar_estado()
        print("-" * 30)
        print(f"Nombre: {self.nombre}")
        print(f"Código: {self.codigo}")
        print(f"Laboratorio 1: {self.lab1}")
        print(f"Laboratorio 2: {self.lab2}")
        print(f"Parcial: {self.parcial}")
        print(f"Promedio Final: {promedio:.2f}")
        print(f"Estado: {estado}")
        print("-" * 30)

def ingresar_datos():
    nombre = input("Ingrese el nombre del estudiante: ")
    codigo = input("Ingrese el código del estudiante: ")
    lab1 = float(input("Ingrese la calificación del Laboratorio 1: "))
    lab2 = float(input("Ingrese la calificación del Laboratorio 2: "))
    parcial = float(input("Ingrese la calificación del Parcial: "))
    return Estudiante(nombre, codigo, lab1, lab2, parcial)

def mostrar_estudiantes(estudiantes):
    print("\nEstudiantes registrados:")
    for estudiante in estudiantes:
        estudiante.mostrar_info()

def menu_principal():
    estudiantes = []  
    while True:
        print("-" * 30)
        opcion = int(input("Ingrese la opción que desea realizar:\n1. Ingresar estudiante\n2. Mostrar estudiantes\n3. Salir\n"))
        if opcion == 1:
            nuevo_estudiante = ingresar_datos()
            estudiantes.append(nuevo_estudiante)
        elif opcion == 2:
            mostrar_estudiantes(estudiantes)
        elif opcion == 3:
            print("Gracias por utilizar el sistema")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        print("-" * 30)


menu_principal()