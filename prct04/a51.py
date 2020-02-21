"""
    Pablo Bethencourt Díaz
    alu0100658705@ull.edu.es
"""


class A51():
    def __init__(self, seed, mensaje):
        self.a = self.crear_lista(seed, 0, 19)
        self.b = self.crear_lista(seed, 19, 41)
        self.c = self.crear_lista(seed, 41, 64)
        if check_bin(mensaje):
            self.mensaje_bin = mensaje
        else:
            self.mensaje_bin = self.mensaje_a_binario(mensaje)
        self.clave = self.generar_clave()

    """
        Funcion: crear_lista
        Crea los registros a partir de la semilla
    """

    def crear_lista(self, lista, ini, fin):
        l_result = []
        while ini < fin:
            l_result.append(int(lista[ini]))
            ini += 1
        return l_result

    def mensaje_a_binario(self, mensaje, encoding='utf-8'):
        num = int.from_bytes(mensaje.encode(encoding), byteorder='big')
        bits = bin(num)[2:]
        while len(bits) % 8 != 0:
            bits = '0' + bits
        return bits

    def binario_a_mensaje(self, cod_bin, encoding='utf-8'):
        num = int(cod_bin, 2)
        return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big').decode(encoding, errors='replace') or '\0'

    def f_mayoria(self, a, b, c):
        if (a + b + c) > 1:
            return 1
        else:
            return 0

    def desplazamiento(self, lista, valor):
        lista.pop()
        lista.insert(0, valor)

    """
        Función: generar_clave
        Genera una clave con length = len(mensaje_bin)
        - LLama a la función mayoría para comprobar que cadenas se desplazan
        - Realiza la operación xor en cada una de las cadenas y empuja el resultado en caso de que haya desplazamiento
        - Se utilizan los tres ultimos bits de cada cadena para realizar la operación xor, el resultado se añade a la salida
        - !!!!! NOTA: Primero realiza la función mayoria y el desplazamiento, y luego añade a la salida.
    """

    def generar_clave(self):
        print(f'Semilla original: ')
        print(f"{self.a} \n{self.b} \n{self.c}\n")
        i = 0
        salida = []
        while i < len(self.mensaje_bin):
            val_a = self.a[8]
            val_b = self.b[10]
            val_c = self.c[10]

            mayoria = self.f_mayoria(val_a, val_b, val_c)

            result_a = self.a[18] ^ self.a[17] ^ self.a[16] ^ self.a[13]
            result_b = self.b[21] ^ self.b[20]
            result_c = self.c[22] ^ self.c[21] ^ self.c[20] ^ self.c[7]

            if val_a == mayoria:
                self.desplazamiento(self.a, result_a)
            if val_b == mayoria:
                self.desplazamiento(self.b, result_b)
            if val_c == mayoria:
                self.desplazamiento(self.c, result_c)

            result = self.a[18] ^ self.b[21] ^ self.c[22]
            salida.insert(i, result)
            i += 1
            self.print_traza(val_a, val_b, val_c, mayoria, result)

        return salida

    """
        Función: imprimir_traza
        Imprime la traza en formato:
        (0,0,1) = 0
        Registro 3 paralizado
        *Imprime todos los registros*
        *imprime el resultado de la operación xor*
    """

    def print_traza(self, v_a, v_b, v_c, mayoria, result):
        print(f"\n({v_a}, {v_b}, {v_c}) = {mayoria}")
        if v_a == v_b == v_c:
            print('Ningún registro paralizado')
        elif v_a != mayoria:
            print('Registro uno paralizado.')
        elif v_b != mayoria:
            print('Regristro dos paralizado')
        else:
            print('Registro tres paralizado')
        print(f"{self.a} \n{self.b} \n{self.c}")
        print(f"z(t)= {result}")

    """
        Función: cifrar
        Realiza cifrado xor
    """

    def cifrar(self):
        res = ''
        for i in range(len(self.mensaje_bin)):
            x = int(self.mensaje_bin[i]) ^ self.clave[i]
            res = res + str(x)
        return res


""" Función: check_bin
    Comprueba si una cadena está en formato binario
"""


def check_bin(k):
    for i in range(len(k)):
        if k[i] != '0' and k[i] != '1':
            return False
    return True
