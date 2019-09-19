#Permutation
import math

def perm_atleast(n, x):
    permutated_sum = 0
    for r in range(x,n + 1):
        permutated = math.factorial(n)/math.factorial(n-r)
        permutated_sum += permutated

    return permutated_sum




choose_from = int(input("Please enter total number to choose from:"))
start = int(input("At least how many?:"))
print(perm_atleast(choose_from, start))

