import itertools
import numpy as np
import pytest
from complexPackage import ComplexNumber

# Generate all testcases using metafunc. Sweep a, b from -1 to 5 in a + bi. This is more to display testing structure

def pytest_generate_tests(metafunc):

    complexReal = list(range(-1, 5))
    complexImag = list(range(-1, 5))

    # Permute possible inputs to generate test dataset
    Testcases = list(itertools.product(complexReal, complexImag,complexReal, complexImag))
    metafunc.parametrize("Testcases", Testcases)

# Test all functions one by one, limit number of asserts to ensure efficient error catching
def test_complex_number_addition(Testcases):
    a = ComplexNumber.ComplexNumber(Testcases[0], Testcases[1])
    b = ComplexNumber.ComplexNumber(Testcases[2], Testcases[3])

    c = a + b
    assert c.real == Testcases[0] + Testcases[2]
    assert c.imag == Testcases[1] + Testcases[3]

def test_complex_number_substraction(Testcases):
    a = ComplexNumber.ComplexNumber(Testcases[0], Testcases[1])
    b = ComplexNumber.ComplexNumber(Testcases[2], Testcases[3])

    c = a - b
    assert c.real == Testcases[0] - Testcases[2]
    assert c.imag == Testcases[1] - Testcases[3]

def test_complex_number_multiplication(Testcases):
    a = ComplexNumber.ComplexNumber(Testcases[0], Testcases[1])
    b = ComplexNumber.ComplexNumber(Testcases[2], Testcases[3])

    c = a * b

    assert c.real == ((Testcases[0] + Testcases[1]*1j)*(Testcases[2] + Testcases[3]*1j)).real
    assert c.imag == ((Testcases[0] + Testcases[1] * 1j) * (Testcases[2] + Testcases[3] * 1j)).imag
#
def test_complex_number_devision(Testcases):

    a = ComplexNumber.ComplexNumber(Testcases[0], Testcases[1])
    b = ComplexNumber.ComplexNumber(Testcases[2], Testcases[3])

    if Testcases[2] and Testcases[3]:
        c = a / b

        # Building your own devision is a bit tricky to get the significance right
        assert c.real == pytest.approx(((Testcases[0] + Testcases[1] * 1j) / (Testcases[2] + Testcases[3] * 1j)).real,0.1)
        assert c.imag == pytest.approx(((Testcases[0] + Testcases[1] * 1j) / (Testcases[2] + Testcases[3] * 1j)).imag, 0.1)
    else:
        return

def test_complex_number_abs(Testcases):
    a = ComplexNumber.ComplexNumber(Testcases[0], Testcases[1])
    b = ComplexNumber.ComplexNumber(Testcases[2], Testcases[3])

    assert abs(a) == abs(Testcases[0] + Testcases[1] * 1j)
    assert abs(b) == abs(Testcases[2] + Testcases[3] * 1j)

def test_complex_number_angle(Testcases):
    a = ComplexNumber.ComplexNumber(Testcases[0], Testcases[1])
    b = ComplexNumber.ComplexNumber(Testcases[2], Testcases[3])

    assert a.angle() == np.angle(Testcases[0] + Testcases[1] * 1j)
    assert b.angle() == np.angle(Testcases[2] + Testcases[3] * 1j)

def test_complex_number_cart2Polar(Testcases):
    a = ComplexNumber.ComplexNumber(Testcases[0], Testcases[1])
    b = ComplexNumber.ComplexNumber(Testcases[2], Testcases[3])

    mag, pha = a.cart2Polar()

    assert mag == abs(Testcases[0] + 1j*Testcases[1])
    assert pha == np.angle(Testcases[0] + 1j*Testcases[1])

# To Do:
# More edge case testing, special corners like approx infinity.