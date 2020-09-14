#using an external variable
>>> a=8
>>> b=9
>>> temp=a
>>> a=b
>>> b=temp
>>> a
9
>>> b
8
#withput an external variable
>>> a=a+b
>>> b=a-b
>>> a=a-b
>>> a
9
>>> b
8
#easiest way
>>> (a,b)=(b,a)
>>> a
9
>>> b
8
