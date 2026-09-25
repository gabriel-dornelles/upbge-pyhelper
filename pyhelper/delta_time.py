class DeltaTime:
    def __init__(self):
        self.monotonic_time = None
        self.timescale = None

        self.__is_first_frame = True
        self.__previous_time = 0.0
        self.__delta_time = 0.0
    
    def __calculate__(self):
        if self.monotonic_time is None:
            return

        if self.__is_first_frame:
            self.__is_first_frame = False
            self.__previous_time = self.monotonic_time()
            return
        else:
            current_time = self.monotonic_time()
            self.__delta_time = current_time - self.__previous_time
            self.__previous_time = current_time

    def __return_delta__(self, scaled):
        if scaled:
            # I'm using getFrameTime
            # and I suppose it's already scaled
            # so I'll not scale again here
            return self.__delta_time
        else:
            return self.__delta_time / self.timescale() if self.__delta_time > 0.0 else 0.0
    
    def deltaTime(self, scaled = True):
        if not hasattr(self, f"_{self.__class__.__name__}__last_tick"):
            setattr(self, f"_{self.__class__.__name__}__last_tick", self.monotonic_time())
        
        if self.monotonic_time() == self.__last_tick:
           return self.__return_delta__(scaled)
        
        self.__calculate__()
        self.__last_tick = self.monotonic_time()

        return self.__return_delta__(scaled)
