# interpolate (x) linearly to the desired value (y) by the factor (s)

def lerp(x,y,s):
    return x*(1-s)+y*s

# x,y
def lerp_vec2(vec,y,s):
    for i in range(2):
        vec[i] = lerp(vec[i],y,s)
    return vec

# x,y,z
def lerp_vec3(vec,y,s):
    for i in range(3):
        vec[i] = lerp(vec[i],y,s)
    return vec
