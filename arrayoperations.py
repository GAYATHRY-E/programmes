 #adding a common factors to array
import numpy
arr=array([1,2,3,6,5])
arr=arr+5
print(arr)

#adding two arrays
from numpy import *
arr1=array([1,5,6,4])
arr2=array([2,3,5,6])
arr3= arr1+ arr2
print(arr3)

#log of an array
from numpy import *
arr1=([1,2,3,4])
print(log(arr1)) 

#squareroot of array
from numpy import *
arr1=([1,2,3,4])
print(sqrt(arr1))

#sum of array
from numpy import *
arr1=([1,2,3,4])
print(sum(arr1))

#concatenating 2 arrays
from numpy import *
arr1=([1,2,3])
arr2=([4,5,6])
print(concatenate([arr1,arr2]))

#copying 1 array to another
from numpy import *
arr1=([1,2,3])
arr2=([4,5,6])
arr2=arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

#coping using view function
from numpy import *
arr1=array([1,2,3])
arr2=arr1.view()
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

#shallow copy
from numpy import *
arr1=array([1,2,3])
arr2=arr1.view()
arr1[1]=6
print(arr1)
print(arr2)
id(arr1)
id(arr2)

#deep copy
from numpy import *
arr1=array([1,2,3])
arr2=arr1.copy()
arr1[1]=6
print(arr1)
print(arr2)
