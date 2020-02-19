"""
Práctica: CIFRADO DE VERNAM
Objetivo: Implementar el cifrado de Vernam.
Alumno: Pablo Bethencourt Díaz
"""
import os
import verman as vm
from bcolors import Bcolors as bc


def inicio():
    print(f"{bc.UNDERLINE} Inicio. Cifrado de Verman {bc.end} \n 1. Cifrar un mensaje \n 2. Descifrar un mensaje \n 3. Salir\n")
    opcion = input("Introduzca la opción: ")
    clear()
    opciones(opcion)


def clear():
    return os.system('clear')


def opciones(opcion):
    if opcion == '1':
        entrada = input("Introduzca el mensaje a cifrar: ")
        M = vm.mensaje_a_binario(entrada)
        result = vm.insertar_clave(M)
        # clear()

        print(f"Mensaje original: {bc.BOLD} {entrada} {bc.end}")
        print(f"Mensaje original en binario: {bc.BOLD} {M} {bc.end}")
        print(f"Longitud del mensaje binario {bc.BOLD} {len(M)} {bc.end}")
        print(f"Clave aleatoria: {bc.BOLD} {result[0]} {bc.end}")
        print(f"Mensaje cifrado en binario: {bc.BOLD} {result[1]} {bc.end}")
        print(f"Mensaje cifrado: {bc.BOLD} {result[2]} {bc.end}\n")
        inicio()

    elif opcion == '2':
        entrada = input("Introduzca el mensaje cifrado: ")
        C = vm.mensaje_a_binario(entrada)
        K = input("Introduzca la clave: ")
        M = vm.cifrado_xor(C, K)
        clear()

        print(f"Mensaje cifrado:  {bc.BOLD} {entrada} {bc.end}")
        print(f"Mensaje cifrado en binario:  {bc.BOLD} {C} {bc.end}")
        print(f"Longitud del mensaje binario  {bc.BOLD} {len(C)} {bc.end}")
        print(f"Clave aleatoria:  {bc.BOLD} {K} {bc.end}")
        print(f"Mensaje original en binario: {bc.BOLD} {M} {bc.end}")
        print(
            f"Mensaje original:  {bc.BOLD} {vm.binario_a_mensaje(M)} {bc.end}\n")
        inicio()

    else:
        print("Saliendo...")


inicio()
