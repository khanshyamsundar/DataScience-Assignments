# program to find the volume of a sphere with given diameter
# import numpy package to use the value of pi
import numpy as np

diameter = 12
radius = diameter/2
volume = ((4/3) * np.pi * (radius**3))
print("Volume of the sphere is: %f" % volume)
