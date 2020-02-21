"""
Práctica: CIFRADO DE VIGENERE
Pablo Bethencourt Díaz
"""

import os
from bcolors import Bcolors as bc
import vigenere


def menu_inicio():
    print(f"{bc.UNDERLINE} Inicio. Cifrado de Vigenere {bc.end} \n 1. Cifrar un mensaje \n 2. Descifrar un mensaje \n 3. Salir\n")
    opcion = input("Introduzca la opción: ")
    os.system('clear')
    opciones(opcion)


def opciones(opcion):
    if opcion == '1':
        print(f"{bc.azul} Cifrado de un mensaje. {bc.end}\n")
        mensaje = input("Introduzca el mensaje a cifrar: ")
        clave = input("Introduzca la clave: ")

        codigo = vigenere.Vigenere(mensaje, clave)
        codigo.print_salida(1)
        menu_inicio()

    elif opcion == '2':
        print(f"{bc.verde} Descifrado de un mensaje. {bc.end}\n")
        mensaje = input("Introduzca el mensaje cifrado: ")
        clave = input("Introduzca la clave: ")

        codigo = vigenere.Vigenere(mensaje, clave)
        codigo.print_salida(2)
        menu_inicio()

    elif opcion == '3':
        print(f"{bc.amarillo} Saliendo... {bc.end}")

    else:
        print(f"{bc.rojo} Opción no reconocida. {bc.end}\n")
        menu_inicio()


menu_inicio()
