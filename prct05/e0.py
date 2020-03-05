class E0():
    def __init__(self, semilla, mensaje=''):
        self.semilla = semilla
        self.reg1 = self.crear_lista(0, 25)
        self.reg2 = self.crear_lista(25, 56)
        self.reg3 = self.crear_lista(56, 89)
        self.reg4 = self.crear_lista(89, 128)
        if mensaje:
            self.mensaje = mensaje
            self.mensaje_bin = self.mensaje_a_binario(mensaje)
        else:
            self.mensaje_bin = input(
                "Introduzca el mensaje cifrado en binario: ")
        self.R1_s = self.inicializar()
        self.clave = ''
        self.cifrado = ''

    def crear_lista(self, ini, fin):
        l_result = []
        while ini < fin:
            l_result.append(int(self.semilla[ini]))
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

    def generador(self):
        ct = [self.R1_s[1], self.R1_s[0]]
        result = self.R1_s
        i = 0

        while i < len(self.mensaje_bin):
            self.realimentacion()
            x = [self.reg1.pop(), self.reg2.pop(),
                 self.reg3.pop(), self.reg4.pop()]
            R1 = ct
            R2 = result
            T1 = R1
            T2 = [R2[1], R2[1] ^ R2[0]]
            Z = self.get_z(ct, x)

            result = [Z[0] ^ T2[0] ^ T1[0], Z[1] ^ T2[1] ^ T1[1]]

            self.clave = self.clave + str(x[0] ^ x[1] ^ x[2] ^ x[3] ^ ct[1])
            ct = [result[1], result[0]]
            if __debug__:
                self.print_traza(x, R1, R2, T1, T2, Z,
                                 result, ct, self.clave[i])
            i += 1

    def inicializar(self):
        print('Semilla de R1:\n1. 00 \n2. 01 \n3. 10 \n4. 11')
        opc = input('Opción: ')
        if opc == '1':
            return [0, 0]
        elif opc == '2':
            return [0, 1]
        elif opc == '3':
            return [1, 0]
        else:
            return [1, 1]

    def realimentacion(self):
        val_1 = self.reg1[7] ^ self.reg1[11] ^ self.reg1[19] ^ self.reg1[24]
        self.reg1.insert(0, val_1)
        val_2 = self.reg2[11] ^ self.reg2[15] ^ self.reg2[23] ^ self.reg2[30]
        self.reg2.insert(0, val_2)
        val_3 = self.reg3[3] ^ self.reg3[23] ^ self.reg3[27] ^ self.reg3[32]
        self.reg3.insert(0, val_3)
        val_4 = self.reg4[3] ^ self.reg4[27] ^ self.reg4[35] ^ self.reg4[38]
        self.reg4.insert(0, val_4)

    def get_z(self, ct, x):
        ct_int = int(''.join(map(str, ct)), 2)
        yt = x[0] + x[1] + x[2] + x[3]
        r = int((yt + ct_int) / 2)
        if r == 0:
            return [0, 0]
        elif r == 1:
            return [0, 1]
        elif r == 2:
            return [1, 0]
        else:
            return [1, 1]

    def cifrar(self):
        i = 0
        result = 0
        while i < len(self.mensaje_bin):
            result = int(self.mensaje_bin[i]) ^ int(self.clave[i])
            self.cifrado = self.cifrado + str(result)
            i += 1

    def print_traza(self, x, R1, R2, T1, T2, Z, result, ct, bit):
        print("\nTraza:")
        print(f"LFSR1: {x[0]}, LFSR2: {x[1]}, LFSR3: {x[2]}, LFSR4: {x[3]}")
        print(f"R1: {R1}")
        print(f"R2: {R2}")
        print(f"T1: {T1}")
        print(f"T2: {T2}")
        print(f"Z: {Z}")
        print(f"result: {result}")
        print(f"ct: {ct}")
        print(f"bit: {bit}")

    def imprimir_c(self):
        print("\nSalida:")
        print(f"Mensaje a cifrar: {self.mensaje}")
        print(f"Mensaje a cifrar en binario: {self.mensaje_bin}")
        print(f"Semilla utilizada: {self.semilla}")
        print(f"Semilla de R1: {self.R1_s}")
        print(f"Clave generada: {self.clave}")
        print(
            f"Mensaje cifrado en binario: {self.cifrado}")

    def imprimir_d(self):
        print("\nSalida:")
        print(f"Mensaje cifrado en binario: {self.mensaje_bin}")
        print(f"Semilla utilizada: {self.semilla}")
        print(f"Clave generada: {self.clave}")
        print(f"Mensaje descifrado: {self.binario_a_mensaje(self.cifrado)}")
