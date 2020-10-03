from array import *
arr=array('i',[])
n=int(input('enter the length of array'))
for i in range(n):
  x=int(input('enter the next value'))
  arr.append(x)
print(arr)
ele=int(input('ente the value to search'))
for e in arr:
  if e==ele:
    break
print(arr.index(ele))
