import numpy as np

# Generate Complex number class, override native buildins to fit complex calculations
class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumber((self.real*other.real - self.imag*other.imag), (self.real*other.imag + self.imag*other.real))

    def __truediv__(self, other):
        # Ensure that we are not dividing by 0
        if other.real and other.imag:
            real = (self.real*other.real + self.imag*other.imag)/(other.real**2 + other.imag**2)
            imag = (self.imag * other.real - self.real * other.imag) / (other.real ** 2 + other.imag ** 2)
            return ComplexNumber(real, imag)
        else:
            return

    def __abs__(self):
        return (self.imag **2 + self.real**2)**0.5

    def __str__(self):
        return f'{self.real} + {self.imag}i'

    # Take arctan2 as numpy complex devision also uses the arctan2
    def angle(self):
        return np.arctan2(self.imag,self.real)

    def cart2Polar(self):
        return abs(self), self.angle()


# To be Implemented: Full support for polar form



