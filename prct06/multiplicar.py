class Multiplicar():
    def __init__(self, a1, a2, alg):
        if self.check_bin(a1):
            self.b1 = a1
            self.b2 = a2
        else:
            self.b1 = self.convertir_binario(a1)
            self.b2 = self.convertir_binario(a2)
            print(self.b1)
            print(self.b2)
        self.a1 = self.transformar(self.b1)
        self.a2 = self.transformar(self.b2)
        if alg == 1:
            self.m = [0, 0, 0, 1, 1, 0, 1, 1]
        else:
            self.m = [1, 0, 1, 0, 1, 0, 0, 1]
        self.resultado = []

    def check_bin(self, cadena, base=2):
        try:
            int(cadena, 2)
            return True
        except ValueError:
            return False

    def convertir_binario(self, num):
        num = int(num, 16)
        bits = bin(num)[2:]
        result = self.fill_zeros(bits)
        return result

    def fill_zeros(self, bits):
        while len(bits) % 8 != 0:
            bits = '0' + bits
        return bits

    """
        Función transformar.
        Covierte la cadena a una lista de enteros
    """

    def transformar(self, cadena):
        lista = []
        for i in range(len(cadena)):
            lista.append(int(cadena[i]))
        return lista

    """
        Función multiplicacion.
        Realiza la multiplicación de bits
    """

    def multiplicacion(self):
        mv = self.a1
        s_resul = []
        b_sale = 0
        for i in reversed(range(8)):
            if b_sale == 1:
                self.operar(mv)
            if self.a2[i] == 1:
                s_resul.append(mv[:])
            b_sale = self.desplazar(mv)
        self.result(s_resul)

    """
        Función desplazar
        desplaza los bits
    """

    def desplazar(self, lista):
        r = lista.pop(0)
        lista.append(0)
        return r

    """
        Función operar
        Realiza la operación de suma xor con el byte 'M' cuando se desplaza un '1'
    """

    def operar(self, lista):
        for i in range(len(lista)):
            lista[i] = lista[i] ^ self.m[i]

    """
        Función result
        Suma los valores para obtener el resultado
    """

    def result(self, lista):
        if len(lista) == 0:
            self.resultado = [0, 0, 0, 0, 0, 0, 0, 0]
        else:
            i = 1
            self.resultado = lista[0]
            while i < len(lista):
                self.resultado = self.suma_xor(self.resultado, lista[i])
                i += 1

    def suma_xor(self, l1, l2):
        for i in range(len(l1)):
            l1[i] = l1[i] ^ l2[i]
        return l1

    def imprimir(self):
        print('\nSalida:')
        print(f'Primer byte: {self.b1}')
        print(f'Segundo byte: {self.b2}')
        print(f"Byte algoritmo: {''.join(map(str, self.m))}")
        print(f"Multiplicación: {''.join(map(str, self.resultado))}")
