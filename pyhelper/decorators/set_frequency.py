import bge

def set_frequency(freq = 60.0):
	target_freq = 1.0 / freq
	def decorator(func):
		def wrapper(self, *args, **kwargs):
			attribute = f"{self.__class__.__name__}__method_{func.__name__}_set_freq__"
			if not hasattr(self, attribute):
				setattr(self, attribute, 0.0)
			
			setattr(self, attribute, getattr(self, attribute) + bge.logic.deltaTime(False))
			if (getattr(self, attribute) >= target_freq):
				if getattr(self, attribute) > target_freq * 5:
					setattr(self, attribute, target_freq)
				
				setattr(self, attribute, getattr(self, attribute) - target_freq)
				return func(self, *args, **kwargs)

		return wrapper
	return decorator
