class DH:
    def __init__(self, p, a, Xa, Xb):
        self.p = p
        self.a = a
        self.XA = Xa
        self.XB = Xb
        self.YA = None
        self.YB = None
        self.k = None

    def generar_clave(self):
        print(f'\nTraza para YA = {self.a}^{self.XA}(mod{self.p}): \n')
        self.YA = self.exp_rapida(self.XA, self.a)
        print(f'\nTraza para YB = {self.a}^{self.XB}(mod{self.p}): \n')
        self.YB = self.exp_rapida(self.XB, self.a)

        print(f'\nTraza para k con = {self.XA}^{self.YB}(mod{self.p}): \n')
        k1 = self.exp_rapida(self.XA, self.YB)
        print(f'\nTraza para k con = {self.XB}^{self.YA}(mod{self.p}): \n')
        k2 = self.exp_rapida(self.XB, self.YA)

        if k1 == k2:
            self.k = k1
        else:
            print('Error: Los valores k no coinciden: ')
            print(f'Valor de k1: {k1}')
            print(f'Valor de k1: {k2}')

    def exp_rapida(self, b, y):
        x = 1
        print('\t y \t b \t x \n')
        while (b > 0) and (y > 1):
            if (b % 2 != 0):
                x = (x * y) % self.p
                b = b - 1
                print(f'\t  \t{b} \t {x}')
            else:
                y = (y*y) % self.p
                b = int(b/2)
                print(f'\t{y}  \t{b}')
        return x

    def imprimir(self):
        print('\nResultados: ')
        print(f' p: {self.p}')
        print(f' \u03B1: {self.a}')
        print(f' XA: {self.XA}')
        print(f' XB: {self.XB}')
        print(f' YA: {self.YA}')
        print(f' YB: {self.YB}')
        print(f' k: {self.k}')
