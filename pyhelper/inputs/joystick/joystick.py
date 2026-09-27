import bge

from .joystick_button import PyJoystickButton
from .joystick_axis import PyJoystickAxis
from .joystick_trigger import PyJoystickTrigger

class PyJoystick:
    def __init__(self):
        self.__device = None

        self.button = {
            "A" : PyJoystickButton(0),
            "B" : PyJoystickButton(1),
            "X" : PyJoystickButton(2),
            "Y" : PyJoystickButton(3),
            "SELECT" : PyJoystickButton(4),
            "HOME" : PyJoystickButton(5),
            "START" : PyJoystickButton(6),
            "L3" : PyJoystickButton(7),
            "R3" : PyJoystickButton(8),
            "LB" : PyJoystickButton(9),
            "RB" : PyJoystickButton(10),
            "PADUP" : PyJoystickButton(11),
            "PADDOWN" : PyJoystickButton(12),
            "PADLEFT" : PyJoystickButton(13),
            "PADRIGHT" : PyJoystickButton(14)
        }

        self.axis = {
            "LEFT_AXIS" : PyJoystickAxis([0,1]),
            "RIGHT_AXIS" : PyJoystickAxis([2,3]),
        }

        self.trigger = {
            "LEFT" : PyJoystickTrigger(4),
            "RIGHT" : PyJoystickTrigger(5),
        }
    
    def update(self):
        for k in self.button.keys():
            self.button[k].update()
    
    def set_device(self, device):
        self.__device = device

        for k in self.button.keys():
            self.button[k].set_device(self.__device)
        
        for k in self.axis.keys():
            self.axis[k].set_device(self.__device)
        
        for k in self.trigger.keys():
            self.trigger[k].set_device(self.__device)
    
    def get_device(self):
        return self.__device
