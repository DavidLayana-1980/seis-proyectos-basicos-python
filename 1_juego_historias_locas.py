#Concatenar cadenas de caracteres.
#Crearemos una cadena que diga: "Aprende a programar con ________"

organización = "freeCodeCamp"

print("Aprende a programar con " + organización)
print("Aprende a programar con {}".format(organización))
print(f"Aprender a programar con {organización}") #f-string


# Mad Libs (Historias Locas)

adjetivo = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo en plural: ")

madlib = f"¡Programar es tan {adjetivo}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madlib)
