import random

opciones = ["piedra", "papel", "tijera"]

#------------------------------------------------------------------------------------
while True:
    usuario = input("Elige (piedra, papel, tijera) o 'salir' para terminar: ").lower()
    
    if usuario == 'salir':
        print("¡Gracias por jugar!")
        break
    
    ordenador = random.choice(opciones)
#--------------------------------------------------------------------------------------
    print("El ordenador ha elegido:", ordenador)
    
    if usuario not in opciones:
        print("Error, opción no válida.")
    elif usuario == "tijera" and ordenador == "piedra" or usuario == "piedra" and ordenador == "papel" or usuario == "papel" and ordenador == "tijera":
        print("Has perdido!")
    else:
        print("Felicitaciones, has ganado!")
