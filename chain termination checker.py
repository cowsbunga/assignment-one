import numpy as np
import matplotlib.pyplot as plt
import math

n = int(input("Enter number of attempts:"))

for i in range(0, 10):
    for j in range(0, 10):
        k=0 
        n1 = i
        n2 = j
        while k < n:
            n_next = (n1 + n2) % 10
            n1 = n2
            n2 = n_next
            if n1 == i and n2 == j:
                print(i, ", ", j, ": success")
                break
            k += 1
        if k == n:
            print(i, ", ", j, ": failure")

