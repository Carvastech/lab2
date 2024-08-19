#Este es un programa, el cual se puede aplicar en el caso de trabajar en alguna empresa de videojuegos, trantando en este caso con las cosas llamadas SKINS
#siendo cosas desbloqueables dentro del juego. Asi que este ejercicio sirve para poder agregar, revisar y buscar las skins adquiridas por el usuario, o que
#puedan ser revisadas por un admin.


class Skin:
    def __init__(self, nombre, tipo, rareza):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza

    def __str__(self):
        return f"Skin: '{self.nombre}', Tipo: {self.tipo}, Rareza: {self.rareza}"

class ColeccionSkins:
    def __init__(self):
        self.skins = []

    def agregar_skin(self, skin):
        self.skins.append(skin)
        print(f"Skin '{skin.nombre}' agregada con éxito.")

    def mostrar_skins(self):
        if not self.skins:
            print("No hay skins en la colección.")
        else:
            print("Lista de skins en la colección:")
            for skin in self.skins:
                print(skin)

    def buscar_skin(self, nombre):
        encontrados = [skin for skin in self.skins if nombre.lower() in skin.nombre.lower()]
        if encontrados:
            print("Skins encontradas:")
            for skin in encontrados:
                print(skin)
        else:
            print("No se encontraron skins con ese nombre.")

def main():
    coleccion = ColeccionSkins()

    while True:
        print("\nMenú:")
        print("1. Agregar skin")
        print("2. Mostrar skins")
        print("3. Buscar skin")
        print("4. Salir")
        opcion = input("Elija una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre de la skin: ")
            tipo = input("Ingrese el tipo de la skin (Ej. Cuchillo, Ares, etc.): ")
            rareza = input("Ingrese la rareza de la skin (Ej. Común, Rara, Épica, Legendaria): ")
            skin = Skin(nombre, tipo, rareza)
            coleccion.agregar_skin(skin)
        elif opcion == '2':
            coleccion.mostrar_skins()
        elif opcion == '3':
            nombre = input("Ingrese el nombre de la skin que desea buscar: ")
            coleccion.buscar_skin(nombre)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()