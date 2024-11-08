from pydualsense import *
from time import sleep
def cross_pressed(state):
    print(state)

ds = pydualsense() # open controller
ds.init() # initialize controller

ds.cross_pressed += cross_pressed
ds.light.setColorT((255,0,255)) # set touchpad color to red
ds.triggerL.setMode(TriggerModes.Rigid  )
ds.triggerL.setForce(1, 255)
ds.triggerR.setMode(TriggerModes.Rigid  )
ds.triggerR.setForce(1, 255)
ds.close()