#count of substring in a string using function
def countsub(string,sub_string):
   count=0
   for i in range(0,len(string)+1):
      if string[i:i+len(sub_string)]==string[:len(sub_string)]:
       count+=1
   print(count)
string=input("enter the string")
sub_string=input("enter the substring")
result=countsub(string,sub_string)
