"""Script de bienvenida para nuevos usuarios de Python.

Este módulo solicita el nombre del usuario a través de la consola
y muestra un mensaje de bienvenida personalizado utilizando f-strings.
"""


def main():
    """Ejecuta la interacción principal con el usuario.

    Solicita la entrada estándar (input) para obtener el nombre
    y escribe en la salida estándar (print) el saludo.
    """
    nombre = input("¿Cómo te llamas? ")

    print(f"¡Hola, {nombre}! 🌍")
    print("¡Bienvenido al mundo de Python! 🚀")


if __name__ == "__main__":
    main()
