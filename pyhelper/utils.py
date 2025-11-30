import bge

KEY_LIST = {}

if hasattr(bge, "logic"):
	KEY_LIST["mouse"] = [k for k in dir(bge.events) if not k.startswith("__") and "MOUSE" in k]
	KEY_LIST["keyboard"] = [k for k in dir(bge.events) if not k.startswith("__") and not any(l in k for l in ["MOUSE", "EventToCharacter", "EventToString"])]

# methods
clamp = lambda v,mi,ma : max(mi, min(v, ma))
lerp  = lambda x,y,s : x*(1-s)+y*s
