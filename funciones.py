import json

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
        "pista": pistas[i]  # Agregar la pista
    }
    palabras.append(palabra)

# Guardar el archivo JSON
with open("data.json", "w") as file:
    json.dump(palabras, file, indent=4)
