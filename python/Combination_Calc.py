#Combination

import math

def comb_atleast(n, x):
    comb_sum = 0
    for r in range(x,n + 1):
        comb = math.factorial(n)/(math.factorial(n-r)* math.factorial(r))
        comb_sum += comb

    return comb_sum




choose_from = int(input("Please enter total number to choose from:"))
start = int(input("At least how many?:"))
print(comb_atleast(choose_from, start))

