#sum of odd numbers in a list
def oddsum(list):
  sum=0
  print("odd numbers are")
  for i in list:
    if i%2==0:
      continue
    else:
      print(i)
      sum=sum+i
  print("sum off odd numbers is ",sum)
list=[ ]
for i in range(1,20):
  list.append(i)
result=oddsum(list)
