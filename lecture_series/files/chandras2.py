# % can be used to format strings, like this:
"%s can be %s" % ("strings", "interpolated")

# A newer way to format strings is the format method.
# This method is the preferred way
"{0} can be {1}".format("strings", "formatted")
# You can use keywords if you don't want to count.
"{name} wants to eat {food}".format(name="Bob", food="lasagna")


def varargs(*args):
    return args

def keyword_args(**kwargs):
    return kwargs

def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)


(lambda x: x > 2)(3)


import math
from math import ceil, floor
# You can import all functions from a module.
# Warning: this is not recommended
from math import *
import math as m
dir(math)
#----

import numpy as np

arr = np.array([(1,2),(3,4),(5,6)])
arr = np.array(np.arange(15).reshape(3,5))
arr.ndim # Number of axes
arr.shape # tuple of integers indicating size
arr.size # Total number of elements in array
arr.dtype # Array elements data type
arr.itemsize # Size in bytes of each element
arr.data # Actual data. Not required

arr = np.array([(1,2),(3,4),(5,6)], dtype=complex)

np.zeros((3,4))
np.ones((2,3,4), dtype=int16)
np.random.random((2,3))

np.linspace(0,2,9) # 9 numbers from 0 to 9
np.linspace(0,2*np.pi,100)

# arithmetic operations

a=np.array([1,2,3,4])
b=np.arange(4)

a=b
b**2
10*sin(a)
a<35


A = array([[1,1],[0,1]])
B = array([[2,0],[3,4]])

A*B
dot(A,B)

a.sum()
a.cumsum()
a.min()
a.max()

vstack((A,B))
hstack((A,B))

B = np.random.random((3,4))

B.sum(axis=0)

B[1,1]
B[:,1]

B[-1] # equivalent to B[-1,:]

B.flat # iterator over all elements of the array

for row in b:
	print row

for element in b.flat:
	print element,

B.ravel()
B.shape = (6,2)
a= arange(30)
a.shape = 2,-1,3
a.shape # => (2,5,3)


B.transpose()

B.resize((2,6))

c = a
c is a
c = a.view()	# Shallow Copy
c is a
c.base is a
c[0,0]=100
a

c = a.copy()	# Deep Copy
d is a

from numpy.linalg import *

a=np.eye(2)
np.trace(a)
eig(a)



import pylab

mu, sigma = 2,0.5
v = np.random.normal(mu,sigma, 10000)

pylab.hist(v,bins = 50, normed = 1)
pylab.show()

(n,bins) = numpy.histogram(v, bins=50, normed = True)
pylab.plot(.5*(bins[1:]+bins[:-1]),n)
pylab.show()



#---

# File I/O

fp = open("wings.txt")
vals = [int(k.strip()) for k in fp.readlines()]
fp.close()
pylab.hist(vals)
pylab.show()





# We subclass from object to get a class.
class Human(object):

    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        return "%s: %s" % (self.name, msg)

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"


# Instantiate a class
i = Human(name="Ian")
print(i.say("hi"))     # prints out "Ian: hi"

j = Human("Joel")
print(j.say("hello"))  # prints out "Joel: hello"

# Call our class method
i.get_species()   # => "H. sapiens"

# Change the shared attribute
Human.species = "H. neanderthalensis"
i.get_species()   # => "H. neanderthalensis"
j.get_species()   # => "H. neanderthalensis"

# Call the static method
Human.grunt()   # => "*grunt*"

