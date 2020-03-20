import operaciones as Ope


class Columna:
    def __init__(self, c_lista):
        self.c_lista = c_lista
        self.c_lista_bin = []
        for i in range(4):
            self.c_lista_bin.append(Ope.convert_binario(self.c_lista[i]))
        self.size = len(self.c_lista)

    def __xor__(self, other):
        result = []
        for i in range(4):
            cadena = ''
            for j in range(len(self.c_lista_bin[i])):
                cadena += str(int(self.c_lista_bin[i][j])
                              ^ int(other.c_lista_bin[i][j]))
            result.append(cadena)
        new_col = Columna(Ope.convert_hexa_lista(result))
        return new_col

    def __getitem__(self, v):
        return self.c_lista[v]

    def asignar(self, ind, val):
        self.c_lista[ind] = val
        self.c_lista_bin[ind] = Ope.convert_binario(self.c_lista[ind])
