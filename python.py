import time
import sys

def slow_print(text, delay=0.05):
    """Imprime el texto de manera gradual."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Para ir a la siguiente línea al finalizar

def presentacion():
    slow_print("¡Hola! Mi nombre es Geraldine Aynaya y quiero compartir un poco de mi experiencia con Python. 🐍")
    time.sleep(1)
    
    slow_print("Estaba muy intrigada por Python 🤔, ya que no tenía experiencia previa en ningún nivel de programación 🤧.")
    time.sleep(1)
    
    slow_print("Esto resultó en un desafío total 🫡, ya que todo lo que me enseñaban era nuevo para mí.")
    time.sleep(1)
    
    slow_print("Era clave practicar constantemente para no olvidarme de los conceptos aprendidos en clase 🙇‍♀️.")
    time.sleep(1)
    
    slow_print("Asimismo, me sirvió para darme cuenta de la infinidad de usos que Python tiene y lo creativo que puede ser 😊.")
    time.sleep(1)
    
    slow_print("¡Definitivamente Python me ha abierto un mundo nuevo de posibilidades! 🚀")

if __name__ == "__main__":
    presentacion()