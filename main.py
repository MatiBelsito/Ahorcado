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
            print ("Jugar")
        elif opcion == '2':
            print ("Puntajes")
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

main()

