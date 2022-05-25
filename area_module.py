from cmath import pi


def houseArea():
    length = input("please state the length: ")
    width = input("please state the width: ")
    area = int(length) * int(width)

    return area

houseArea()

def circOfCircle():
    diameter = input("please state the diamter of the circle: ")
    circumference = int(diameter) * 3.141

    return circumference