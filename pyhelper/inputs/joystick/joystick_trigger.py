import math

class PyJoystickTrigger:
    def __init__(self, trigger_index):
        self.__device = None
        self.__trigger_index = trigger_index
    
    def set_device(self, device):
        self.__device = device
    
    @property
    def value(self):
        if self.__device is None or self.__device.invalid:
            return 0.0
        
        triggerVal = self.__device.axisValues[self.__trigger_index]
        if math.isclose(triggerVal, 0.0, abs_tol=1e-4):
            triggerVal = 0.0
        
        return triggerVal
