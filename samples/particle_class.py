
# example of how to use classes
# and class inheritance, along
# with some of the special methods


import numpy as np

# define a base class which will
# be inherited
class PointObject:

  X = np.zeros(3)

  # __init__ is a special method
  # that defines PointObjects behaviour
  # when initialised
  def __init__(self,ar1):
    self.X = np.array(ar1)

  def __add__(self,ar1):
    X=np.copy(self.X)
    if type(ar1)==type(np.array([])) and ar1.size==3:
      X+=ar1
    elif type(ar1)==type([]) and size(ar1)==3:
      X+=np.array(ar1)
    elif type(ar1)==type(1) or type(ar1)==type(1.0):
      X+=ar1
    else:
      raise TypeError
    return PointObject(X)

  def __sub__(self,ar1):
    X=np.copy(self.X)
    if type(ar1)==type(np.array([])) and ar1.size==3:
      X-=ar1
    elif type(ar1)==type([]) and size(ar1)==3:
      X-=np.array(ar1)
    elif type(ar1)==type(1) or type(ar1)==type(1.0):
      X-=ar1
    else:
      raise TypeError
    return PointObject(X)


  def __mul__(self,ar1):
    X=np.copy(self.X)
    if type(ar1)==type(np.array([])) and ar1.shape==(3,3):
      X=np.dot(ar1,self.X)
    elif type(ar1)==type([]) and np.array(ar1).shape==(3,3):
      X=np.dot(np.array(ar1),self.X)
    elif type(ar1)==type(1) or type(ar1)==type(1.0):
      X*=ar1
    else:
      raise TypeError
    return PointObject(X)  

# Particle inherits from PointObject
# but has additional methods/variables
class Particle(PointObject):

  P = np.zeros(3)

  # overwrite the init method
  def __init__(self,position,momentum):
    self.X=np.array(position)
    self.P=np.array(momentum)

  # define some new methods
  def Potential(self,position):
    return np.sum(position**2)

  def EvolveStep(self):
    P = np.copy(np.sqrt(np.sum(self.P**2))) 
    X = np.copy(self.X)
   
    # note euler "a heap of crap"
    self.X+=self.P
    self.P+=(self.Potential(self.X)-self.Potential(X))/P

  # this is what is printed on calling __print__
  def __str__(self):
    return "X: "+str(list(self.X))+"\nP: "+str(list(self.P))

  # redefine arithmatic
  def __add__(self,ar1):
    prtobj=PointObject.__add__(self,ar1)
    return Particle(np.copy(prtobj.X),np.copy(self.P))

  def __sub__(self,ar1):
    prtobj=PointObject.__sub__(self,ar1)
    return Particle(np.copy(prtobj.X),np.copy(self.P))

  def __mul__(self,ar1):
    prtobj=PointObject.__mul__(self,ar1)
    return Particle(np.copy(prtobj.X),np.copy(self.P))


#something that inherits from particle
class ChargedParticle(Particle):

  q=1

  # only redefining one thing
  def Potential(self,position):
    return Particle.Potential(self,position)+(self.q**2.0)/(np.sqrt(np.sum(position**2)))


# actually use the code
prtc1 = Particle([1.0,0.0,0.0],[1.0,2.0,3.0])

print prtc1
for i in range(4):
  
  prtc1.EvolveStep()
  print prtc1

prtc1=prtc1+1
print
print prtc1


# same for ChargedParticle:


prtc1 = ChargedParticle([1.0,0.0,0.0],[1.0,2.0,3.0])

print
print "Charged Particle"
print prtc1
for i in range(4):
  
  prtc1.EvolveStep()
  print prtc1

prtc1=prtc1+1
print
print prtc1








