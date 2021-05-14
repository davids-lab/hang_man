import random
import os

ahorcado_aasci = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
   _            ___  __    ___   _      ___  ___                            _   _                    __                       _             _     ___  
  /_\    /\  /\/___\/__\  / __\ /_\    /   \/___\   ___ _ __    _ __  _   _| |_| |__   ___  _ __    / /_ __   ___  _ __    __| | __ ___   _(_) __| \ \ 
 //_\\  / /_/ //  // \// / /   //_\\  / /\ //  //  / _ \ '_ \  | '_ \| | | | __| '_ \ / _ \| '_ \  | || '_ \ / _ \| '__|  / _` |/ _` \ \ / / |/ _` || |
/  _  \/ __  / \_// _  \/ /___/  _  \/ /_// \_//  |  __/ | | | | |_) | |_| | |_| | | | (_) | | | | | || |_) | (_) | |    | (_| | (_| |\ V /| | (_| || |
\_/ \_/\/ /_/\___/\/ \_/\____/\_/ \_/___,'\___/    \___|_| |_| | .__/ \__, |\__|_| |_|\___/|_| |_| | || .__/ \___/|_|     \__,_|\__,_| \_/ |_|\__,_|| |
                                                               |_|    |___/                         \_\_|                                          /_/'''

print(logo)

fin_del_juego = False
lista_de_palabras = ["ardilla",
                     "camello",
                     "caracol",
                     "doctor",
                     "elefante",
                     "marinero",
                     "perro"
                     "dormir"
                     "torta"]
palabra_elegida = random.choice(lista_de_palabras)
lenght_palabra = len(palabra_elegida)

#vidas

vidas = 6

#Testeo palabra de la lista
#print(f'test activado, la solucion es {palabra_elegida}.')

#Mostrar espacios para letras por pantalla
mostrar = []
for _ in range(lenght_palabra):
    mostrar += "_"

while not fin_del_juego:   
    letra_usuario = input("¿Que letra elegis?: ").lower()
    os.system('cls')
    #avisar si ya elegio una letra.
    if letra_usuario in mostrar:
      print("Ya adivinaste esa palabra. Por favor elegi otra")
    #revisar la letra del usuario
    for position in range(lenght_palabra):
        letra = palabra_elegida[position]
        if letra == letra_usuario:
          mostrar[position] = letra
          print("¡Muy bien! adivinaste una letra")

    #Reducir vidas si no hay coindicencia. Si llega a 0 vidas fin del juego.
    #Avisar que la letra elegida no esta en la palabra y las vidas que restan.
    if letra_usuario not in palabra_elegida:
      vidas -= 1
      print(f"La letra elegida no esta en la palabra. Quedan {vidas} vidas")
    if vidas == 0:
      print("\033[1mBuen intento, quiza la proxima (Fin del juego)\033[0m")
      fin_del_juego = True

    #Pasar todos los elementos de la lista a string y mostrar.
    print(f"\033[1m{' '.join(mostrar)}\033[0m")

    #Revisa si el usuario ingreso todas las letras de la palabra y gano.
    if "_" not in mostrar:
        fin_del_juego = True
        print("\033[1mGanaste campeon/a (Fin del juego)\033[0m")

    #Muestra la figura del ahorcado cada vez que el usuario ingresa una letra.
    if fin_del_juego == False:
        print(ahorcado_aasci[vidas])
input("")



    