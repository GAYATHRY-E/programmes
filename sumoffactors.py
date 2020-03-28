n=int(input("enter the number"))
s=0
for i in range(1,n+1):
  if(n%i==0):
    s=s+i
print("sum of factors of n are ",s)
