def leapyear(year):
 if year%4==0:
  if year%100==0:
     if year%400==0:
        print("its a leap year")
     else:
        print("not leap year")
  else:
        print("Is a leap year")
 else:
        print("not leap year")
year=int(input("enter the year"))
result=leapyear(year)
