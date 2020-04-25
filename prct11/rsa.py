import random


class RSA:
    def __init__(self, mensaje):
        self.mensaje_orignal = mensaje
        self.p = self.get_primo("p")
        self.q = self.get_primo("q")
        self.n = self.p*self.q
        self.fi_n = (self.p-1)*(self.q-1)
        self.e, self.d = self.get_e()
        self.tam_bloque = self.get_tam()

    def get_primo(self, num):
        num_p = int(
            input(f"\nInformación privada: Introduzca el número primo {num}: "))
        while self.primalidad(num_p) == False:
            print("\np debe ser un número primo.")
            num_p = int(input(f"Introduzca un nuevo valor para {num}: "))
        return num_p

    def exp_rapida(self, y, b, mod):
        x = 1
        while (b > 0):
            if (b % 2 != 0):
                x = (x * y) % mod
                b = b - 1
            else:
                y = (y*y) % mod
                b = int(b/2)
        return x

    def primalidad(self, val):
        l_enteros = list(range(1, val))
        primo = True

        while primo and len(l_enteros) > 0:
            a = random.choice(l_enteros)
            l_enteros.remove(a)
            result = self.exp_rapida(a, (val-1)/2, val)
            if (result != 1) and (result != val - 1):
                primo = False

        return primo

    def get_e(self):
        d = int(input("\n Introduzca un valor para d: "))
        e, mcd = self.euclides_extend(d, self.fi_n)
        while mcd != 1:
            print(
                f'\n Error: d:{d} no es primo respecto de \u03C6(n){self.fi_n}.')
            d = int(input("Introduzca un nuevo valor para d: "))
            e, mcd = self.euclides_extend(d, self.fi_n)
        if e < 0:
            e = self.fi_n + e
        return e, d

    def euclides_extend(self, a, b):
        X = [a, b]
        Z = [1, 0]
        i = 1
        self.inicio_traza(a)

        while X[i] != 0:
            resto = X[i-1] % X[i]
            div = int(X[i-1]/X[i])
            z = -div * Z[i] + Z[i-1]

            if resto != 0:
                print(f'\t {i} \t {X[i]} \t {z}')
            else:
                print(f'\t {i} \t {X[i]} \t')

            X.append(resto)
            Z.append(z)
            i += 1

        return Z[i-1], X[i-1]

    def inicio_traza(self, val):
        print("\nTraza: ")
        print('\t i \t Xi \t Zi \n')
        print(f'\t-1 \t   \t 0')
        print(f'\t 0 \t {val} \t 1')

    def get_tam(self):
        j = 1
        while pow(len(alfabeto), j) < self.n:
            j += 1
        return j - 1

    def cifrar_mensaje(self):
        self.cod_numerica()
        self.cifrar_num = []
        for val in self.cod_num:
            res = self.exp_rapida(val, self.e, self.n)
            self.cifrar_num.append(res)

    def cod_numerica(self):
        self.cod_num = []
        bloque = []
        cont = 0
        for i in range(len(self.mensaje_orignal)):
            if self.mensaje_orignal[i] != ' ':
                bloque.append(self.mensaje_orignal[i])
                cont += 1
                if cont == self.tam_bloque:
                    result = 0
                    for i in range(len(bloque)):
                        result += alfabeto.index(bloque[i].upper()) * \
                            pow(len(alfabeto), cont-1)
                        cont -= 1
                    self.cod_num.append(result)
                    bloque.clear()
        return self.cod_num

    def descifrar(self):
        result = []
        mensaje_li = list(self.mensaje_orignal.split(" "))
        for val in mensaje_li:
            res = self.exp_rapida(int(val), self.d, self.n)
            result.append(res)
        print(result)

    def imprimir(self):
        print(f"Salida: \nValor de p: {self.p} \nValor de q: {self.q}")
        print(f"Valor de n:  {self.n}")
        print(f"Valor de \u03C6(n): {self.fi_n}")
        print(f"Valor de d: {self.d} \nValor de e: {self.e}")
        print(f"Codificación numérica: {self.cod_num}")
        print(f"Cifrado: {self.cifrar_num}")


alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
