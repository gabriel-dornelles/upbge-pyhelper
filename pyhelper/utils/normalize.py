from .clamp import clamp

# normalizes a value within a specified range
# x: value
# ymi: original min value
# yma: orginal max value
# zmi: new normalized min value
# zma: new original max value
def normalize(x,ymi,yma,zmi,zma):
    return clamp(zmi+(x-ymi)*(zma-zmi)/(yma-ymi), zmi, zma)
