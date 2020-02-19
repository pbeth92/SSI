import random


def mensaje_a_binario(mensaje, encoding='utf-8'):
    num = int.from_bytes(mensaje.encode(encoding), byteorder='big')
    bits = bin(num)[2:]
    while len(bits) % 8 != 0:
        bits = '0' + bits
    return bits


def binario_a_mensaje(cod_bin, encoding='utf-8'):
    num = int(cod_bin, 2)
    return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big').decode(encoding, errors='replace') or '\0'


def cifrado_xor(mensaje, cifrado):
    resultado = ''
    i = len(mensaje) - 1
    while(i >= 0):
        if (mensaje[i] == cifrado[i]):
            resultado = '0' + resultado
        else:
            resultado = '1' + resultado
        i = i - 1
    return resultado


def clave_aleatoria(mensaje):
    tam = len(mensaje) / 8
    resultado = []
    signos = []

    # Lee un fichero con los símbolos ascii y los carga en una lista
    with open('signos.txt') as f:
        for line in f:
            for c in line.split():
                signos.append(c)

    # Generamos un mensaje aleatorio y lo insertamos en la salida
    secuencia = ''
    while len(secuencia) < tam:
        secuencia = random.choice(signos) + secuencia
    resultado.append(secuencia)

    # Convertimos el cifrado a binario y se inserta en la salida
    secuencia_bin = mensaje_a_binario(secuencia)
    resultado.insert(0, secuencia_bin)

    # Generamos la clave y se interta en la salida
    clave = cifrado_xor(mensaje, secuencia_bin)
    resultado.insert(0, clave)
    return resultado


def clave_teclado(mensaje):
    resultado = []
    clave = input("Introduzca la clave: ")
    # Comprueba que la clave es del mismo tamaño que el mensaje
    while len(clave) != len(mensaje):
        print("Clave no válida, debe tener igual tamaño.")
        clave = input("Introduzca una nueva clave: ")
    resultado.insert(0, clave)

    # Generamos el mensaje cifrado en binario
    cifrado_bin = cifrado_xor(mensaje, clave)
    resultado.insert(1, cifrado_bin)

    # Generamos el mensaje cifrado en ascii
    cifrado = binario_a_mensaje(cifrado_bin)
    resultado.insert(2, cifrado)
    return resultado


def insertar_clave(mensaje):
    print(f"Insertar clave: ")
    print('0. Manual.')
    print('1. Aleatoria.')
    opc = input("Introduzca la opción: ")
    if (opc == '0'):
        valores = clave_teclado(mensaje)
        return valores
    elif (opc == '1'):
        valores = clave_aleatoria(mensaje)
        return valores
    else:
        print("Opción no reconocida.")
        insertar_clave(mensaje)
