"""
    Pablo Bethencourt Díaz
    alu0100658705@ull.edu.es
"""

import os
from bcolors import Bcolors as bc


class RC4():

    def __init__(self, mensaje, key, base):
        self.S = list(range(0, 256))
        self.base = base
        self.mensaje = self.format_texto(mensaje)
        self.clave = self.format_texto(key)
        self.K = self.fill_K(self.clave)
        self.a = self.b = 0
        self.secuencia_cifrante = []
        self.texto_cifrado = []

        self.inicializar()
        self.convertir_binario(self.clave, 10)
        self.base = 2

    """
        Funcion: format_text.
        Formatea el mensaje original y la clave en función de la base
    """

    def format_texto(self, texto):
        cadena = ''
        salida = []
        if self.base == '4':    # Base ascii: Acepta todas las cadenas
            for i in range(len(texto)):
                salida.append(ord(texto[i]))

        elif self.base == '3':  # Base hexadecimal: Comprueba que es un caracter hexadeciamal
            for i in range(len(texto)):
                if self.check_base(texto[i], 16):
                    cadena += texto[i]
                    if i == len(texto) - 1:
                        salida.append(int(cadena, 16))
                        cadena = ''
                    if len(cadena) == 2:
                        salida.append(int(cadena, 16))
                        cadena = ''
                elif cadena != '':
                    salida.append(int(cadena, 16))
                    cadena = ''

        elif self.base == '2':  # Base decimal: Comprueba que es un entero
            comprobate = ''
            for i in range(len(texto)):
                if self.check_base(texto[i]):
                    comprobate = cadena + texto[i]
                    if int(comprobate) >= 256:
                        salida.append(cadena)
                        cadena = texto[i]
                    else:
                        cadena += texto[i]
                    if i == len(texto) - 1:
                        salida.append(cadena)
                    comprobate = ''
                elif cadena != '':
                    salida.append(cadena)
                    cadena = ''

        else:  # Base binaria: Comprueba que es un '0' o '1', genera cadenas de longitud 8
            for i in range(len(texto)):
                if (texto[i] == '1' or texto[i] == '0') and len(cadena) < 8:
                    cadena += texto[i]
                    if i == len(texto) - 1:
                        salida.append(int(cadena, 2))
                else:
                    if len(cadena) != 8:
                        cadena = self.fill_zeros(cadena)
                    salida.append(int(cadena, 2))
                    cadena = ''
        return salida

    """
        Funcion: check_base.
        Comprueba si un carcater pertenece a una determinada base
    """

    def check_base(self, palabra, base=10):
        try:
            int(palabra, base)
            return True
        except ValueError:
            return False

    """
        Funcion: fill_K
        Llena la lista 'K' con los valores de la clave
    """

    def fill_K(self, clave):
        salida = []
        j = 0
        for i in range(len(self.S)):
            if j == len(clave) - 1:
                salida.append(clave[j])
                j = 0
            else:
                salida.append(clave[j])
                j += 1
        return salida

    """
        Funcion: inicializar.
        Realiza el algoritmo KSA
    """

    def inicializar(self):
        j = 0
        tam = len(self.clave)
        for i in range(len(self.S)):
            j = (j + self.S[i] + int(self.K[i])) % 256
            self.swap(j, i)

    """
        Funcion: crear_cifrado
        Genera la secuencia cifrante. LLama al método: generar_secuencia
    """

    def crear_cifrado(self):
        for i in range(len(self.mensaje)):
            self.secuencia_cifrante.append(self.generar_secuencia())

    """
        Funcion: generar_secuencia
        Realiza el algoritmo PRGA. Devuelve el valor de cada elemento que compone la secuencia cifrante
    """

    def generar_secuencia(self):
        a = self.a
        b = self.b
        a = (a + 1) % 256
        b = (b + self.S[a]) % 256
        self.set_ab(a, b)
        self.swap(a, b)
        return self.S[(self.S[a] + self.S[b]) % 256]

    """
        Funcion: set_ab
        Asigna valores a las variables de clase 'a' y 'b' utilizadas en el método 'generar_secuencia'
    """

    def set_ab(self, a, b):
        self.a = a
        self.b = b

    """
        Funcion: cifrar_texo
        Pasa el mensaje y la cadena cifrante a binario, luego realiza la operación xor y devuelve la secuencia cifrada.
    """

    def cifrar_texto(self):
        self.convertir_binario(self.mensaje, 10)
        self.convertir_binario(self.secuencia_cifrante, 10)
        for i in range(len(self.mensaje)):
            men = self.mensaje[i]
            sec = self.secuencia_cifrante[i]
            resultado = ''
            for j in range(len(men)):
                if (men[j] == sec[j]):
                    resultado = resultado + '0'
                else:
                    resultado = resultado + '1'
            self.texto_cifrado.append(resultado)

    """
        Funcion: convertir_binario
        Convierte una secuencia en cualquier base a binario
    """

    def convertir_binario(self, texto, base):
        for i in range(len(texto)):
            num = int(str(texto[i]), base)
            bits = bin(num)[2:]
            bits = self.fill_zeros(bits)
            texto[i] = bits
        return texto

    """
        Funcion: convertir_hexadecimal
        Convierte una secuencia en cualquier base a hexadecimal
    """

    def convertir_hexadecimal(self, texto, base):
        for i in range(len(texto)):
            num = int(str(texto[i]), base)
            texto[i] = hex(num).lstrip("0x").rstrip("L")
        return texto

    """
        Funcion: convertir_texto
        Convierte una secuencia en cualquier base a formato texto (ascii)
    """

    def convertir_texto(self, texto, base):
        for i in range(len(texto)):
            num = int(str(texto[i]), base)
            texto[i] = chr(num)
        return texto

    """
        Funcion: convertir_decimal
        Convierte una secuencia en cualquier base a decimal
    """

    def convertir_decimal(self, texto, base):
        for i in range(len(texto)):
            num = int(str(texto[i]), base)
            texto[i] = num
        return texto

    """
        Funcion: fill_zeros
        Añade "leading zeros" a la cadena binaria hasta tener 8 bits
    """

    def fill_zeros(self, bits):
        while len(bits) % 8 != 0:
            bits = '0' + bits
        return bits

    """ 
        Funcion: swap
        Intercambia dos valores dentro del vector de estados
    """

    def swap(self, i, j):
        temp = self.S[i]
        self.S[i] = self.S[j]
        self.S[j] = temp

    """
        Funcion: imprimir_salida
        Imprime el resultado de la ejecución del programa
    """

    def imprimir_salida(self):
        print(f"\n{bc.azul}Salida, base {self.base}:{bc.end}")
        print(
            f"Clave:{bc.BOLD}  {self.clave} {bc.end}")
        print(f"Mensaje de entrada:{bc.BOLD} {self.mensaje} {bc.end}")
        print(
            f"Secuencia cifrante:{bc.BOLD} {self.secuencia_cifrante} {bc.end}")
        print(f"Mensaje de salida:{bc.BOLD} {self.texto_cifrado} {bc.end}\n")
        self.cambiar_base()

    """
        Funcion: imprimir_texto
        Imprime la salida en formato texto
    """

    def imprimir_texto(self):
        print(f"\n{bc.azul}Salida, base Ascii:{bc.end}")
        print(
            f"Clave:{bc.BOLD}  {self.convertir_texto(self.clave, self.base)} {bc.end}")
        print(
            f"Mensaje de entrada:{bc.BOLD} {self.convertir_texto(self.mensaje, self.base)} {bc.end}")
        print(
            f"Secuencia cifrante:{bc.BOLD} {self.convertir_texto(self.secuencia_cifrante, self.base)} {bc.end}")
        print(
            f"Mensaje de salida:{bc.BOLD} {self.convertir_texto(self.texto_cifrado, self.base)} {bc.end}\n")
        self.text_to_decimal()
        self.cambiar_base()

    """
        Funcion: text_to_decimal
        Transforma la salida en ascii a formato decimal
    """

    def text_to_decimal(self):
        for i in range(len(self.clave)):
            self.clave[i] = ord(self.clave[i])
        for i in range(len(self.mensaje)):
            self.mensaje[i] = ord(self.mensaje[i])
        for i in range(len(self.secuencia_cifrante)):
            self.secuencia_cifrante[i] = ord(self.secuencia_cifrante[i])
        for i in range(len(self.texto_cifrado)):
            self.texto_cifrado[i] = ord(self.texto_cifrado[i])
        self.base = 10

    """
        Funcion: cambiar_base
        Realiza el cambio de base en la salida
    """

    def cambiar_base(self):
        print("Imprimir la salida en otra base:")
        print(" 1. Binario \n 2. Decimal \n 3. Hexadecimal \n 4. Ascii \n 5. Salir \n")
        base = input("Seleccione el valor de la base: ")
        if base == '1':
            self.convertir_binario(self.clave, self.base)
            self.convertir_binario(self.mensaje, self.base)
            self.convertir_binario(self.secuencia_cifrante, self.base)
            self.convertir_binario(self.texto_cifrado, self.base)
            self.base = 2
            self.imprimir_salida()
        elif base == '2':
            self.convertir_decimal(self.clave, self.base)
            self.convertir_decimal(self.mensaje, self.base)
            self.convertir_decimal(self.secuencia_cifrante, self.base)
            self.convertir_decimal(self.texto_cifrado, self.base)
            self.base = 10
            self.imprimir_salida()
        elif base == '3':
            self.convertir_hexadecimal(self.clave, self.base)
            self.convertir_hexadecimal(self.mensaje, self.base)
            self.convertir_hexadecimal(self.secuencia_cifrante, self.base)
            self.convertir_hexadecimal(self.texto_cifrado, self.base)
            self.base = 16
            self.imprimir_salida()
        elif base == '4':
            self.imprimir_texto()
        elif base == '5':
            os.system('clear')
            return
        else:
            print(f'{bc.rojo}Opción no válida, seleccione de nuevo una base {bc.end}')
            self.cambiar_base()
