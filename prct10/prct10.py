"""
    Pablo Bethencourt Díaz
    alu0100658705@ull.edu.es
    Práctica 10: Implementar la demostración de conocimiento nulo de Fiat-Shamir.
"""

from fs import FS


def menu():
    # Inicialización
    print('\nAlgoritmo de Fiat-Shamir. Introduzca el valor de p, debe ser un número primo.')
    p = int(input('Valor de p: '))
    while comprobar_primo(p) == False:
        print('El valor de p debe ser un número primo.')
        p = int(input('Valor de p: '))

    print('\nIntroduzca el valor de q, debe ser un número primo.')
    q = int(input('Valor de q: '))
    while comprobar_primo(q) == False:
        print('El valor de q debe ser un número primo.')
        p = int(input('Valor de q: '))

    # Valor N público
    N = p * q

    # Identificación secreta de A
    print(
        f'\nIntroduzca un número secreto mayor que cero y menor que {N}, debe ser primo con {N}.')
    s = int(input("Número secreto: "))
    while s >= N:
        print(f'El número secreto debe ser menor que {N}')
        s = input("Número secreto: ")
    while coprimos(s, N) == False:
        print(f'{s} debe ser primo con N')
        s = input("Número secreto: ")

    ite = int(input("\nNúmero de iteraciones: "))

    algoritmo_fs = FS(p, q, N, s, ite)
    algoritmo_fs.generador()
    algoritmo_fs.imprimir()


def comprobar_primo(n):
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1
        if cont >= 3:
            return False
    return True


def coprimos(a, b):
    d_a = [i for i in range(1, b + 1) if a % i == 0]
    d_b = [i for i in range(1, b + 1) if b % i == 0]

    for val in d_a:
        if val in d_b:
            gcd = val

    if gcd == 1:
        return True
    else:
        return False


menu()
