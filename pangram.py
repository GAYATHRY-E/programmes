#if a string contain all th alphabets from a to z..then it is known as pangram
def pangram(alpha,string): 
 for i in range(0,len(alpha)):
   for j in range(0,len(string)):
     if alpha[i]!=string[j]:
        flag=0
     else:
        flag=1
 if flag==0:
    print("it is not a pangram")
 else:
     print("is  a pangram")   
string=input("enter the string")
alpha="abcdefghijklmnopqrstuvwxyz"
result=pangram(alpha,string)
