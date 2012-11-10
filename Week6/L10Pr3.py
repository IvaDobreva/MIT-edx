""" L10 Problem 3 : 5.0 points

Write a boolean function isPrime(n) that returns True if the positive integer n is a prime number, and False otherwise. The function should raise a TypeError if n isn't an integer (i.e., an instance of int) and a ValueError if n is an integer less than or equal to zero.
"""

def isPrime(n):
    counter = 0
    if type(n) != int:
        raise TypeError()
    if n < 0:
        raise ValueError()
    if n == 0 or n == 1:
        return False
    for c in range(2, n+1):
        if n%c == 0:
            break
    if c == n:
        return True
    else:
        return False
     
