import sys
from multiplicar import Multiplicar as M


def menu_inicio():
    f_byte = input("Introduzca el byte multiplicando: ")
    s_byte = input("Introduzca el byte multiplicador: ")
    num_algo = select_algoritmo()
    mul = M(f_byte, s_byte, num_algo)
    mul.multiplicacion()
    mul.imprimir()


def select_algoritmo():
    opc = input(
        "Seleccione el algoritmo: \n1. AES \n2. SNOW 3G \n3. Salir \nOpción: ")
    if opc == '1':
        return 1
    elif opc == '2':
        return 2
    elif opc == '3':
        sys.exit()
    else:
        print("\nOpción no válida.\n")
        select_algoritmo()


menu_inicio()
