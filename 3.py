class Funcion:
    def __init__(self, titulo, hora, tipo, numero_sala):
        self.titulo = titulo
        self.hora = hora
        self.tipo = tipo
        self.numero_sala = numero_sala

    def calcular_precio_total(self, cantidad_boletos, es_miercoles):
        precio_base = 10.0  
        if es_miercoles:
            cantidad_boletos = (cantidad_boletos + 1) // 2  
        return precio_base * cantidad_boletos

    def mostrar_info(self):
        print("-" * 30)
        print(f"Título de la Película: {self.titulo}")
        print(f"Hora de la Función: {self.hora}")
        print(f"Tipo de Función: {self.tipo}")
        print(f"Número de Sala: {self.numero_sala}")
        print("-" * 30)

def ingresar_datos():
    titulo = input("Ingrese el título de la película: ")
    hora = input("Ingrese la hora de la función (HH:MM): ")
    tipo = input("Ingrese el tipo de función (normal/3D/IMAX): ")
    numero_sala = int(input("Ingrese el número de sala: "))
    cantidad_boletos = int(input("Ingrese la cantidad de boletos: "))
    
   
    dia_semana = input("Ingrese el día de la semana de la función (lunes, martes, ...): ").strip().lower()
    es_miercoles = dia_semana == "miércoles"

    funcion = Funcion(titulo, hora, tipo, numero_sala)
    precio_total = funcion.calcular_precio_total(cantidad_boletos, es_miercoles)
    
    return funcion, cantidad_boletos, precio_total

def mostrar_funciones(funciones):
    print("\nFunciones registradas:")
    for funcion, cantidad_boletos, precio_total in funciones:
        funcion.mostrar_info()
        print(f"Cantidad de Boletos: {cantidad_boletos}")
        print(f"Precio Total: ${precio_total:.2f}")
        print("-" * 30)

def menu_principal():
    funciones = []  
    while True:
        print("-" * 30)
        opcion = int(input("Ingrese la opción que desea realizar:\n1. Ingresar función\n2. Mostrar funciones\n3. Salir\n"))
        if opcion == 1:
            funcion, cantidad_boletos, precio_total = ingresar_datos()
            funciones.append((funcion, cantidad_boletos, precio_total))
        elif opcion == 2:
            mostrar_funciones(funciones)
        elif opcion == 3:
            print("Gracias por utilizar el sistema")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        print("-" * 30)


menu_principal()
