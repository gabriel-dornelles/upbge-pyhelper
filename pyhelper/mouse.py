import bge

if hasattr(bge, "logic"):
	import math
	import mathutils

	from .decorators import once_per_tick
	from .utils import KEY_LIST

	class PyMouse:
		def __init__(self):
			self.device           = bge.logic.mouse
			self.__old_position   = mathutils.Vector((0.0, 0.0))
			self.__delta_position = mathutils.Vector((0.0, 0.0))
			self.__first_frame    = True
			self.__center         = False
			self.__was_centered   = False

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
			for key in KEY_LIST["mouse"]:
				k_input = self.device.inputs[getattr(bge.events, key)]
				setattr(self, key, k_input)

		@once_per_tick
		def __get_delta_position__(self):
			mouse_pos = mathutils.Vector(self.device.position)

			if self.__first_frame:
				self.__first_frame  = False
				self.__old_position = mouse_pos
				return
			
			if self.__center and not self.__was_centered:
				xc = math.isclose(mouse_pos.x, 0.5, abs_tol = 0.02)
				yc = math.isclose(mouse_pos.y, 0.5, abs_tol = 0.02)

				if xc and yc:
					self.__was_centered = True
				
				return
			
			dx = self.__old_position.x - mouse_pos.x
			dy = self.__old_position.y - mouse_pos.y

			if math.isclose(round(dx * bge.render.getWindowWidth(), 2), 0.5):
				dx = 0.0
			if math.isclose(round(dy * bge.render.getWindowHeight(), 2), 0.5):
				dy = 0.0
			
			self.__delta_position = mathutils.Vector((dx,dy))
			self.__old_position   = mouse_pos
			self.__center         = False
		
		@property
		def deltaPosition(self):
			self.__get_delta_position__()
			return self.__delta_position.copy()
		
		@once_per_tick
		def reCenter(self):
			self.__center = True

			width = bge.render.getWindowWidth()
			height = bge.render.getWindowHeight()

			self.__old_position.x = (width * 0.5) / width
			self.__old_position.y = (height * 0.5) / height

			self.device.position = (0.5, 0.5)
