#Создайте класс Fraction, представляющий дробь. Реализуйте магические методы сложения, вычитания, умножения и деления для дробей.

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __add__(self, other):
         new_a = self.a + other.a
         new_b = self.b + other.b

         return Fraction(new_a, new_b,)

    def __add__(self, other):
        if isinstance(other, Fraction): # other == Vector
            return Fraction(self.a + other.a, self.b + other.b)

    def __str__(self):
        return f"Fraction({self.a}, {self.b})"


    def __sub__(self, other):
        if isinstance(other, Fraction):
         return Fraction(self.a - other.a, self.b - other.b)



    def __mul__(self, other):
        if isinstance(other, Fraction):
         return Fraction(self.a * other.a, self.b * other.b)





    def __truediv__(self, other):
        if isinstance(other, Fraction):
         return Fraction(self.a / other.a, self.b / other.b)






fraction1 = Fraction(1.5, 1.5)
fraction2 = Fraction(2, 2)
fraction3 = fraction1 + fraction2
fraction4 = fraction1 - fraction2
fraction5 = fraction1 * fraction2
fraction6 = fraction1 / fraction2
print(fraction3)
print(fraction4)
print(fraction5)
print(fraction6)
