>>> data={1:"raju",2:"ravi",3:"akku"}
>>> data
{1: 'raju', 2: 'ravi', 3: 'akku'}
>>> data[2]
'ravi'
>>> data.get(5)
>>> print(data.get(5))
None
>>> data.get(5,"not found")
'not found'
  #coverting 2 list into dictionary
>>> keys=["raju","ravi","akku"]
>>> values=["ammu","anu","kavitha"]
>>> data=dict(zip(keys,values))
>>> data
{'raju': 'ammu', 'ravi': 'anu', 'akku': 'kavitha'}
   #getting an element
>>> data["raju"]
'ammu'
   #adding a new element
>>> data['rahul']='aparna'
>>> data
{'raju': 'ammu', 'ravi': 'anu', 'akku': 'kavitha', 'rahul': 'aparna'}
    #delete a element
>>> del data['raju']
>>> data
{'ravi': 'anu', 'akku': 'kavitha', 'rahul': 'aparna'}
  #dictionary within another dictionary
>>> prog={'js':'atom', 'cs':'vs', 'python':['pycharm',"sublime"],"java":{"jse":"netbeans","jee":"eclipse"}}
>>> prog
{'js': 'atom', 'cs': 'vs', 'python': ['pycharm', 'sublime'], 'java': {'jse': 'netbeans', 'jee': 'eclipse'}}
>>> prog['js']
'atom'
>>> prog['python']
['pycharm', 'sublime']
>>> prog['python'][1]
'sublime'
>>> prog['java']
{'jse': 'netbeans', 'jee': 'eclipse'}
>>> prog['java']['jee']
'eclipse'
>>> 
