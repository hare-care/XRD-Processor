from math import sin, radians, sqrt
import sys

# calculate sine from degrees
def sind(angle):
    rad = radians(angle)
    val = sin(rad)
    return val

# format so there are 4 significant figures
def rounding_4(num):
    #start with 4
    rounder = 4
    count = 2
    # if number is a decimal then look for how many digits to display
    # otherwise, 4 decimal places are good
    if num < 1:
        # if <1, then format is like 0.###### 
        # so the decimals are in the third slot of the str
        #get length of decimal digits
        dec_digits = len(str(num)) - 2
        
        while count < dec_digits:
            # look through zeros until there is a nonzero value
            # once we find that, that is our first significant digit and need to show 4 after that
            if str(num)[count] == '0':
                rounder = rounder + 1
            else:
                #ends loop once we find something thats nonzero
                count = dec_digits
                
            # safety measure to prevent infinite loop
            count = count + 1
    #round the number to the correct number of digits
    rounded = round(num, rounder)
    #return value
    return rounded

#actual calculator
def calc(sl1n, sl0, sub, sl1p, lamb=1.54, h=0, k=0, ll=4, n=1):
    # sl1n: superlattice peak to the left of sample
    # sl0: main peak of sample
    # sub: substrate peak of sample
    # sl1p: supperlattice peak to the right of sample
    #lamb: lambda of xrd 
    # h, k, ll: hkl of sample
    # n: magnitude of peak to the side
    
    theta = sl0
    #calculating d value of main peak
    dSL = (n * lamb) / (2 * sind(theta))
    #calculating a value of main peak
    SLa = dSL * (sqrt(h ** 2 + k ** 2 + ll ** 2))

    theta = sub
    #calculating d val of substrate peak
    dsuba = (n * lamb) / (2 * sind(theta))
    #calculating a val of substrate peak
    suba = dsuba * (sqrt(h ** 2 + k ** 2 + ll ** 2))
    #calculating mismatch between substrate and main peak
    mismatch = abs((suba - SLa) / suba)
    #calculatinf thickness of superlattice
    thickness = abs(-lamb / (2 * (sind(sl1p) - sind(sl0))))
    #formatting output
    output = (f"Mismatch = {rounding_4(mismatch)} \n\n"
              f"Substrate Constant = {rounding_4(suba)} \n\n"
              f"SL Constant = {rounding_4(SLa)} \n\n"
              f"Thickness = {rounding_4(thickness)} \n")
    #printing
    print(output)

# when calling in terminal just take arguments for peak values
# simplifies my life since the other parameters are always the same
calc(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))

