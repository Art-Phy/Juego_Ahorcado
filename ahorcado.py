### Juego del Ahorcado ###

import random

# Se crea una lista de palabras para el juego
palabras = ["naruto", "gaara", "hinata", "shikamaru", "kakashi", "choji"]

# La selección de la palabra será al azar
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
intentos = 7

# Función para el estado actual de la palabra
def mostrar_palabra():
    estado_palabra = " "
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            estado_palabra += letra + " "
        else:
            estado_palabra += "_"
    return estado_palabra.strip()

# Función del juego
def jugar():
    global intentos
    print("Juguemos al Ahorcado")
    print("Te quedan", intentos, "intentos.")

    while intentos > 0:
        print("\nPalabra:", mostrar_palabra())
        letra = input("Introduce una letra: ").lower()

         # Controlar que sólo sea una letra en cada intento
        if len(letra) != 1 or not letra.isalpha():
            print("Ey, ¡no hagas trampa!, sólo puedes una letra por tirada.")
            continue

        # Controlar que la letra no se repita si ya se adivinó
        if letra in letras_adivinadas:
            print("Te hacen falta pasas, esa letra ya la tienes.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("¡Enhorabuena!")
            # Mostrar progreso
            print("\nProgreso:", mostrar_palabra())
            if set(palabra_secreta) <= set(letras_adivinadas):
                print("\n¡Muy bien!, has adivinado la palabra:", palabra_secreta, ".")
                break
        else:
            intentos -= 1
            print("Va a ser que no. Te quedan", intentos, "intentos.")
    
    if intentos == 0:
        print("\nOooh, has perdido. La palabra era:", palabra_secreta)

# Iniciar programa
jugar()

