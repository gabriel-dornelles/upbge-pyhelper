class DeltaTime:
    def __init__(self):
        self.monotonic_time = None
        self.timescale      = 0.0

        self.__is_first_frame = True
        self.__previous_time  = 0.0
        self.__delta_time     = 0.0
    
    def __calculate__(self, is_scaled):
        if self.monotonic_time is None or self.timescale == 0.0:
            return

        if self.__is_first_frame:
            self.__is_first_frame = False
            self.__previous_time  = self.monotonic_time()
        else:
            current_time         = self.monotonic_time()
            delta_time           = current_time - self.__previous_time
            self.__previous_time = current_time

            self.__delta_time = (delta_time * self.timescale()) if is_scaled else delta_time
    
    def deltaTime(self, is_scaled = True):
        self.__calculate__(is_scaled)
        return self.__delta_time
