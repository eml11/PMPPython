import numpy as np
import numpy.ma as ma
from scipy.optimize import curve_fit
import sys
import pylab as pb

# load data from file

filename = sys.argv[1]

data = np.loadtxt(filename,skiprows=1,delimiter=",")

photon_energy=data[:,0]
lperunitfreq=data[:,1]

# define various fitting functions
# there are physical reasons for
# the form of the functions but that's
# not really relevent

def black_body(x,a,b,exponent):
  return 1e15*(x**exponent)*a/(np.exp(x/(100*b)) - 1.0)

def powerlaw(x,a,b):
  return 1e15*(a*x**b)*np.exp(-1000/x)*np.exp(-x/4000.0)

def combined_law(x,a,b,c,d,exponent):
  return black_body(x,a,b,exponent) + powerlaw(x,c,d)


# fit the black_body and power law
# seperately

# powerlaw
# only want to include some of the data
power_popt, power_pcov = curve_fit(powerlaw,photon_energy[photon_energy>10000.0],lperunitfreq[photon_energy>10000.0])

#black body

bb_popt, bb_pcov = curve_fit(black_body,photon_energy[photon_energy<10000.0],lperunitfreq[photon_energy<10000.0])

# plot data
pb.loglog(photon_energy,lperunitfreq,'kx')

# plot model
pb.loglog(photon_energy,combined_law(photon_energy,bb_popt[0],bb_popt[1],power_popt[0],power_popt[1],bb_popt[2]),'k--')

#pb.loglog(photon_energy,black_body(photon_energy,popt[0],popt[1]),'k--')

pb.show()
