## Define Function 

def computepay(r,h):
    if h <= 40:
        wage = h * r
    else:
        overtime = h - 40
        ot = float(overtime)
        wage = (40 * r) + (1.5 * r * ot)
    return wage

hrs = input('Input Hours: ')
h = float(hrs)
rate = input('Input Rate: ')
r = float(rate)
print('Your Pay is: ',computepay(r,h))
