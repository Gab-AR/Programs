class Fraction:
    def __init__(self, w_num, w_den):
        self.num = w_num
        self.den = w_den
    
    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def show(self):
        print(self.num,'/', self.den)

    def __str__(self) -> str:
        return "Fracao: "+str(self.num)+"/"+str(self.den)
    
    def simplificar(self):
        def mdc(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        divisor_comum = mdc(self.num, self.den)
        self.num //= divisor_comum
        self.den //= divisor_comum

    def __add__(self, outro):
        new_num = self.num * outro.den + self.den * outro.num
        new_den = self.den * outro.den
        resultado = Fraction(new_num, new_den)
        resultado.simplificar()
        return resultado
    
    def __sub__(self, outro):
        new_num = self.num * outro.den - self.den * outro.num
        new_den = self.den * outro.den
        resultado = Fraction(new_num, new_den)
        resultado.simplificar()
        return resultado
    
    def __mul__(self, outro):
        new_num = self.num * outro.num
        new_den = self.den * outro.den
        resultado = Fraction(new_num, new_den)
        resultado.simplificar()
        return resultado
    
    def __truediv__(self, outro):
        new_num = self.num * outro.den
        new_den = self.den * outro.num
        resultado = Fraction(new_num, new_den)
        resultado.simplificar()
        return resultado
    
    def __gt__(self, outro):
        valor1 = self.num / self.den
        valor2 = outro.num / outro.den
        return valor1 > valor2
        
    def __ge__(self, outro):
        valor1 = self.num / self.den
        valor2 = outro.num / outro.den
        return valor1 >= valor2
    
    def __lt__(self, outro):
        valor1 = self.num / self.den
        valor2 = outro.num / outro.den
        return valor1 < valor2
    
    def __le__(self, outro):
        valor1 = self.num / self.den
        valor2 = outro.num / outro.den
        return valor1 <= valor2
    
    def __eq__(self, outro):
        valor1 = self.num / self.den
        valor2 = outro.num / outro.den
        return valor1 == valor2
    
    def __ne__(self, outro):
        valor1 = self.num / self.den
        valor2 = outro.num / outro.den
        return valor1 != valor2


if __name__== '__main__':
    f1 = Fraction(7,3)
    f2 = Fraction(4,6)
    print(f1)
    print("Numerador:", f1.getNum())
    print("Denominador:", f1.getDen())
    print("f1 + f2:", f1 + f2)
    print("f1/f2:", f1/f2)
    print("f1 > f2:", f1 > f2)
    print("f1 == f2:", f1 == f2)
