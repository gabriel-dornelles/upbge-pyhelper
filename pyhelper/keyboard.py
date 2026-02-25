import bge

if hasattr(bge, "logic"):
	from .utils import KEY_LIST

	class PyKeyboard:
		def __init__(self):
			self.device = bge.logic.keyboard
			self.__init_keys__()
			
		def __getattr__(self, attr):
			return getattr(self.device, attr)
			
		def __setattr__(self, attr, value):
			if f'_{self.__class__.__name__}device' in self.__dict__.keys():
				if attr in dir(self.device.__class__):
					setattr(self.device, attr, value)
					return

			super().__setattr__(attr, value)
		
		def __init_keys__(self):
			for key in KEY_LIST["keyboard"]:
				k_input = self.device.inputs[getattr(bge.events, key)]
				setattr(self, key, k_input)
