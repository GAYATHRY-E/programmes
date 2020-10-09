#no. of odd numbers and even numbers in list which taken from user using function
def count(list):
  odd=0
  even=0
  for i in list:
    if i%2==0:
      even+=1
    else:
      odd+=1
  return even,odd 

n=int(input("enter the length of the list"))
list=[]
for j in range(n):
   x=int(input("enter the next value"))
   list.append(x)
odd,even=count(list)
print("odd:{}   even:{}".format(odd,even))
