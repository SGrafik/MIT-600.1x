def closest_power(base, num, x = 0):
    '''
    Returns the integer exponent closest to the supplied number.
    Required args are a base value and a number to check against.
    Returns the lower exponent in instances of ties.
    '''
    y = base ** x
    z = base ** (x + 1)

    if z >= num:
        if abs(z - num) >= abs(y - num):
            return x
        else:
            return x + 1
    else:
        return closest_power(base, num, x + 1)

print (closest_power(4, 1))
