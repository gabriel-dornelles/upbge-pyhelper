def init():
    import bge
    import importlib
    import sys

    for module in list(sys.modules):
        if module.startswith("pyhelper."):
            del sys.modules[module]
    
    importlib.import_module("pyhelper.delta_time")
    importlib.import_module("pyhelper.decorators")
    importlib.import_module("pyhelper.mouse")
    importlib.import_module("pyhelper.keyboard")
