"""
    Pablo Bethencourt Díaz
    alu0100658705@ull.edu.es
    Práctica 11: Implementar el cifrado de clave pública RSA. 
"""
from rsa import RSA


def menu():
    print("Algoritmo RSA. \n 1.Cifrar mensaje \n 2.Descifrar mensaje \n 3.Salir")
    opc = input("Opción: ")
    if opc == '1':
        mensaje = input("\nIntroduzca el mensaje a cifrar: ")
        cifrar = RSA(mensaje)
        cifrar.cifrar_mensaje()
        cifrar.imprimir()

    elif opc == '2':
        mensaje = input("Introduzca el mensaje a descifrar: ")
        descifrar = RSA(mensaje)
        descifrar.descifrar()


menu()
