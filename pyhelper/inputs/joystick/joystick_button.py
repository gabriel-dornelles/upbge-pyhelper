class PyJoystickButton:
    def __init__(self, button_index):
        self.__device = None
        self.__button_index = button_index
        self.__button_status = -1
        self.__activated = False
        self.__released = False
        self.__hold = False
    
    def __check_input_status__(self):
        if self.__device is None or self.__device.invalid:
            self.__button_status = -1
            self.__activated = False
            self.__released = False
            self.__hold = False
            return
        
        button_in = self.__button_index in self.__device.activeButtons

        # -1 inactive
        #  0 pressed
        #  1 holding
        #  2 released

        # -1 -> 0
        #  0 -> 1
        #  1 -> 2
        #  2 -> -1

        if self.__button_status == -1:
            self.__button_status = 0 if button_in else -1 # <- pressed
        elif self.__button_status == 0:
            self.__button_status = 1 if button_in else 2 # <- holding
        elif self.__button_status == 1:
            self.__button_status = 2 if not button_in else 1
        elif self.__button_status == 2:
            self.__button_status = -1
        
        self.__activated = self.__button_status == 0
        self.__released = self.__button_status == 2
        self.__hold = self.__button_status == 1
    
    def update(self):
        self.__check_input_status__()

    @property
    def active(self):
        return self.__hold
    
    @property
    def activated(self):
        return self.__activated
    
    @property
    def released(self):
        return self.__released
    
    def set_device(self, device):
        self.__device = device
