#address depends on value not on variable name
>>> a=5
>>> a
5
>>> b=a
>>> b
5
#finding address of variable
>>> id(a)
1558964208
>>> id(b)
1558964208
>>> b=8
>>> id(b)
1558964256
