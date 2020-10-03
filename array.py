#using buffer_info we can identify address of array and no. of elemnts in array
from array import *
arr=array('i',[2,5,6,9,-6])
print(arr.buffer_info())

#append
from array import *
arr=array('i',[2,5,6,9,-6])
arr.append(3)
print(arr)

#remove
from array import *
arr=array('i',[2,5,6,9,-6])
arr.remove(6)
print(arr)

#printing a particular element of an array
from array import *
arr=array('i',[2,5,6,9,-6])
print(arr[3])

#printing all elements of an array
from array import *
arr=array('i',[2,5,6,9,-6])
for i in range(len(arr)):
  print(arr[i])
  
#shortcut to print all elements
from array import *
arr=array('i',[2,5,6,9,-6])
for i in arr:
 print(i)
 
#characters in array
from array import *
arr=array('u',['j','k','h'])
for i in arr:
 print(i)
 
#coping an array into newarray
from array import *
arr=array('i',[1,2,3,5,6])
newarr=array(arr.typecode,(a for a in arr))
for i in newarr:
 print(i)

#print all elements using while loop
from array import *
arr=array('i',[1,2,3,5,6])
i=0
while(i<len(arr)):
  print(arr[i])
  i=i+1
