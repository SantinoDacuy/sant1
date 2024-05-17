#simular juego de piedra, papel o tijera

import random 
opciones= ["piedra","papel", "tijera"]
usuario = input("Elige: ").lower()
ordenador= random.choice(opciones)
print("El ordenador ha elegido:", ordenador)


if usuario not in opciones:
    print ("Error")
    quit()
elif  usuario == "tijera" and ordenador == "piedra" or usuario == "piedra" and ordenador == "papel" or usuario == "papel" and ordenador == "tijera":
    print("Has perdido!")
else:
    print("Felicitaciones, has ganado!")

           