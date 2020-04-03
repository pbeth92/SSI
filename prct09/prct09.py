"""
    Pablo Bethencourt Díaz
    alu0100658705@ull.edu.es
    Práctica 9: Algoritmo de Diffie-Hellman
"""
from dh import DH


def menu():
    print('Algoritmo de Diffie-Hellman. Introduzca el valor de p')
    p = int(input('Valor de p: '))
    while comprobar_primo(p) == False:
        print('El valor de p debe ser un número primo.')
        p = int(input('Valor de p: '))
    a = int(input('Valor de \u03B1: '))
    while a >= p:
        print('El valor de \u03B1 debe ser menor que p.')
        a = int(input('valor de \u03B1: '))
    Xa = int(input('Valor secreto XA: '))
    Xb = int(input('Valor secreto XB: '))

    clave_dh = DH(p, a, Xa, Xb)
    clave_dh.generar_clave()
    clave_dh.imprimir()


def comprobar_primo(n):
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1
        if cont >= 3:
            return False
    return True


menu()
