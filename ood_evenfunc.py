#finding odd and even numbers in a list
def odd_even(list):
 
  even=[ ]
  odd=[ ]
  for i in list:
    if i%2==0:
      even.append(i)
    else:
      odd.append(i)
  print("even numbers are",even)
  print()
  print("odd numbers are",odd)
list=[]
for i in range(1,51):
  list.append(i)
result=odd_even(list)
