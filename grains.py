"""
Ejercicio basado en el cuento del campesino que le enseñó a jugar ajedrez al rey
"""

def square(number):
    return 2**(number-1) 


def total(number):
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    total = 0
    for i in range(0, number + 1): 
        total = total + square(i)
    return round(total)


print(square(4))

print(total(4))

print(total(0))