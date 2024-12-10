# This is a simple calculation program
# created to demonstrate version control.
from libadd import *
from libmult import *
a = 13
b = 5
print(plus(a,b))
print(mult(a,b))
print(multx(a,b,2))

def multiply_numbers(a, b):
    """
    Funkcija, kas sareizina divus skaitļus.
    """
    return a * b

# Piemērs, kā izmantot funkciju
if __name__ == "__main__":
    print("Reizināšanas rezultāts:", multiply_numbers(4, 6))
