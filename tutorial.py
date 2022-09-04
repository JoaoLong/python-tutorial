#PYTHON TUTORIAL - João Joaquim

#Unlike C++, there is no ; to end lines, so a new line is a new command, unless you use \
#Indentation is required by the language
#Multi-line comment is with three apostrophes '''

#Packages/modules

#Numerical, scientific, plotting
import numpy as np
import scipy as sp
import matplotlib as mpl

#Submodules
from matplotlib import pyplot as plt

#Read-write
#Input only inputs strings, so type must be cast
print("Hello World!")
test = input("What is your age?")
print(test)
num = float(test)
print(num)


#Python has 5 data types and variables do not need explicit type declaration
#Numbers (int, float, long, complex) 
n = 1
x = 2.1
z = 1+2j
z1 = 3e-5j

print(n)
print(x)

#Strings - ' or " or even ''' for multi-line string
name = "John"

print(name)
print(name[0])
print(name + "Smith")

#Lists - arrays with all possible types (with brackets)
list = ["John", 22, 71.4]

print(list)
print(list[0])
print(list + ["Smith", 23])

list[2] = 11;
print(list)

del list[2]
print(list)

#Tuples - read-only lists (with parentheses)
tuple = ("John", 22, 71.4)

print(tuple)
print(tuple[0])
print(tuple + ("Smith", 23))

#Invalid code: tuple[2] = 100

#Dictionary - like a map in C++, with a key and an entry (with brackets)
dict = {"name" : "John", "grade" : 16}
print(dict)
print(dict["name"])
dict["age"] = 20;
print(dict)

#Casting
y = 2
y1 = float(y)
print(y1)
s = chr(y)
print(s + "hello")

#Operators are the same, but exponentiation is **
#Booleans are True and False
print(2**4)
print(3>2 and 4>1)
print(True and False)
print(True or False)
print(not False)

#Membership operator in, identity is, compares memory addresses
print(list is tuple)
print("John" in list)

#Control and decision - if and else
if ("John" in list):
    print("Correct")
else:
    print("Wrong")

if (x == 2):
    print ("Two")
elif (x == 3):
    print ("Three")
else :            
    print ("Four")

#Loop for
for i in range(1,10) :
    print(i)

for i in "Python" :
    print (i)

for i in list :
    print (i)      

#Loop while
count = 0
while (count < 9):
    print(count)
    count = count + 1

count = 0
while (count < 9):
    if (count == 6) :
        break
    print(count)
    count = count + 1   

count = 0
while (count < 9):
    print(count)
    count = count + 1  
    if (count == 6) :
        continue 

#Functions - all parameters are passed by reference
def function(arg):
   return arg

print(function(2))

#Lambda functions
sum = lambda arg1, arg2: arg1 + arg2
print(sum(2,3))

#Files - read and write are r and w, binary is b, rb, wb
#Read-write is w+ if the file does not exist and r+ if it does
f = open("foo.txt", "w")
print ("Name of the file: ", f.name)
f.write("Hello world")
f.close()

f1 = open("foo.txt", "r")
str = f1.read(2)
f1.close()
print(str)

#Classes and objects
class Employee:
    #Documentation string - __doc__
    'Common base class for all employees'

    #Variables
    empCount = 0

    #Constructor - self is like this in C++
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    #Destructor
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")
    
    #Methods
    def displayCount(self):
        print("Total Employee ", Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

print(Employee.__doc__)
emp1 = Employee("Zara", 2000)

#Derived class
class Person(Employee): # define child class
   def __init__(self):
        print("Calling child constructor")

   def childMethod(self):
        print('Calling child method')

#Libraries - numpy vectors and matrices
print(np.pi + np.sqrt(2))
v = np.array([0,1])
M = np.array([[0,1],[2,3]])
print(np.matmul(M,v))

#Scipy - scientific python, built from numpy
#Submodules:
'''
File input/output – scipy.io
Special Function – scipy.special
Linear Algebra Operation – scipy.linalg
Interpolation – scipy.interpolate
Optimization and fit – scipy.optimize
Statistics and random numbers – scipy.stats
Numerical Integration – scipy.integrate
Fast Fourier transforms – scipy.fftpack
Signal Processing – scipy.signal
Image manipulation – scipy.ndimage
'''

print(sp.linalg.det(M))
print(sp.linalg.eigvals(M))

def f(x):
    return np.cos(x)

print(sp.integrate.quad(f, 0, 2))    

#Matplotlib - graphics and plots
import matplotlib.pyplot as plt

#Criar listas de pontos
x = np.arange(0,100)
y = x**2
figura = plt.figure(figsize=(5, 5))
plt.plot(x , y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Funcao quadratica")
plt.grid()
plt.show()
plt.savefig('plot.png')