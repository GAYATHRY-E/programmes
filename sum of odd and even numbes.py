n=int(input("enter the limit"))
t=0
s=0
for i in range(0,n+1):
  if(i%2==0):
    t=t+i
    i=i+1
  else:
    s=s+i
    i=i+1
print("sum of even numbers is ",t)
print("sum of odd numbers is ",s)
