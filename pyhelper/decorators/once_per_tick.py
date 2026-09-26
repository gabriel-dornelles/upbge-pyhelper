import bge

def once_per_tick(func):
	def wrapper(self, *args, **kwargs):
		attribute = f"{self.__class__.__name__}__method_{func.__name__}_once_per_tick__"
		if not hasattr(self, attribute):
			setattr(self, attribute, 0.0)
		
		if bge.logic.getFrameTime() != getattr(self, attribute):
			setattr(self, attribute, bge.logic.getFrameTime())
			return func(self, *args, **kwargs)
	
	return wrapper
