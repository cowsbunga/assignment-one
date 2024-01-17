# given 2 numbers n1 and n2, calculates the number bracelet they give
#stops when the chain starts reapeating, or when the 102nd element of the chain is reached, to prevent breaking if the chain is infinite

import numpy as np
import matplotlib.pyplot as plt
import math

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
n1 = first
n2 =  second
print(n1)
print(n2)
i = 0



while i<100:
    n_next = (n1 + n2) % 10
    print(n_next)
    n1 = n2
    n2 = n_next
    if n1 == first and n2 == second:
        break
    i += 1
