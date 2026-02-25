import bge

KEY_LIST = {}

if hasattr(bge, "logic"):
	KEY_LIST["mouse"] = [k for k in dir(bge.events) if not k.startswith("__") and "MOUSE" in k]
	KEY_LIST["keyboard"] = [k for k in dir(bge.events) if not k.startswith("__") and not any(l in k for l in ["MOUSE", "EventToCharacter", "EventToString"])]

# limits the value (v) to a specific range (mi = min, ma = max)
clamp = lambda v,mi,ma : max(mi, min(v, ma))

# interpolate (x) linearly to the desired value (y) by the factor (s)
lerp  = lambda x,y,s : x*(1-s)+y*s

# normalizes a value within a specified range
# x: value
# ymi: original min value
# yma: orginal max value
# zmi: new normalized min value
# zma: new original max value
normalize = lambda x,ymi,yma,zmi,zma : clamp(zmi+(x-ymi)*(zma-zmi)/(yma-ymi), zmi, zma)
