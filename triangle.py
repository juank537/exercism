def is_triangle(sides):
    if len(sides) == 3 and ((sides[0] > 0) and (sides[1] > 0) and (sides[2] > 0)) :
        return ((sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[0] + sides[2] >= sides[1]))
    return False


def equilateral(sides):
    return is_triangle(sides) and (sides[0] == sides[1] == sides[2])


def isosceles(sides):
    return is_triangle(sides) and ((sides[0] == sides[1]) or (sides[1] == sides[2]) or (sides[0] == sides[2]))


def scalene(sides):
    return is_triangle(sides) and not equilateral(sides) and not isosceles(sides)


print(equilateral([2,2,2]))
print(equilateral([0,0,0]))
print(equilateral([2,1,2]))
print(isosceles([2,1,2]))
print(isosceles([4,2,5]))
print(scalene([2,1,3]))
print(scalene([2,1,2]))
