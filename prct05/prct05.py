import os
import sys
import random
from e0 import E0


def menu_inicio():
    print("Generador E0 de Bluetooth. \n1. Cifrar \n2. Descifrar \n3. Salir")
    opcion = input("Opción: ")
    os.system('cls||clear')
    opciones(opcion)


def opciones(opc):
    if opc == '1':
        cifrar()
    elif opc == '2':
        descifrar()
    elif opc == '3':
        print('Saliendo...')
    else:
        print(f'Opción "{opc}"no reconocida.')
        menu_inicio()


def cifrar():
    print('Cifrado de una clave. \nInserte la semilla: \n1. Aleatoria \n2. Manual \n3. Salir')
    opcion = input('Opción: ')
    if opcion == '1':
        k = seed_aleatoria()
    elif opcion == '2':
        k = seed_manual()
    else:
        print('Saliendo...')
        sys.exit()

    m = input('Mensaje a cifrar: ')
    cfr = E0(k, m)
    cfr.generador()
    cfr.cifrar()
    cfr.imprimir_c()


def descifrar():
    k = input("Semilla: ")
    dscfr = E0(k)
    dscfr.generador()
    dscfr.cifrar()
    dscfr.imprimir_d()


def seed_aleatoria():
    k = ''
    signos = ['0', '1']
    while len(k) < 128:
        k = (random.choice(signos)) + k
    return k


def seed_manual():
    k = input('Introduzca la semilla: ')
    while len(k) != 128 or check_bin(k) == False:
        print('La semilla debe tener longitud 128 y solo acepta caracteres binarios')
        k = input('Introduzca la semilla: ')
    return k


def check_bin(k):
    for i in range(len(k)):
        if k[i] != '0' and k[i] != '1':
            return False
    return True


menu_inicio()

# semilla de prueba: 11111101001010101101111111111110100101010110111111001111111111010010101011011111100111111010111010010101011011111100111011001010
