from cmath import inf, log
import math

n = int(input("Enter a number: "))
a = log(2, n)
if a % 1 ==0:
    print(n, " is power of 2.")