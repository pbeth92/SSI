class FS:
    def __init__(self, p, q, N, s, iter):
        self.p = p
        self.q = q
        self.N = N
        self.s = s
        # Identificación pública de A
        self.v = s*s % N
        self.n_iter = iter
        self.l_iter = []

    def generador(self):
        for ite in range(self.n_iter):
            valores = []
            print(f'Iteración número {ite+1}')

            # Compromiso secreto de A
            x = self.compromiso()
            valores.append(x)

            # Testigo: A envía a B
            valores.append(x*x % self.N)

            # Reto: B envía a A
            e = self.reto()
            valores.append(e)

            # Respuesta: A envía a B
            y = self.respuesta(x, e)
            valores.append(y)

            self.l_iter.append(valores)

    def compromiso(self):
        x = int(input("Valor de x: "))
        while x < 0 and x > self.N:
            print(f'El valor de x debe ser mayor que 0 y menor que {self.N}')
            x = int(input("Valor de x: "))
        return x

    def reto(self):
        e = int(input("Valor de e: "))
        while e > 1 and e < 0:
            print("El valor de e debe ser 0 o 1")
            e = int(input("Valor de e: "))
        return e

    def respuesta(self, x, e):
        if e == 0:
            return(x % self.N)
        else:
            return(x * self.s % self.N)

    def imprimir(self):
        print("\n\n\nEntrada:")
        print(f' p = {self.p}, q = {self.q}')
        print(f' s = {self.s}')
        print(f' i = {self.n_iter}')
        for i in range(self.n_iter):
            print(
                f' Iteración {i+1}: x = {self.l_iter[i][0]}, e = {self.l_iter[i][2]}')

        print("\nSalida: ")
        print(f' N = {self.N}')
        print(f' v = {self.v}')
        # Verficación: B comprueba la información recibida
        for i in range(self.n_iter):
            x = self.l_iter[i][0]
            a = self.l_iter[i][1]
            e = self.l_iter[i][2]
            y = self.l_iter[i][3]

            if e == 0:
                print(
                    f'Iteración {i+1}: a={a}, y={y}, comprobamos que y^2(mod{self.N})={y ** 2 % self.N}  ==  a(mod{self.N})={a % self.N}')
            else:
                print(
                    f'Iteración {i+1}: a={a}, y={y}, comprobamos que y^2(mod{self.N})={y ** 2 % self.N} ==  a*v(mod{self.N})={a*self.v % self.N}')
