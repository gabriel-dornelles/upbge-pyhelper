def init():
    import bge
    import sys

    for m in list(sys.modules):
        if m.startswith("pyhelper."):
            del sys.modules[m]
    
    from . import decorators
    
    if hasattr(bge, "logic"):
        from .delta_time import DeltaTime

        if not hasattr(bge.logic, "deltaTime"):
            dt                  = DeltaTime()
            dt.monotonic_time   = bge.logic.getFrameTime
            dt.timescale        = bge.logic.getTimeScale

            bge.logic.deltaTime = dt.deltaTime
        
        # replaces original keyboard and mouse
        # you can access the original with the "device" property
        from .keyboard import PyKeyboard
        from .mouse import PyMouse

        bge.logic.keyboard = PyKeyboard()
        bge.logic.mouse    = PyMouse()
