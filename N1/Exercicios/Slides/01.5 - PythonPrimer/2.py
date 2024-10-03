"""
Escreva uma função em Python que receba um inteiro positivo n 
e retorne a soma dos quadrados de todos os inteiros positivos menores do que n.
"""

from functools import reduce
from operator import add

def square_sum(n: int) -> int:
    return reduce(add, map(lambda x: x*x, range(n)))

if __name__ == "__main__":
    print(square_sum(5))
