def fib(list):
  a=0
  b=1
  print(a,b,end="  ")
  for i in list :
    c=a+b
    if c==i:
       print(i,end=" ")
       a=b
       b=c
       c=a+b
list=[ ]   
last=int(input("enter the last element wanted"))

for i in range(1,last+1):
  list.append(i)
result=fib(list)
