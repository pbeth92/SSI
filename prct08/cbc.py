from bloque import Bloque as B
from columna import Columna as COL
from aes import Rijndael as R
import copy

TAM = 16


class CBC:
    def __init__(self, texto, v_ini, clave):
        self.texto = texto
        self.texto_hex = self.crear_lista(texto)
        self.size = len(self.texto_hex)
        self.bloques = self.crear_bloques(self.texto_hex)
        self.clave = B(self.crear_lista(clave))
        self.v_inicializador = B(self.crear_lista(v_ini))
        self.bloques_cifrados = []
        self.bloques_desc = []

    def crear_bloques(self, lista):
        l_bloques = []
        i = 0
        while (i < self.size):
            b_valores = []
            if (self.size - i) < TAM:
                for ind in range(i, self.size):
                    b_valores.append(lista[ind])
            else:
                j = 0
                while j < TAM:
                    b_valores.append(lista[i+j])
                    j += 1
            bloque = B(b_valores)
            l_bloques.append(bloque)
            i += TAM
        return l_bloques

    def cifrar_cbc(self):
        print("\n\nEntrada: ")
        print("Clave: ")
        self.clave.imprimir()
        print("Vector de inicialización: ")
        self.v_inicializador.imprimir()
        for i in range(len(self.bloques)):
            print(f"Bloque {i} de texto original:")
            self.bloques[i].imprimir()

        bloque_r = self.bloques[0] ^ self.v_inicializador
        cifr = R(bloque_r, self.clave)
        self.bloques_cifrados.append(cifr.rijndael())

        for i in range(1, len(self.bloques)):
            if self.bloques[i].n_campos == TAM:
                # Operación Xor
                bloque_r = self.bloques[i] ^ self.bloques_cifrados[i-1]
                # Cifrado con la clave
                cifr = R(bloque_r, self.clave)
                self.bloques_cifrados.append(cifr.rijndael())
            else:
                # Copia del bloque cifrado anterior
                bloque_c = copy.deepcopy(self.bloques_cifrados[i-1])
                # Se llama al método cipher_stealing
                self.cipher_stealing(i)
                # Se realiza el cifrado
                cifr = R(bloque_c, self.clave)

                # Se intercambian las posiciones
                aux = self.bloques_cifrados.pop()
                self.bloques_cifrados.append(cifr.rijndael())
                self.bloques_cifrados.append(aux)

        print("\n\nBloques cifrados:")
        for i in range(len(self.bloques_cifrados)):
            print(f"Bloque {i} de texto cifrado:")
            self.bloques_cifrados[i].imprimir()

    def descifrar_cbc(self):
        print("\n\nEntrada: ")
        print("Clave: ")
        self.clave.imprimir()
        print("Vector de inicialización: ")
        self.v_inicializador.imprimir()
        for i in range(len(self.bloques)):
            print(f"Bloque {i} de texto cifrado:")
            self.bloques[i].imprimir()

        for i in range(0, len(self.bloques)):
            if i == 0:
                bloque_xor = self.v_inicializador
            else:
                bloque_xor = self.bloques[i-1]

            cifr = R(self.bloques[i], self.clave)
            bloque_r = cifr.desencriptar_rijndael()
            bloque_r = bloque_xor ^ bloque_r
            self.bloques_desc.append(bloque_r)

        print("\n\nBloques Originales:")
        for i in range(len(self.bloques_desc)):
            print(f"Bloque {i} de texto original:")
            self.bloques_desc[i].imprimir()

    def cipher_stealing(self, ind):
        l = 0
        i = self.bloques[ind].n_campos
        while i < TAM:
            # Buscamos la columna correspondiente del bloque cifrado anterior
            j = self.bloques[ind].size - 1
            if i % 4 == 0:
                # Creamos un nuevo objeto columna y lo añadimos al último bloque
                column = COL(self.bloques_cifrados[ind-1][j].c_lista)
                self.bloques[ind].bloque.append(column)
                self.bloques[ind].size += 1
                self.bloques[ind].n_campos += 4
                # Eliminamos esa columna del bloque anterior
                del self.bloques_cifrados[ind - 1].bloque[j]
                self.bloques_cifrados[ind - 1].size -= 1
                i += 4
            else:
                k = i % 4
                self.bloques[ind][j].c_lista.append(
                    self.bloques_cifrados[ind-1][j].c_lista[k-l])
                self.bloques[ind][j].c_lista_bin.append(
                    self.bloques_cifrados[ind-1][j].c_lista_bin[k-l])
                self.bloques[ind][j].size += 1
                self.bloques[ind].n_campos += 1

                del self.bloques_cifrados[ind - 1].bloque[j].c_lista[k-l]
                del self.bloques_cifrados[ind - 1].bloque[j].c_lista_bin[k-l]
                self.bloques_cifrados[ind-1][j].size -= 1
                l += 1
                i += 1

    def crear_lista(self, cadena):
        h_lista = []
        c_hexa = ''
        cont = 0
        for i in range(len(cadena)):
            if cont == 2 or cadena[i] == ' ':
                h_lista.append(c_hexa)
                cont = 0
                c_hexa = ''
            elif i == len(cadena) - 1:
                c_hexa += cadena[i]
                h_lista.append(c_hexa)
            else:
                c_hexa += cadena[i]
                cont += 1
        return h_lista
