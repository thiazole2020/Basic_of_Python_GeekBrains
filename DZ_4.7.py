import math

def some_factorial(n = 0):
    for i in range(1, n+1):
        yield math.factorial(i)

for i in some_factorial(15):
    print(i)