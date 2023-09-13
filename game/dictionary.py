class Dictionary:
    def __init__(self):
        self.words = set()  # Utilizamos un conjunto para un acceso rápido a las palabras

    def add_word(self, word):
        self.words.add(word.lower())  # Almacenamos las palabras en minúsculas para hacer búsquedas sin distinción de mayúsculas

    def check_word(self, word):
        return word.lower() in self.words  # Verificamos si la palabra está en el conjunto (ignorando mayúsculas/minúsculas)

# Incorpora la clase Dictionary en tu código existente

# Crea una instancia del diccionario
dictionary = Dictionary()

# Agrega palabras al diccionario
dictionary.add_word("gato")
dictionary.add_word("perro")
dictionary.add_word("ratón")

# Comprueba si una palabra existe en el diccionario
print(dictionary.check_word("gato"))  # True
print(dictionary.check_word("pájaro"))  # False