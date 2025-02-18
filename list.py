#list is mutable
#a=[1,2,3]
#a[1]=10
#print(a) #[1,10,3]



#creating empty list
#a=[]
#print(type(a)) #<class 'list>



#creating list with default values
#a=[0]*5
#print(a) #[0,0,0,0,0]



#list comprehension
#a=[i for i in range(10)] #[0,1,2,3,4,5,6,7,8,9]
#print(a)



#creating list with user values
#a=list(map(int,input().split()))
#print(*a)



#indexing
#Ex-1
#a=[10,20,30,40]
#print(a[1]) #20



#Ex-2
#a=[10,20,30,40]
#print(a['1']) #Type Error
#print(a[4]) #Index Error



#Negative Indexing
#Ex-1
#a=[10,20,30,40]
#print(a[-1]) #40



#Ex-2
#a=[10,20,30,40]
#print(a[-5]) #Index Error



#Slicing
#Ex-1
#a=[10,20,30]
#print(a[:2]) #[10,20]
#print(a[1:]) #[20,30]
#print(a[:]) #[10,20,30]



#Ex-2
#a=[10,20,30,40]
#print(a[2:2]) #[]
#print(a[4:2]) #[]



#Ex-3
#a=[10,20,30,40]
#print(a[::2]) #[10,30]
#print(a[1::2]) #[20,40]



#Ex-4
#a=[10,20,30,40]
#print(a[-2:]) #[30,40]
#print(a[:-2]) #[10,20]



#Ex-5 Reversing
#a=[10,20,30,40]
#print(a[::-1]) #[40,30,20,10]



#Ex-6
#a=[10,20,30,40,50,60,70]
#print(a[0:5:-2]) #[]



#Ex-7
#a=[10,20,30,40,50,60,70]
#print(a[5:0:-2]) #[60,40,20]



#in-built functions or list methods
#1.index()
#a=[1,2,3,2]
#print(a.index(2)) #1



#2.sort()
#Ex-1
#a=[2,1,3]
#a.sort()
#print(a) #[1,2,3]



#Ex-2
#a=[2,1,3]
#a.sort(reverse=True)
#print(a) #[3,2,1]



#3.reverse()
#a=[1,2,3]
#a.reverse()
#print(a) #[3,2,1]



#4.append()
#a=[1,2,3]
#a.append(4)
#a.append([5,6])
#print(a) #[1,2,3,4,[5,6]]



#5.extend()
#a=[1,2,3]
#a.extend([5,6])
#print(a) #[1,2,3,5,6]



#6.insert()
#a=[1,2,3]
#a.insert(1,10)
#print(a) #[1,10,2,3]



#del keyword
#Ex-1
#a=[1,2,3]
#del a[1]
#print(a) #[1,3]



#Ex-2
#a=[1,2,3]
#del a
#print(a) #Name Error



#7.remove()
#a=[1,2,3,2]
#a.remove(2)
#print(a) #[1,3,2]



#8.pop()
#a=[1,2,3]
#print(a.pop()) #3
#print(a.pop(1)) #2
#print(a) #[1]



#9.clear()
#a=[1,2,3]
#a.clear()
#print(a) #[]



#10.count()
#a=[1,2,3,2]
#print(a.count(2)) #2



#11.copy()
#deep copy()
#a=[1,2,3]
#b=a.copy()
#b[1]=10
#print(a) #[1,2,3]
#print(b) #[1,10,3]



#shallow copy
#a=[1,2,3]
#b=a
#a[1]=10
#print(a) #[1,10,3]
#print(b) #[1,10,3]



#list comprehension
#list=["EVEN" if i%2==0 else 'odd' for i in range(10)]
#print(list)



#s=[1,2,3,2,3,4]
#for i in range(len(s)):
    #if s[i]==3:
        #print(i)



'''
Task-1:practice list and list comprehension.

Task-2:prepare a doc on list.

Task-3:explore jira.
'''





