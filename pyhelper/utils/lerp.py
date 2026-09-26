# interpolate (x) linearly to the desired value (y) by the factor (s)
def lerp(x,y,s):
    return x*(1-s)+y*s
