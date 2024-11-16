import json

# Lista de palabras

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


# Creo un diccionario con las listas

palabras =[]

for i in range(len(lista_en_castellano)):
    
    palabra = { 
         
         "ID": i +1,     
         "ingles": lista_en_ingles[i],
         "castellano": lista_en_castellano[i]
         
         }
    palabras.append (palabra)
    
    


# Creo el archivo json donde voy a guardar el diccionario

with open ("data.json", "w") as file:
    json.dump(palabras, file, indent =4)   # esta linea convierte el diccionario  "datos" en una cadena json. "file" hace referencia a "data.json"
 
 
