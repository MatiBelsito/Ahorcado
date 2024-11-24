import json
from funciones import comenzar_a_adivinar, mostrar_top_5_puntajes
# from funciones import *

def mostrar_menu():
    print ("-" * 8)
    print ("AHORCADO")
    print ("-" * 8)
    print("Menu Principal")
    print("1. Jugar")
    print("2. Puntajes")
    print("3. Salir")
    print("-" * 30)


def main():
    while True:
        mostrar_menu()  # Muestra el menú
        try:
            opcion = int(input("Selecciona una opción: "))  # Solicita la opción del usuario
            
            if opcion == 1:
                comenzar_a_adivinar()  # Llama a la función para comenzar a jugar
            elif opcion == 2:
                mostrar_top_5_puntajes()  # Llama a la función para mostrar los puntajes
            elif opcion == 3:
                print("¡Gracias por jugar! ¡Hasta luego!")  # Mensaje de despedida
                exit()  # Sale del programa
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 3.")
            
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")  # Maneja el error si se ingresa algo no numérico


main()  # Llamo a la función principal para ejecutar el menú