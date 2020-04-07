class Columna:
    def __init__(self, c_lista=0):
        if c_lista != 0:
            self.c_lista = c_lista
        else:
            self.c_lista = ['00', '00', '00', '00']
        self.c_lista_bin = self.convert_binario(self.c_lista)
        self.size = len(self.c_lista)

    def __getitem__(self, ind):
        return self.c_lista[ind]

    def get_bin(self, ind):
        return self.c_lista_bin[ind]

    def __setitem__(self, ind, val):
        self.c_lista[ind] = val
        self.c_lista_bin[ind] = self.valor_binario(val)

    def __xor__(self, other):
        result = []
        for i in range(self.size):
            cadena = ''
            for j in range(len(self.c_lista_bin[i])):
                cadena += str(int(self.c_lista_bin[i][j])
                              ^ int(other.c_lista_bin[i][j]))
            result.append(self.convert_hexa(cadena))
        new_col = Columna(result)
        return new_col

    def convert_binario(self, lista, base=16):
        l_bin = []
        for i in range(len(lista)):
            num = int(str(lista[i]), base)
            bits = bin(num)[2:]
            bits = self.fill_zeros(bits)
            l_bin.append(bits)
        return l_bin

    def valor_binario(self, val):
        num = int(str(val), 16)
        bits = bin(num)[2:]
        bits = self.fill_zeros(bits)
        return bits

    def fill_zeros(self, bits):
        while len(bits) % 8 != 0:
            bits = '0' + bits
        return bits

    def convert_hexa(self, l_val, base=2):
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

    def imprimir_valor(self, ind):
        if ind < self.size:
            return(self.c_lista[ind])
        else:
            return "--"

    def imprimir(self):
        print(self.c_lista)
