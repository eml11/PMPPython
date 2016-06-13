import numpy as np
import pylab as pb
from scipy.integrate import odeint
from scipy.optimize import leastsq

# example of a boundary value solver
# this is marginally more complex than
# the solver in meteor_solver (initial value
# problem) as we no longer have all the 
# information specified at a single point

# note their are existing methods for solving
# the boundary value problem (e.g. scikits.bvp_solver)
# so really these should be used


# helper equation
def density_eos(pressure):
  mn=1.0e-30 # setting units arbitarilly
  return ((5.0**(3.0/5.0))*(mn**(8.0/5.0)))/((3**(2.0/5.0))*np.pi**(4.0/5.0))*(pressure**(3.0/5.0))

def pressure_eos(density):
  mn=1.0e-30
  return (((5.0**(3.0/5.0))*(mn**(8.0/5.0)))/((3**(2.0/5.0))*np.pi**(4.0/5.0))**(-5.0/3.0))*(density**(5.0/3.0))

# y = [mass,radius,pressure]

# function to solve
def TolOppVol(y,radius):

  if radius<=1.0:
    #for stability
    dm=4*np.pi*density_eos(y[1])
    dP=-(density_eos(y[1]) + y[1])*(y[0]+4*pi*y[1])
  else:
    # mass  
    dm = 4*np.pi*density_eos(y[1])*radius**2
    # pressure
    dP = -(y[1]+density_eos(y[1]))*(y[0] + 4*np.pi*y[1]*radius**3)/(radius*(radius - 2*y[0]))

  return [dm,dP]
 

# guess = [pressure_center,radius]
# boundary conditions:
# center M=0,R=0
# surface M=Mass,Pressure=0

def Vector_Residual(guess,Mass):
  y_out=np.array([0.0,guess[0]])
  radii=np.linspace(0,guess[1]/2.0)
  outwards=odeint(TolOppVol,y_out,radii)

  y_in=np.array([Mass,0])
  radii=np.linspace(guess[1],guess[1]/2.0)
  inwards=odeint(TolOppVol,y_out,radii)

  return np.abs((outwards[-1]-inwards[-1])/(outwards[-1]+inwards[-1]))


Mass=1.0e30
guess_radius=1.0e5*Mass

initial_guess=np.array([pressure_eos(Mass/(guess_radius**3.0)),guess_radius])

#print Vector_Residual(initial_guess,Mass)

result=leastsq(Vector_Residual,initial_guess,args=(Mass,))

#print result

y_out=np.array([0.0,result[0][0]])
radii = np.linspace(0,result[0][1],100)
profile=odeint(TolOppVol,y_out,radii)

print profile

pb.plot(radii/np.max(radii),profile[:,0]/np.max(profile[:,0]),label="Mass")
pb.plot(radii/np.max(radii),profile[:,1]/np.max(profile[:,1]),label="Pressure")
pb.plot(radii/np.max(radii),density_eos(profile[:,1])/np.max(density_eos(profile[:,1])),label="Density")

pb.legend(loc="best")
pb.show()




