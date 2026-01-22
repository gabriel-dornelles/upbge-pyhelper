# I need to create this function because blender/upbge keeps the module in memory once it's loaded
# so this "init" will never be executed again unless the module is reloaded.
# and since I only need to reload the submodules, this initialization function does the trick;
# just don't forget to call it.
def init():
    import sys

    for m in list(sys.modules):
        if m.startswith("pyhelper."):
            del sys.modules[m]

    from . import delta_time
    from . import decorators
    from . import mouse
    from . import keyboard

    for m in ['init', 'delta_time', 'mouse', 'keyboard']:
        del globals()[m]
    