def fact(n):
  c=1
  if n==1:
    return 1
  else:
    for i in range(1,n+1):
      c=c*i
    print(c)
n=int(input("enter the number"))
result=fact(n)
