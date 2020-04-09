"""
    Pablo Bethencourt Díaz
    alu0100658705@ull.edu.es
    Modo CBC de operación en cifrado en bloque (usando AES)
"""

from cbc import CBC


def menu_inicio():
    print("Modos de operación en cifrado en boque.")
    print("Menu: \n 1.Cifrar Texto \n 2.Descifrar Texto")
    opc = input("Elija una opción: ")
    if opc == '1':
        cifrado()
    elif opc == '2':
        descifrado()
    else:
        print('Opción no reconocida.')


def cifrado():
    print("\n\nMenu. \n 1.Cifrado Manual \n 2. Cifrado automático")
    opc = input("Elija una opción: ")
    if opc == '1':
        texto = input("Introduzca el texto a cifrar: ")
        IV = input("Introduzca el vector de inicializacion: ")
        clave = input("Introudzca la clave: ")
        cifr = CBC(texto, IV, clave)
        cifr.cifrar_cbc()
    elif opc == '2':
        # Formato hexadecimal:
        clave = '00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F'
        IV = '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
        texto = '00 11 22 33 44 55 66 77 88 99 AA BB CC DD EE FF 00 00 00 00 00 00 00 00 00 00'
        cifr = CBC(texto, IV, clave)
        cifr.cifrar_cbc()
    else:
        print('Opción no reconocida.')


def descifrado():
    print("\n\nMenu. \n 1.Descifrado Manual \n 2.Descifrado automático")
    opc = input("Elija una opción: ")
    if opc == '1':
        texto = input("Introduzca el texto a descifrar: ")
        IV = input("Introduzca el vector de inicializacion: ")
        clave = input("Introudzca la clave: ")
        cifr = CBC(texto, IV, clave)
        cifr.cifrar_cbc()
    elif opc == '2':
        # Formato hexadecimal:
        clave = '00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F'
        IV = '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
        texto = '69 C4 E0 D8 6A 7B 04 30 D8 CD B7 80 70 B4 C5 5A 4F 63 8C 73 5F 61 43 01 56 78 24 B1 A2 1A 4F 6A'
        cifr = CBC(texto, IV, clave)
        cifr.descifrar_cbc()
    else:
        print('Opción no reconocida.')


menu_inicio()
