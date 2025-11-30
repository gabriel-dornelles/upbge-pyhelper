import bge

if hasattr(bge, "logic"):
	from .utils import KEY_LIST

	class PyKeyboard:
		def __init__(self):
			self.__device = bge.logic.keyboard
			self.__init_keys__()
			
		def __getattr__(self, attr):
			return getattr(self.__device, attr)
			
		def __setattr__(self, attr, value):
			if f'_{self.__class__.__name__}__device' in self.__dict__.keys():
				if attr in dir(self.__device.__class__):
					setattr(self.__device, attr, value)
					return

			super().__setattr__(attr, value)
		
		def __init_keys__(self):
			for key in KEY_LIST["keyboard"]:
				k_input = self.__device.inputs[getattr(bge.events, key)]
				setattr(self, key, k_input)
	
	bge.logic.pykeyboard = PyKeyboard()
