#series of prime number upto 100 using function
def prime(list):
  for i in list:
    for j in range(2,i):
      if i%j==0:
        break
    else:
      print(i)
list=[]
for i in range(1,100):
  list.append(i)

result=prime(list)
print(result)

