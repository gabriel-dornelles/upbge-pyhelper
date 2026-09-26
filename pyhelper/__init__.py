def init():
    import bge
    import sys

    # remove pyhelper from sys modules if loaded.
    for module in list(sys.modules):
        if module.startswith("pyhelper."):
            del sys.modules[module]
    
    from . import decorators

    # we're in editor not engine, return.
    if not hasattr(bge, "logic"):
        return
    
    from . import utils
    
    # not adding deltatime if already exists in logic module.
    if not hasattr(bge.logic, "deltaTime"):
        from . import timing

        delta_time_cls = timing.DeltaTime()
        delta_time_cls.monotonic_time = bge.logic.getFrameTime
        delta_time_cls.timescale = bge.logic.getTimeScale

        bge.logic.deltaTime = delta_time_cls.deltaTime

        del globals()['timing']
    
    from . import inputs

    # replacing devices with our classes
    # but we still can access the devices
    # from "cls.device" attribute.
    bge.logic.keyboard = inputs.PyKeyboard()
    bge.logic.mouse = inputs.PyMouse()

    del globals()['inputs']
