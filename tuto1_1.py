
#!/bin/python2

# Typical header of a Python script using Pinocchio
from pinocchio.utils import *
from pinocchio.explog import exp,log
from numpy.linalg import pinv,norm
import pinocchio as se3
import gepetto.corbaserver


from display import Display
display = Display()

# Example of use of the class Display to create a box visual object.
boxid   = 147
name    = 'box' + str(boxid)
[w,h,d] = [1.0,1.0,1.0]
color   = [red,green,blue,transparency] = [1,1,0.78,1.0]
display.viewer.gui.addBox('world/'+name, w,h,d,color)

# Example of use of the class Display to create a sphere visual object.
display.viewer.gui.addSphere('world/sphere', 1.0,color)

# Example of use of the class Display to create a cylinder visual object.
radius = 1.0
height = 1.0
display.viewer.gui.addCylinder('world/cylinder', radius,height,color)

# Example of use of the class display to place the previously-create object at random SE3 placements.
display.place("world/box147",se3.SE3.Random(),False)
display.place("world/sphere",se3.SE3.Random(),False)
display.place("world/cylinder",se3.SE3.Random())
