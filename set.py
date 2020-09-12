   #creating set
>>> set={2,2,3,6,5,7,2}
>>> set
{2, 3, 5, 6, 7}
   #adding elements into set
>>> set.add(45)
>>> set
{2, 3, 5, 6, 7, 45}
  #copying a set
>>> set.copy()
{2, 3, 5, 6, 7, 45}
  #check whether a element present in set or not
>>> print(5 in set)
True
   #adding new element
>>> set.add(65)
>>> set
{65, 2, 3, 5, 6, 7, 45}
    #updating an set
>>> set.update([1,5,6])
>>> set
{65, 2, 3, 1, 5, 6, 7, 45}
   #length of a set
>>> print(len(set))
8
   #removing an element
>>> set.remove(5)
>>> set
{65, 2, 3, 1, 6, 7, 45}
  #discarding an element from set
>>> set.discard(7)
>>> set
{65, 2, 3, 1, 6, 45}
  #pop an element
>>> print(set.pop())
65
  #joining two sets
>>> set1={"gayu","hayu"}
>>> set3=set.union(set1)
>>> set3
{1, 2, 3, 'gayu', 6, 'hayu', 45}
  #inserting elements of set1 into set
>>> set.update(set1)
>>> set
{2, 3, 1, 6, 'hayu', 45, 'gayu'}
  #intersection of 2 sets
>>> set.intersection(set1)
{'gayu', 'hayu'}
>>> 
