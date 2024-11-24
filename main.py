import funciones


def adivinar():
    
    
    print ("¿En que idioma desea jugar ?:")
    print ("1. Ingles")
    print ("2. Español")
    print ("3. Volver al menu anterior")
    
    while True:
    
        idioma = int(input("Indique la opción: "))
    
        if (idioma == 1):
            print ("comencemos a jugar en ingles")
        
        elif (idioma ==2):
            print ("comencemos a jugar en español")
        elif (idioma ==3):
            main()   
        
        else:
            print ("opción invalida, reintente: ")


# adivinar()


def mostrar_menu():
    print("----- Menú de Opciones -----")
    print("1. Jugar")
    print("2. Puntajes")
    print("3. Salir")
    print("-----------------------------")


# mostrar_menu()

def main():
    
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
           adivinar()
        elif opcion == '2':
            print ("Puntajes")
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

main()




