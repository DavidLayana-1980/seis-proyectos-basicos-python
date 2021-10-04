import random

def adivina_el_número(x):

    print("=======================")
    print(" ¡Bienvenido al juego! ")
    print("=======================")
    print("Tu meta es adivinar el número generado por la computadora.")

    número_aleatorio = random.randint(1, x) #Número aleatorio entre 1 y x.

    predicción = 0

    while predicción != número_aleatorio:
        # El usuario ingresa un número
        predicción = int(input(f"Adivina un número entre 1 y {x}: ")) #F-string

        if predicción < número_aleatorio:
            print("Intenta otra vez. Este número es muy pequeño")
        elif predicción > número_aleatorio:
            print("Intenta otra vez. Este número es muy grande")
        
    print(f"Felicitaciones! Adivinaste correctamente el número {número_aleatorio}")


adivina_el_número(50)
