import bge

if hasattr(bge, "logic"):
    from .decorators import once_per_tick

    class DeltaTime:
        def __init__(self):
            self.__firstFrame = True
            self.__previousTime = 0.0
            self.__deltaTime = 0.0
        
        @once_per_tick
        def __calc__(self, scaled):
            if self.__firstFrame:
                self.__firstFrame = False
                self.__previousTime = bge.logic.getRealTime()
            else:
                current = bge.logic.getRealTime()
                delta = current - self.__previousTime
                self.__previousTime = current
                self.__deltaTime = (delta * bge.logic.getTimeScale()) if scaled else delta
        
        def deltaTime(self, scaled = True):
            self.__calc__(scaled)
            return self.__deltaTime

    bge.logic.deltaTime = DeltaTime().deltaTime
