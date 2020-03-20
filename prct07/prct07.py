"""
    Pablo Bethencourt Díaz
    alu0100658705@ull.edu.es
    Práctica 7: Algoritmo Rijndael
"""
import random
import sys
from rijndael import Rijndael as R

"""
    Prueba
    Clave: 000102030405060708090a0b0c0d0e0f
    Texto Original: 00112233445566778899aabbccddeeff
"""

# clave: 2b,7e,15,16,28,ae,d2,a6,ab,f7,15,88,09,cf,4f,3c

signos = ['0', '1', '2', '3', '4', '5', '6',
          '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
mensaje = 'Formato hexadecimal sin espacios: '


def clave_aleatoria():
    k = []
    cadena = ''
    while len(k) < 16:
        cadena += random.choice(signos)
        if len(cadena) == 2:
            k.append(cadena)
            cadena = ''
    return k


def input_manual(palabra):
    kv = input(mensaje)
    k = []
    cadena = ''
    for i in range(len(kv)):
        if kv[i] in signos:
            cadena += kv[i]
            if i == len(kv) - 1:
                k.append(cadena)
                cadena = ''
            if len(cadena) == 2:
                k.append(cadena)
                cadena = ''
    if len(k) != 16:
        print(
            f'Error: {palabra.upper()} ha de tener 16 bytes en hexadecimal')
        sys.exit
    return k


def generar_clave():
    print('Introducir clave: \n1. Aleatoria \n2. Manual \n3. Salir')
    var = input("Opción: ")
    if var == '1':
        k = clave_aleatoria()
    elif var == '2':
        k = input_manual('clave')
    else:
        print('Saliendo..')
        sys.exit()
    return k


def inicio():
    print('Algoritmo Rijndael: \n1. Cifrar \n2. Descifrar \n3. Salir')
    var = input("Opción: ")
    if var == '1':
        print('Mensaje a cifrar')
        texto = input_manual('Mensaje')
        print('Clave')
        clave = generar_clave()
        cifr = R(texto, clave)
        cifr.rijndael()
    elif var == '2':
        print('Mensaje a Descifrar')
        texto = input_manual('Mensaje')
        print('Clave:')
        clave = input_manual('clave')
        descifr = R(texto, clave)
        descifr.desencriptar_rijndael()
    else:
        print('Saliendo..')
        sys.exit()


inicio()
