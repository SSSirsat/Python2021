import math
pi = math.pi

def circle(radius):
    return pi * (radius ** 2)
def cube(side):
    return 6 * side * side
def cylinder(radius, height):
    return 2*pi *radius + 2*pi*height
def sphere(radius):
    return 2 * pi * (radius ** 2)
print(circle(45))
print(cube(33))
print(cylinder(34,55))
print(sphere(66))
