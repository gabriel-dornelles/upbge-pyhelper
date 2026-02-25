# UPBGE - PyHelper

A Python module with small functionalities to help with game development on UPBGE 0.2.5b.

## Features

- [x] Delta Time (Time elapsed between frames; used to maintain stability on different hardwares)
- [x] Decorators (Used to change the behavior of methods)
- [x] PyKeyboard (A class that extends the SCA_PythonKeyboard class)
- [x] PyMouse (A class that extends the SCA_PythonMouse class)
- [x] Utils (useful generic methods and variables)

## How to use?

The first thing you need to do is import the module, but you need to also call the "init" method from the module to properly initialize the module.

This is necessary because UPBGE/Blender keeps the module loaded in memory, which makes things a bit difficult to handle, so I had to create a function to reload the PyHelper submodules.

```python
# import the module
import pyhelper

# call the initialization method
pyhelper.init()
```

Then you can use PyHelper normally without breaking your python components and ge (That's what I hope.).

### More Examples

Here are some examples about how to use PyHelper features:

### Delta Time

```python
# initialize pyhelper
import pyhelper
pyhelper.init()

# Calling the deltaTime method
bge.logic.deltaTime(is_scaled = True)
```

When you import pyhelper and call the initialization method, a new method called "deltaTime" is "injected" into bge.logic module, so you can easily access the method from bge.logic module. I did it this way because the bge module is used much more frequently and this make things simpler, although it's not the ideal way to do it.

### PyMouse

Also we have a new python class called PyMouse, this class replaces the original mouse in "bge.logic" module.

After initializing the module, you should be able to access the PyMouse class through the bge's logic module, like this:

```python
import pyhelper
pyhelper.init()

print(bge.logic.mouse.deltaPosition) # returns a mathutils vec2

# you can also access the original SCA_PythonMouse:
bge.logic.mouse.device # <-- original device
```

From PyMouse class you can access the mouse buttons directly, without bge.events:

```python
left_mouse_button = bge.logic.mouse.LEFTMOUSE # <-- SCA_InputEvent

if left_mouse_button.activated:
    print("LeftMouseButton has been pressed!")
```

### PyKeyboard

And the PyKeyboard class, is mainly used to access the keyboard keys, same as PyMouse:

```python
wkey = bge.logic.keyboard.WKEY # <-- SCA_InputEvent

if wkey.activated:
    print("W key pressed!")
```
