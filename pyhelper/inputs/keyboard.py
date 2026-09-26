import bge

class PyKeyboard:
	def __init__(self):
		self.device = bge.logic.keyboard
		self.__init_keys__()
		
	def __getattr__(self, attr):
		return getattr(self.device, attr)
		
	def __setattr__(self, attr, value):
		if 'device' in self.__dict__.keys() and hasattr(self.device, attr):
			setattr(self.device,attr,value)
			return
		
		super().__setattr__(attr, value)
	
	def __init_keys__(self):
		key_list = [k for k in dir(bge.events) if not k.startswith("__") and not any(l in k for l in ["MOUSE", "EventToCharacter", "EventToString"])]
		
		for key in key_list:
			k_input = self.device.inputs[getattr(bge.events, key)]
			setattr(self, key, k_input)
