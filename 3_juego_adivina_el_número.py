import random


def adivina_el_número_computadora(x):

    print("=======================")
    print(" ¡Bienvenido al juego! ")
    print("=======================")
    print("Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo.")

    límite_inferior = 1
    límite_superior = x

    respuesta = ""
    while respuesta != "c":
        # Generar predicción
        if límite_inferior != límite_superior: 
            predicción = random.randint(límite_inferior, límite_superior)
        else:
            predicción = límite_inferior # También podría ser el límite superior
        
        # Obtener respuesta del usuario
        respuesta = input(f"Mi predicción es {predicción}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower()


        if respuesta == "a":
            límite_superior = predicción - 1
        elif respuesta == "b":
            límite_inferior = predicción + 1

    print(f"¡Siiii! La computadora adivinó tu número correctamente. El número era {predicción}")


adivina_el_número_computadora(10)

    
