#fibonacci series using fuction
def fib(count):
  a=0
  b=1
  print(a,b,end="  ")
  counts=count-1
  for i in range(1,counts):
    c=a+b
    a=b
    b=c
    print(c,end="  ")
    counts+=1
count=int(input("enter the count"))
result=fib(count)
