import sympy

n=int(input())
if sympy.isprime(n):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")