#Ex-1:
#d={'id':1,'name':'ravi','add':'hyd','add':'bglr'}
#print(d) #{'id':1, 'name':'ravi', 'add':'bglr'}



#Creating dictionary
#Ex-1:
#d={}
#print(type(d)) #<class 'dict'>



#Ex-2:
#keys=('name','add')
#d=dict.fromkeys(keys)
#print(d) #{'name':None, 'add':None}



#Ex-3:
#d={i:i**2 for i in range(10)}
#print(d) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}



#Ex-4:
#d={'id':1,'name':'ravi'}
#print(d) #{'id': 1, 'name': 'ravi'}



#operations:-
#1.a)Accessing
#d={'id':1,'name':'ravi'}
#print(d['name']) #ravi
#print(d['age']) #key error



#b)get():-
#d={'id':1,'name':'ravi'}
#print(d.get('name')) #ravi
#print(d.get('age')) #None
#print(d.get('age',0)) #0



#c)set default():-
#d={'id':1,'name':'ravi'}
#print(d.setdefault('id',0)) #1
#print(d.setdefault('age')) #None
#print(d) #{'id': 1, 'name': 'ravi', 'age': None}



#d)keys():-
#d={'id': 1, 'name':'ravi'}
#print(d.keys( )) #dict_keys(['id', 'name'])

#Traversing:-
#for key in d.keys():
    #print(key) #id name



#e)values():-
#d={'id':1,'name':'ravi'}
#print(d.values()) #dict_values([1, 'ravi'])
#for value in d.values():
    #print(value) # 1       ravi



#f)items():-
#d={'id':1,'name':'ravi'}
#print(d.items()) #dict_items([('id', 1), ('name', 'ravi')])
#for i,j in d.items():
    #print(i,j) #id 1        name ravi



#2.Searching:-
#a)has_key():-
#d={'id':1,'name':'ravi'}
#print(d.has_key('name'))
#print(d.has_key('age')) #Attribute Error



#3.Insertion:-
#a)assignment operator():-
#d={'id':1,'name':'ravi'}
#d['age']=22
#d['name']='likki'
#print(d) #{'id': 1, 'name': 'likki', 'age': 22}

                

#b)update():-
#d={'id':1,'name':'ravi'}
#d.update({'name':'likki','age':19})
#print(d) #{'id': 1, 'name': 'likki', 'age': 19}



#4.Deletion:-
#a)del keyword:-
#d={'id':1,'name':'ravi'}
#del d['name']
#print(d) #{'id': 1}



#b)pop():-
#d={'id':1,'name':'ravi'}
#print(d.pop('name')) #ravi



#c)popiem():-
#d={'id': 1,'name':'ravi'}
#print(d.popitem()) #('name', 'ravi')



#d)clear():-
#d={'id':1,'name':'ravi'}
#print(d.clear()) #None



#Creating nested dictionary:-
#d={1:{'id':1,'name':'ravi'},2:{'id':2,'name':'likki'}}
#print(d) #{1: {'id': 1, 'name': 'ravi'}, 2: {'id': 2, 'name': 'likki'}}



#Accessing nested dictionary:-
#d={1:{'id':1,'name':'ravi'},2:{'id':2,'name':'likki'}}
#print(d[1]['name']) #ravi
#print(d[2]['name']) #likki



'''
Task-1
Practice dict

Task-2
Prepare a doc on dictionary

Task-3
learn interview questions
Super Market project
'''



