import os
from bcolors import Bcolors as bc


class Vigenere():
    def __init__(self, mensaje, clave):
        self.alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                         'W', 'X', 'Y', 'Z']
        self.mensaje_original = mensaje.upper()
        self.mensaje = self.format_mensaje(mensaje)
        self.clave = self.format_mensaje(clave).replace(" ", "")
        self.cadena_clave = self.generar_cadena()
        self.mensaje_cod = self.codificar()

    def generar_cadena(self):
        cadena = ''
        j = 0
        for i in range(len(self.mensaje)):
            if self.mensaje[i] != ' ':
                cadena += self.clave[j]
                if j < len(self.clave) - 1:
                    j += 1
                else:
                    j = 0
            else:
                cadena += ' '
        return cadena

    def codificar(self):
        cripto = ''
        for i in range(0, len(self.mensaje)):
            if self.mensaje[i] != ' ':
                a1 = self.get_index(self.mensaje[i])
                a2 = self.get_index(self.cadena_clave[i])
                i_letra = (a1 + a2) % len(self.alfabeto)
                cripto += self.get_letra(i_letra)
            else:
                cripto += ' '
        return cripto

    def descodificar(self):
        descifrado = ''
        for i in range(0, len(self.mensaje)):
            if self.mensaje[i] != ' ':
                a1 = self.get_index(self.mensaje[i])
                a2 = self.get_index(self.cadena_clave[i])
                a3 = (a1 - a2)
                if a3 < 0:
                    a3 = a3 + len(self.alfabeto)
                i_letra = a3 % len(self.alfabeto)
                descifrado += self.get_letra(i_letra)
            else:
                descifrado += ' '
        return descifrado

    def get_index(self, valor):
        return self.alfabeto.index(valor)

    def get_letra(self, valor):
        return self.alfabeto[valor]

    def format_mensaje(self, mensaje):
        men_format = ''
        for simbol in mensaje:
            if simbol.upper() in self.alfabeto:
                men_format += simbol
            elif simbol == ' ':
                men_format += ' '
        return men_format.upper()

    def print_salida(self, config):
        os.system('clear')
        if config == 1:
            print(
                f"Mensaje original: {bc.BOLD} {self.mensaje_original} {bc.end}")
            print(f"Palabra clave:  {bc.BOLD} {self.clave} {bc.end}")
            print(f"Cadena clave:  {bc.BOLD} {self.cadena_clave} {bc.end}")
            print(f"Transformación:  {bc.BOLD} {self.codificar()} {bc.end}")
        else:
            print(f"Mensaje cifrado: {bc.BOLD} {self.mensaje} {bc.end}")
            print(f"Palabra clave:  {bc.BOLD} {self.clave} {bc.end}")
            print(
                f"Mensaje cifrado:  {bc.BOLD} {self.descodificar()} {bc.end} \n")
