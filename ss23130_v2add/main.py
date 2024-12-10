# This is a simple calculation program
# created to demonstrate version control.
from libadd import *
from libmult import *
a = 13
b = 5
print(plus(a,b))
print(plusx(a,b,2))
print(mult(a,b))

def add_numbers(a, b):
    """
    Funkcija, kas saskaita divus skaitļus.
    """
    return a + b

# Piemērs, kā izmantot funkciju
if __name__ == "__main__":
    print("Saskaitīšanas rezultāts:", add_numbers(5, 3))
