from .keyboard import PyKeyboard
from .mouse import PyMouse

from .joystick.joystick_manager import PyJoystickManager

del globals()['keyboard']
del globals()['mouse']
del globals()['joystick']
