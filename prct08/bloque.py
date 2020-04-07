from columna import Columna as COL


class Bloque():
    def __init__(self, l_bytes=0):
        if l_bytes == 0:
            self.bloque = self.inicializar_0()
        else:
            self.bloque = self.generar_bloque(l_bytes)
        self.size = len(self.bloque)
        self.n_campos = self.tam_bloques()

    def __getitem__(self, ind):
        return self.bloque[ind]

    def __setitem__(self, idn, val):
        self.bloque[idn] = val

    def __xor__(self, other):
        result = []
        for i in range(self.size):
            columna = self.bloque[i] ^ other.bloque[i]
            for val in columna.c_lista:
                result.append(val)
        new_bloque = Bloque(result)
        return new_bloque

    def inicializar_0(self):
        bloque = []
        for i in range(4):
            column = COL(0)
            bloque.append(column)
        return bloque

    def generar_bloque(self, l_bytes):
        bloque = []
        tam = len(l_bytes)
        i = 0
        while (i < tam):
            c_valores = []
            if (tam - i) < 4:
                for ind in range(i, tam):
                    c_valores.append(l_bytes[ind])
            else:
                j = 0
                while j < 4:
                    c_valores.append(l_bytes[i+j])
                    j += 1

            column = COL(c_valores)
            bloque.append(column)
            i += 4

        return bloque

    def tam_bloques(self):
        cont = 0
        for i in range(self.size):
            cont += self.bloque[i].size
        return cont

    def imprimir(self):
        bloque_impreso = []
        for i in range(4):
            fila = ''
            fila += '|'
            for col in self.bloque:
                fila += col.imprimir_valor(i)
                fila += '|'
            bloque_impreso.append(fila)

        for fila in bloque_impreso:
            print(fila)
