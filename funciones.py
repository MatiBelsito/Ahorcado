import json
import random

# Listas de palabras
lista_en_castellano = [
    "manzana", "banana", "uva", "naranja", "fresa", "gato", "perro", "casa", "auto", "arbol",
    "computadora", "teclado", "rato", "pantalla", "monitor", "sol", "luna", "estrella", "cielo", "nube",
    "libro", "pluma", "lapiz", "papel", "cuaderno", "escuela", "maestro", "estudiante", "aula", "pizarra",
    "ciudad", "pueblo", "villa", "montana", "rio", "oceano", "playa", "desierto", "bosque", "selva",
    "pajaro", "pez", "leon", "tigre", "elefante", "amigo", "familia", "amor", "paz", "felicidad"
]

lista_en_ingles = [
    "apple", "banana", "grape", "orange", "strawberry", "cat", "dog", "house", "car", "tree",
    "computer", "keyboard", "mouse", "screen", "monitor", "sun", "moon", "star", "sky", "cloud",
    "book", "pen", "pencil", "paper", "notebook", "school", "teacher", "student", "classroom", "blackboard",
    "city", "town", "village", "mountain", "river", "ocean", "beach", "desert", "forest", "jungle",
    "bird", "fish", "lion", "tiger", "elephant", "friend", "family", "love", "peace", "happiness"
]

# Pistas o ayudas para las palabras
pistas = [
    "Es una fruta roja o verde, y puede ser una marca de tecnología.",
    "Es una fruta amarilla, alargada y dulce.",
    "Es una fruta pequeña y redonda, puede ser morada o verde.",
    "Es una fruta cítrica de color naranja.",
    "Es una fruta roja, pequeña y dulce.",
    "Es un animal felino que suele ser doméstico.",
    "Es un animal canino, conocido como el mejor amigo del hombre.",
    "Es el lugar donde vives, con paredes y techo.",
    "Es un vehículo que se usa para viajar.",
    "Es una planta que crece muy alta, con un tronco fuerte.",
    "Es un aparato electrónico usado para calcular y crear programas.",
    "Es un dispositivo que permite escribir en una computadora.",
    "Es un dispositivo apuntador usado para interactuar con la computadora.",
    "Es una superficie en la que se proyectan imágenes o información.",
    "Es una pantalla que muestra lo que ves en la computadora.",
    "Es el cuerpo celeste que ilumina el día en la Tierra.",
    "Es el cuerpo celeste que ilumina la noche.",
    "Es el astro brillante que aparece en el cielo de noche.",
    "Es el espacio sobre la Tierra donde están las nubes.",
    "Es una masa visible de agua en el cielo.",
    "Es una herramienta para escribir.",
    "Es un objeto de escritura usado para escribir en papel.",
    "Es un instrumento usado para escribir sobre papel.",
    "Es el material en el que se escriben las ideas.",
    "Es un objeto donde se toman notas y se escriben cosas.",
    "Es el lugar donde los niños van a aprender.",
    "Es una persona que enseña en la escuela.",
    "Es una persona que aprende en la escuela.",
    "Es el espacio donde se toman clases.",
    "Es una superficie que se usa para escribir o dibujar.",
    "Es una gran área urbana donde vive mucha gente.",
    "Es un lugar con menos densidad de población que una ciudad.",
    "Es una localidad más pequeña que una ciudad.",
    "Es una gran elevación de tierra.",
    "Es un curso de agua que fluye por la tierra.",
    "Es una gran masa de agua salada.",
    "Es una zona de arena a orillas del mar.",
    "Es una zona muy árida con poca vegetación.",
    "Es un área con gran cantidad de árboles y vida salvaje.",
    "Es una región tropical con abundante vegetación.",
    "Es un animal con alas que puede volar.",
    "Es un animal acuático que vive en el mar.",
    "Es un gran felino, conocido por su melena.",
    "Es un animal salvaje similar al león, pero más pequeño.",
    "Es un animal muy grande con trompa y colmillos.",
    "Es una persona que comparte una relación cercana.",
    "Es un grupo de personas que comparten un lazo sanguíneo.",
    "Es un sentimiento profundo de afecto hacia otra persona.",
    "Es la ausencia de conflicto y violencia.",
    "Es el estado de bienestar y satisfacción."
]

# Crear el diccionario con las palabras y sus pistas
palabras = []
for i in range(len(lista_en_castellano)):
    palabra = { 
        "ID": i + 1, 
        "ingles": lista_en_ingles[i],
        "castellano": lista_en_castellano[i],
        "pista": pistas[i]
    }
    palabras.append(palabra)

# Guardar el archivo JSON de palabras
with open("data.json", "w") as file:
    json.dump(palabras, file, indent=4)

# Función para obtener una palabra aleatoria
def obtener_palabra_aleatoria():
    return random.choice(palabras)

# Función para guardar los puntajes en el archivo JSON
def guardar_puntajes(nombre, puntaje, palabra_correcta, intentos):
    try:
        with open("scores.json", "r") as file:
            puntajes = json.load(file)
    except FileNotFoundError:
        puntajes = []

    puntajes.append({"nombre": nombre, "puntaje": puntaje, "palabra": palabra_correcta, "intentos_restantes": intentos})

    with open("scores.json", "w") as file:
        json.dump(puntajes, file, indent=4)

# Función para ordenar los puntajes de mayor a menor
def obtener_puntaje(d):
    return d["puntaje"]

def mostrar_top_5_puntajes():
    try:
        with open("scores.json", "r") as file:
            puntajes = json.load(file)
    except FileNotFoundError:
        print("No hay puntajes guardados.")
        return

    puntajes.sort(key=obtener_puntaje, reverse=True)
    print("\nTop 5 Mejores Puntajes:")
    print("-" * len("Top 5 Mejores Puntajes"))
    for i in range(min(5, len(puntajes))):
        print(f"{i + 1}. {puntajes[i]['nombre']} - {puntajes[i]['puntaje']} puntos")
    print("-" * len("Top 5 Mejores Puntajes"))

# Función para adivinar la palabra
def adivinar_palabra(palabra_correcta):
    intentos = 6
    adivinanza = ["-"] * len(palabra_correcta)
    letras_correctas = []
    letras_incorrectas = []
    print(f"La palabra contiene {len(palabra_correcta)} letras")
    
    while intentos > 0:
        print(f"Intentos restantes: {intentos}")
        if intentos == 5:
            print("          0  ")
        elif intentos == 4:
            print("          0  ")
            print("         /   ")
        elif intentos == 3:
            print("          0  ")
            print("         / \\ ")
        elif intentos == 2:
            print("          0  ")
            print("         / \\ ")
            print("          |  ")
        elif intentos == 1:
            print("          0  ")
            print("         / \\ ")
            print("          |  ")
            print("         /   ")

        print(f"Letras correctas: {letras_correctas}")
        print(f"Letras incorrectas: {letras_incorrectas}")
        print("Palabra actual: " + "".join(adivinanza))
        print("-"* len ("Palabra actual: " + "".join(adivinanza)))
    
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_correctas or letra in letras_incorrectas:
            print("Ya has intentado esta letra, elige otra.")
            continue

        if letra in palabra_correcta:
            for i in range(len(palabra_correcta)):
                if palabra_correcta[i] == letra:
                    adivinanza[i] = letra
            letras_correctas.append(letra)
        else:
            letras_incorrectas.append(letra)
            intentos -= 1
        
        if "".join(adivinanza) == palabra_correcta:
            puntaje = len(palabra_correcta) + intentos
            print(f"¡Has adivinado la palabra! La palabra correcta era: {palabra_correcta}")
            print(f"Has sumado {puntaje} puntos")
            
            nombre = input("¿Cuál es tu nombre? ")
            guardar_puntajes(nombre, puntaje, palabra_correcta, intentos)
            mostrar_top_5_puntajes()
            break
    
    if "".join(adivinanza) != palabra_correcta:
        print(f"No has adivinado, la palabra correcta era: {palabra_correcta}")
        print("No has sumado puntos en esta ocasión")
        print("          0  ")
        print("         / \\ ")
        print("          |  ")
        print("         / \\ ")
        mostrar_top_5_puntajes()

# Función principal para comenzar a adivinar
def comenzar_a_adivinar():
    while True:
        print("¿En qué idioma deseas jugar?:")
        print("1. Inglés")
        print("2. Español")
        print("3. Volver al menú anterior")
        print("-" * 30)  
        print("")  

        try:
            # Solicito la opción
            idioma = int(input("Indica la opción: "))
            
            if idioma == 1:
                print("Comencemos a jugar en inglés")
                print("-" * len ("Comencemos a jugar en inglés"))
                palabra = obtener_palabra_aleatoria()  # Obtener palabra aleatoria
                print("Pista:", palabra["pista"])  # Mostrar pista
                adivinar_palabra(palabra["ingles"])  # Llamo a la función para adivinar la palabra
            elif idioma == 2:
                print("Comencemos a jugar en español")
                print("-" * len("Comencemos a jugar en español"))
                palabra = obtener_palabra_aleatoria()
                print("Pista:", palabra["pista"])
                adivinar_palabra(palabra["castellano"])
            elif idioma == 3:
                print("Volviendo al menú anterior...")
                break  # Salir de la función
            else:
                print("Opción no válida, por favor ingresa un número entre 1 y 3.")
        
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")  # En caso que no se ingrese un numero


# comenzar_a_adivinar()
