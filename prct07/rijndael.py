import operaciones as Ope
from columna import Columna as Col


class Rijndael:
    def __init__(self, texto, clave):
        self.texto_orignal = texto
        self.clave_original = clave
        self.bloque_texto = self.generar_bloque(texto)
        self.bloque_clave = self.generar_bloque(clave)
        self.R_con = self.generar_Rcon()
        self.claves = []
        self.generar_claves(self.bloque_clave)

    def generar_claves(self, bloque_raiz):
        bloque_anterior = bloque_raiz
        for i in range(10):
            bloque_clave = []
            col_0 = self.SubBytes(self.RotWord(bloque_anterior[3]))
            col_0 = bloque_anterior[0] ^ col_0 ^ self.R_con[i]
            bloque_clave.append(col_0)

            for j in range(1, len(bloque_anterior)):
                bloque_clave.append(bloque_anterior[j] ^ bloque_clave[j-1])
            self.claves.append(bloque_clave[:])

            bloque_anterior = bloque_clave

    def RotWord(self, col):
        l_hexa = []
        i = 1
        while i < col.size:
            l_hexa.append(col[i])
            i += 1
        l_hexa.append(col[0])
        r_col = Col(l_hexa)
        return r_col

    def generar_Rcon(self):
        result = []
        val = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36']
        for i in range(10):
            result.append(Col([val[i], '00', '00', '00']))
        return result

    def generar_bloque(self, texto):
        bloque = []
        l_c = []
        j = 0
        for i in range(16):
            l_c.append(texto[i])
            j += 1
            if j == 4:
                bloque.append(Col(l_c[:]))
                l_c.clear()
                j = 0
        return bloque

    def rijndael(self):
        # Iteración inicial:
        print('\nIteración inicial: ')
        print('\nBloque de entrada: ')
        self.print_bloque(self.bloque_texto)
        print('\nBloque de Clave maestra: ')
        self.print_bloque(self.bloque_clave)
        bloque_pri = self.Add_RoundKey(self.bloque_texto, self.bloque_clave)
        print('\n Subclave Inicial: ')
        self.print_bloque(bloque_pri)

        # 9 Iteraciones
        for i in range(9):
            for j in range(len(bloque_pri)):
                self.SubBytes(bloque_pri[j])
            self.ShiftRow(bloque_pri)
            self.MixColumn(bloque_pri)
            bloque_pri = self.Add_RoundKey(bloque_pri, self.claves[i])
            print(f'\n\nIteración R{i+1}:')
            print(f'Subclave {i+1}: ')
            self.print_bloque(self.claves[i])
            print(f'\nResultado iteración {i+1}:')
            self.print_bloque(bloque_pri)

        # Iteración 10
        for j in range(len(bloque_pri)):
            self.SubBytes(bloque_pri[j])
        self.ShiftRow(bloque_pri)
        bloque_pri = self.Add_RoundKey(bloque_pri, self.claves[-1])
        print('\n\nÚltima iteración R10:')
        print(f'Subclave {10}: ')
        self.print_bloque(self.claves[-1])
        print(f'\nResultado última iteración {10}:')
        self.print_bloque(bloque_pri)
        print(f'\nTexto cifrado: {self.print_texto(bloque_pri)}')

    def desencriptar_rijndael(self):
        # Clave 10:
        print('\nIteración inicial: ')
        print('\nBloque cifrado: ')
        self.print_bloque(self.bloque_texto)
        print('\nSubclave 10')
        self.print_bloque(self.claves[-1])
        bloque_pri = self.Add_RoundKey(self.bloque_texto, self.claves[-1])
        self.inverse_ShiftRow(bloque_pri)
        for j in range(len(bloque_pri)):
            self.inverse_SubBytes(bloque_pri[j])
        print('\nResultado primera iteración: ')
        self.print_bloque(bloque_pri)

        # 9 Iteraciones siguientes
        for i in range(8, -1, -1):
            bloque_pri = self.Add_RoundKey(bloque_pri, self.claves[i])
            self.inverse_MixColumn(bloque_pri)
            self.inverse_ShiftRow(bloque_pri)
            for j in range(len(bloque_pri)):
                self.inverse_SubBytes(bloque_pri[j])
            print(f'\n\nIteración R{i+1}:')
            print(f'Subclave {i+1}: ')
            self.print_bloque(self.claves[i])
            print(f'\nResultado iteración {i+1}:')
            self.print_bloque(bloque_pri)

        # Iteración final
        print('\nIteración Final: ')
        bloque_pri = self.Add_RoundKey(bloque_pri, self.bloque_clave)
        print(f'Clave Maestra: ')
        self.print_bloque(self.bloque_clave)
        print(f'\nResultado última iteración {10}:')
        self.print_bloque(bloque_pri)
        print(f'\nTexto descifrado: {self.print_texto(bloque_pri)}')

    def print_bloque(self, bloque):
        for i in range(len(bloque)):
            print(
                f'| {bloque[0][i]} | {bloque[1][i]} | {bloque[2][i]} | {bloque[3][i]} |')

    def print_texto(self, bloque):
        cadena = ''
        for i in range(len(bloque)):
            for j in range(bloque[i].size):
                cadena += bloque[i][j]
        return cadena

    def Add_RoundKey(self, b1, b2):
        r_bloque = []
        for i in range(len(b1)):
            r_bloque.append(b1[i] ^ b2[i])
        return r_bloque

    def SubBytes(self, col):
        for i in range(col.size):
            value = col[i]
            x = int(str(value[0]), 16)
            y = int(str(value[1]), 16)
            col.asignar(i, S_caja[x][y])
        return col

    def ShiftRow(self, bloque):
        for i in range(len(bloque)):
            a = 0
            while a < i:
                aux = bloque[0][i]
                bloque[0].asignar(i, bloque[1][i])
                bloque[1].asignar(i, bloque[2][i])
                bloque[2].asignar(i, bloque[3][i])
                bloque[3].asignar(i, aux)
                a += 1

    def MixColumn(self, bloque):
        for i in range(len(bloque)):
            a = bloque[i][0]
            b = bloque[i][1]
            c = bloque[i][2]
            d = bloque[i][3]

            val_1 = Ope.mul_result([Ope.multiplicar(2, a), Ope.multiplicar(3, b), Ope.transformar(
                Ope.convert_binario(c)), Ope.transformar(Ope.convert_binario(d))])
            bloque[i].asignar(0, Ope.convert_hexa(val_1))

            val_2 = Ope.mul_result([Ope.transformar(Ope.convert_binario(a)), Ope.multiplicar(
                2, b), Ope.multiplicar(3, c), Ope.transformar(Ope.convert_binario(d))])
            bloque[i].asignar(1, Ope.convert_hexa(val_2))

            val_3 = Ope.mul_result([Ope.transformar(Ope.convert_binario(a)), Ope.transformar(
                Ope.convert_binario(b)), Ope.multiplicar(2, c), Ope.multiplicar(3, d)])
            bloque[i].asignar(2, Ope.convert_hexa(val_3))

            val_4 = Ope.mul_result([Ope.multiplicar(3, a), Ope.transformar(Ope.convert_binario(
                b)), Ope.transformar(Ope.convert_binario(c)), Ope.multiplicar(2, d)])
            bloque[i].asignar(3, Ope.convert_hexa(val_4))

    def inverse_SubBytes(self, col):
        for i in range(col.size):
            value = col[i]
            x = int(str(value[0]), 16)
            y = int(str(value[1]), 16)
            col.asignar(i, S_caja_inversa[x][y])
        return col

    def inverse_ShiftRow(self, bloque):
        for i in range(len(bloque)):
            a = 0
            while a < i:
                aux = bloque[3][i]
                bloque[3].asignar(i, bloque[2][i])
                bloque[2].asignar(i, bloque[1][i])
                bloque[1].asignar(i, bloque[0][i])
                bloque[0].asignar(i, aux)
                a += 1

    def inverse_MixColumn(self, bloque):
        for i in range(len(bloque)):
            a = bloque[i][0]
            b = bloque[i][1]
            c = bloque[i][2]
            d = bloque[i][3]

            val_1 = Ope.mul_result(
                [Ope.multiplicar('0e', a), Ope.multiplicar('0b', b), Ope.multiplicar('0d', c), Ope.multiplicar('09', d)])
            bloque[i].asignar(0, Ope.convert_hexa(val_1))

            val_2 = Ope.mul_result(
                [Ope.multiplicar('09', a), Ope.multiplicar('0e', b), Ope.multiplicar('0b', c), Ope.multiplicar('0d', d)])
            bloque[i].asignar(1, Ope.convert_hexa(val_2))

            val_3 = Ope.mul_result(
                [Ope.multiplicar('0d', a), Ope.multiplicar('09', b), Ope.multiplicar('0e', c), Ope.multiplicar('0b', d)])
            bloque[i].asignar(2, Ope.convert_hexa(val_3))

            val_4 = Ope.mul_result(
                [Ope.multiplicar('0b', a), Ope.multiplicar('0d', b), Ope.multiplicar('09', c), Ope.multiplicar('0e', d)])
            bloque[i].asignar(3, Ope.convert_hexa(val_4))


S_caja = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5',
           '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
          ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0',
           'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
          ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc',
           '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
          ['04', 'c7', '23', 'c3', '18', '96', '05', '9a',
           '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
          ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0',
           '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
          ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b',
           '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
          ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85',
           '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
          ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5',
           'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
          ['cd', '0c', '13', 'ec', '5f', '97', '44', '17',
           'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
          ['60', '81', '4f', 'dc', '22', '2a', '90', '88',
           '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
          ['e0', '32', '3a', '0a', '49', '06', '24', '5c',
           'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
          ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9',
           '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
          ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6',
           'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
          ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e',
           '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
          ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94',
           '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
          ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68',
           '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

S_caja_inversa = [['52', '09', '6a', 'd5', '30', '36', 'a5', '38',
                   'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'],
                  ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87',
                   '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb'],
                  ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d',
                   'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'],
                  ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2',
                   '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'],
                  ['72', 'f8', 'f6', '64', '86', '68', '98', '16',
                   'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'],
                  ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da',
                   '5e', '15', '46', '57', 'a7', '8d', '9d', '84'],
                  ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a',
                   'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06'],
                  ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02',
                   'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'],
                  ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea',
                   '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73'],
                  ['96', 'ac', '74', '22', 'e7', 'ad', '35', '85',
                   'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'],
                  ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89',
                   '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b'],
                  ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20',
                   '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'],
                  ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31',
                   'b1', '12', '10', '59', '27', '80', 'ec', '5f'],
                  ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d',
                   '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'],
                  ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0',
                   'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'],
                  ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26',
                   'e1', '69', '14', '63', '55', '21', '0c', '7d']]
