from columna import Columna as Col


# OPERACIONES MULTIPLICACIÓN:
def multiplicar(v1, v2):
    mnd = transformar(convert_binario(v1))
    mul = transformar(convert_binario(v2))
    result = []
    b_sale = 0
    for i in reversed(range(8)):
        if b_sale == 1:
            operar(mnd)
        if mul[i] == 1:
            result.append(mnd[:])
        b_sale = desplazar(mnd)
    return mul_result(result)


def transformar(cadena):
    lista = []
    for i in range(len(cadena)):
        lista.append(int(cadena[i]))
    return lista


def desplazar(lista):
    r = lista.pop(0)
    lista.append(0)
    return r


def operar(lista):
    B_1B = [0, 0, 0, 1, 1, 0, 1, 1]
    for i in range(len(lista)):
        lista[i] = lista[i] ^ B_1B[i]


def mul_result(lista):
    result = []
    if len(lista) == 0:
        result = [0, 0, 0, 0, 0, 0, 0, 0]
    else:
        i = 1
        result = lista[0]
        while i < len(lista):
            result = suma_xor(result, lista[i])
            i += 1
    return result


def suma_xor(l1, l2):
    for i in range(len(l1)):
        l1[i] = l1[i] ^ l2[i]
    return l1


# OPERACIONES DE CONVERSIÓN:
def convert_binario(val):
    num = int(str(val), 16)
    bits = bin(num)[2:]
    bits = fill_zeros(bits)
    return bits


def fill_zeros(bits):
    while len(bits) % 8 != 0:
        bits = '0' + bits
    return bits


def convert_hexa(l_val):
    cad = ''
    for i in range(len(l_val)):
        cad += str(l_val[i])
    num = int(str(cad), 2)
    if num == 0:
        num_hexa = '00'
    else:
        num_hexa = hex(num).lstrip("0x").rstrip("L")
    if len(num_hexa) == 1:
        num_hexa = '0' + num_hexa
    return num_hexa


def convert_hexa_lista(l_bin, base=2):
    l_hex = []
    for i in range(len(l_bin)):
        num = int(str(l_bin[i]), base)
        if num == 0:
            num_hexa = '00'
        else:
            num_hexa = hex(num).lstrip("0x").rstrip("L")
        if len(num_hexa) == 1:
            num_hexa = '0' + num_hexa
        l_hex.append(num_hexa)
    return l_hex
