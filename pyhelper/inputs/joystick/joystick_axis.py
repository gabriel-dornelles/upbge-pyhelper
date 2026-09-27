import math

class PyJoystickAxis:
    def __init__(self, axis_index_range):
        self.__device = None
        self.__axis_index_range = axis_index_range
    
    def set_device(self, device):
        self.__device = device
    
    @property
    def values(self):
        if self.__device is None or self.__device.invalid:
            return (0.0,0.0)
        
        axis1 = self.__device.axisValues[self.__axis_index_range[0]]
        if math.isclose(axis1, 0.0, abs_tol=1e-4):
            axis1 = 0.0

        axis2 = self.__device.axisValues[self.__axis_index_range[-1]]
        if math.isclose(axis2, 0.0, abs_tol=1e-4):
            axis2 = 0.0

        return (axis1, axis2)
