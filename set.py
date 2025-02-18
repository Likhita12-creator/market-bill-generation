#Ex-1:
#s={3,1,2}
#print(s) #{1, 2, 3}



#Duplicates not allowed
#s={1,2,3,1,2}
#print(s) #{1, 2, 3}



#Creating set
#Ex-1:
#s=set()
#print(s) #set()



#Ex-2:
#s=('0')*3
#print(s) #000



#Ex-3:
#s=(i for i in range(10))
#print(s) #<generator object <genexpr> at 0x000002776FD44940>



#Ex-4:
#s=set(map(int,input().split()))
#print(s) #{2, 3, 4, 5, 6}



#operations:
#1.insertion operation
#a) add()
#s={1,2,3}
#s.add(4)
#print(s) #{1,2,3,4}



#b) update()
#s={3,4,1}
#s.update({2,5})
#print(s) #{1, 2, 3, 4, 5}



#3.deletion
#a)remove()
#s={3,4,1}
#s.remove(4)
#print(s) #{1,3}
#s.remove(5) #key error



#b)discard()
#s={3,4,1}
#s.discard(4)
#print(s) #{1,3}



#c)pop()
#s={1,4,3}
#print(s.pop()) #1



#d)clear()
#s={3,4,1}
#s.clear()
#print(s) #set()



#Ex-2:
#s1={1,2,3,4,5}
#s2={4,5,6,7,8}
#s3={6,7,8}
#print(s1|s2,s1&s2,s1-s2,s1^s2) #{1, 2, 3, 4, 5, 6, 7, 8} {4, 5} {1, 2, 3} {1, 2, 3, 6, 7, 8}
#print(s1.union(s2),s1.intersection(s2),s1.difference(s2),s1.symmetric_difference(s2))
#print(s1.isdisjoint(s2),s1.isdisjoint(s3),s3.issubset(s2),s2.issuperset(s3)) #False True True True




#Frozen set
#h=[1,2,3,4,4]
#print(h) #[1, 2, 3, 4, 4]
#d=frozenset()
#print(d) #frozenset()
#print(d.append(5)) #Error
#print(d[0]) #Error
#print(list(d)) #[ ]
 
 
 
'''
Task-1: Prepare a doc on total methods of datatypes.

Task-2: Complete the mini project.
'''
 




