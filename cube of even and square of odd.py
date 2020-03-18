#sum of square of odd numbers and sum of cube of even numbers upto n natural numbers
n=int(input("enter the limit"))
t=0
s=0

for i in range(1,n+1):
  if(i%2==0):
   s=s+(i*i*i)
   i=i+1
  else:
   t=t+(i*i)
   i=i+1
print("sum of cube of even numbers")
print(s)
print("sum of square ofodd numbers")
print(t)
