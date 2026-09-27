import bge

from .joystick import PyJoystick
from ... import decorators
from ...utils.clamp import clamp

class PyJoystickManager:
    def __init__(self):
        # current active joysticks
        self.__joystick_list = []

        for i in range(8):
            self.__joystick_list.append(PyJoystick()) # memleak?
    
    def __update_joystick_list__(self):
        for i in range(8):
            joy = bge.logic.joysticks[i]
            pyj = self.__joystick_list[i]

            if joy != pyj.get_device():
                pyj.set_device(joy)

    def __check_joysticks__(self):
        self.__update_joystick_list__()
    
    def __update_joysticks__(self):
        for i in range(8):
            pyj = self.__joystick_list[i]
            pyj.update()
    
    def init(self):
        self.__update_joystick_list__()
    
    # should be called every frame by user
    def update(self):
        self.__check_joysticks__()
        self.__update_joysticks__()
    
    def get_joystick_list(self):
        return self.__joystick_list
    
    def get_joystick(self, index):
        return self.__joystick_list[clamp(index, 0, 7)]
