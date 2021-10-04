import random


def jugar():
    
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera. Tu opción es:  ").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return '¡Empate!'
    
    if ganó_el_jugador(usuario, computadora):
        return '¡Ganaste!'
    
    return '¡Perdiste!'


def ganó_el_jugador(jugador, oponente):
    # Retornar True si gana el juador
    # Piedra gana a Tijera (pi > ti).
    # Tijera ana a papel (ti > pa).
    # Papel gana a tijera (pa > pi).
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())
    
