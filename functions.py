from math import sqrt


# functions
def pythag(a, b):
    c = sqrt(a * a + b * b)
    return c

# main
print('What is the length of side a')
a = int(input())
print('What is the length of side b')
b = int(input())
c = pythag(a, b)
print(c)