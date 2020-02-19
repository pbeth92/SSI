import os
from bcolors import Bcolors as bc
import rc4


def menu_inicio():
    print(f"{bc.UNDERLINE} Inicio. Cifrado RC4 {bc.end} \n 1. Cifrar un mensaje \n 2. Descifrar un mensaje \n 3. Salir\n")
    opcion = input("Introduzca la opción: ")
    os.system('clear')
    opciones(opcion)


def menu_base():
    print(f"{bc.UNDERLINE} Base del cifrado {bc.end} \n 1. Binario \n 2. Decimal \n 3. Hexadecimal \n 4. Ascii \n")
    base = input("Seleccione el valor de la base: ")
    os.system('clear')
    return base


def get_base(base):
    if base == '1':
        return 'Binaria'
    elif base == '2':
        return 'Decimal'
    elif base == '3':
        return 'Hexadecimal'
    elif base == '4':
        return 'Ascii'
    else:
        print(f'{bc.rojo}Opción no válida, seleccione de nuevo una base {bc.end}')
        opciones(1)


def opciones(opcion):
    try:
        if opcion == '1':
            base = menu_base()
            v_base = get_base(base)
            print(f"{bc.azul}Cifrado de un mensaje en base {v_base}. {bc.end}")
            mensaje = input("Introduzca el mensaje a cifrar: ")
            clave = input("Introduzca la clave: ")
        elif opcion == '2':
            base = menu_base()
            v_base = get_base(base)
            print(f"{bc.verde}Descifrado de un mensaje en base {v_base}. {bc.end}\n")
            mensaje = input("Introduzca el mensaje cifrado: ")
            clave = input("Introduzca la clave: ")
        elif opcion == '3':
            print(f"{bc.amarillo} Saliendo... {bc.end}")
            return
        else:
            print(f"{bc.rojo} Opción no reconocida. {bc.end}\n")
            menu_inicio()

        os.system('clear')
        cripto = rc4.RC4(mensaje, clave, base)
        cripto.crear_cifrado()
        cripto.cifrar_texto()
        cripto.imprimir_salida()
        menu_inicio()

    except:
        print(
            f"{bc.rojo} ERROR: Formato de clave no válido para la base seleccionada. {bc.end}")


menu_inicio()
