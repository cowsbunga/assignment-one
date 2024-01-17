import numpy as np
import matplotlib.pyplot as plt
import math

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
n1 = first
n2 =  second
i = 0

while True:
    n_next = (n1 + n2) % 10
    n1 = n2
    n2 = n_next
    i += 1
    if n1 == first and n2 == second:
        break

print("length: ", i)