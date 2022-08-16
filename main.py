from math import sin, radians, sqrt
import sys


def sind(angle):
    rad = radians(angle)
    val = sin(rad)
    return val


def rounding_4(num):
    rounder = 4
    count = 2
    if num < 1:
        dec_digits = len(str(num)) - 2
        while count < dec_digits:
            if str(num)[count] == '0':
                rounder = rounder + 1
            else:
                count = dec_digits
            count = count + 1

    rounded = round(num, rounder)
    return rounded


def calc(sl1n, sl0, sub, sl1p, lamb=1.54, h=0, k=0, ll=4, n=1):
    theta = sl0
    dSL = (n * lamb) / (2 * sind(theta))
    SLa = dSL * (sqrt(h ** 2 + k ** 2 + ll ** 2))

    theta = sub
    dsuba = (n * lamb) / (2 * sind(theta))
    suba = dsuba * (sqrt(h ** 2 + k ** 2 + ll ** 2))
    mismatch = abs((suba - SLa) / suba)
    thickness = abs(-lamb / (2 * (sind(sl1p) - sind(sl0))))
    output = (f"Mismatch = {rounding_4(mismatch)} \n\n"
              f"Substrate Constant = {rounding_4(suba)} \n\n"
              f"SL Constant = {rounding_4(SLa)} \n\n"
              f"Thickness = {rounding_4(thickness)} \n")
    print(output)


calc(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))

