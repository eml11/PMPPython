# this is a sample file for reading
# in data from a csv using numpy
# note this runs in python 2

# haven't had time to debug

import sys
import numpy as np
from scipy.integrate import simps

# get filename passed to file
# sys.argv is the list of python
# arguments. Note sys.argv[0] is
# the name of the python program
# i.e. meteor.py
filename = sys.argv[1]

# load data from file
data = np.genfromtxt(filename,delimiter=",",names=True)
header=data.dtype.names

# unpack the data
altitude=data[header[1]]
energyperkm=data[header[0]]

# the functions we need are in various libraries

# find the energy
energy=simps(energyperkm,x=altitude)

print "energy [kt]: " + str(energy) # convert to string

double_energyperkm=energyperkm*2.0

# double energy
double_energy=simps(double_energyperkm,x=altitude)

print "energy [kt]: " + str(double_energy)


# write new energy to file.
data2=np.column_stack((altitude,double_energyperkm))

print data2

header_string=",".join(list(header))
np.savetxt("new_meteor_numpy.csv",data2,delimiter=",",header=header_string)

