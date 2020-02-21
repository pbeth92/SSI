"""
    Pablo Bethencourt Díaz
    alu0100658705@ull.edu.es
"""

import os
import sys
import random
from a51 import A51, check_bin


def seed_manual():
    k = input('Introduzca la semilla: ')
    while len(k) != 64 or check_bin(k) == False:
        print('La semilla debe tener longitud 64 y solo acepta caracteres binarios')
        k = input('Introduzca la semilla: ')
    return k


def seed_aleatoria():
    k = []
    signos = ['0', '1']
    while len(k) < 64:
        k.append(random.choice(signos))
    return k


def seed_reverse():
    k = seed_manual()
    k1 = k2 = k3 = ''
    kr = ''
    for i in range(len(k)):
        if i < 19:
            k1 += k[i]
        elif i >= 19 and i < 41:
            k2 += k[i]
        else:
            k3 += k[i]
    kr = k1[::-1] + k2[::-1] + k3[::-1]
    return kr


def insert_semilla():
    K = []
    print('Generar semilla: \n1. Aleatoria \n2. Manual \n3. Reverse \n4. Salir')
    var = input('\nMétodo: ')
    if var == '1':
        K = seed_aleatoria()
    elif var == '2':
        K = seed_manual()
    elif var == '3':
        K = seed_reverse()
    elif var == '4':
        print('Saliendo...')
        sys.exit()
    else:
        os.system('cls||clear')
        print(f'Opción no válida: {var}.')
        insert_semilla()
    return K


def menu_inicio():
    print(f"Cifrado A5/1. \n1. Cifrar un mensaje \n2. Descifrar un mensaje \n3. Salir")
    opcion = input("\nElija una opción: ")
    os.system('cls||clear')
    opciones(opcion)


def activar_cifrado():
    M = input('Introduzca el mensaje a cifrar: ')
    K = insert_semilla()
    cod = A51(K, M)
    cif = cod.cifrar()
    k_string = ''.join([str(x) for x in K])
    print(f'\nMensaje original: {M}')
    print(f'Mensase original en binario: {cod.mensaje_bin}')
    print(f'Semilla: {k_string}')
    print(f'Clave: {cod.clave}')
    print(f'Cifrado binario: {cif}')


def activar_descifrado():
    M = input('Introduzca el código a descifrar: ')
    while check_bin(M) == False:
        print('El código tiene que ser binario')
        M = input('Introduzca el valor: ')
    K = seed_manual()
    desc = A51(K, M)
    dcif = desc.cifrar()
    print(f'\nCódigo a descifrar: {M}')
    print(f'Semilla: {K}')
    print(f'Clave: {desc.clave}')
    print(f'Mensaje original binario: {dcif}')
    print(f'Mensaje original: {desc.binario_a_mensaje(dcif)}')


def opciones(opc):
    if opc == '1':
        activar_cifrado()
    elif opc == '2':
        activar_descifrado()
    elif opc == '3':
        print('Saliendo...')
        sys.exit()
    else:
        print(f"Opción no válida: {opc} .")
        menu_inicio()


menu_inicio()

# Probar reverse con : 1001000100011010001010110011110001001101010111100110111100001111
