#Ex:-1
#def add(a,b):
#    print(a+b)
#add(2,3) #5



#Ex:-2
#def add(a):
#    print("Hi",a)
#n=input()
#add(n)



#Ex:-3
#def likki(*a): 
#   print("Hii", a)
#likki(1,2,3,4,5,6)



#Ex-4
#def likki(a):
#   print("Hii")
#likki([1,2,3,4,5,6]) #Hii



#Ex-5
#Nested functions
#def outer_function():
#   print("This is outer function")
#    def inner_function():
#       print("This is inner function")
#  inner_function()
#outer_function()



#Ex-6
#def likki(**name):
#   print("Hii",name)
#likki(name="ram",age=5) #Hii {'name': 'ram', 'age': 5}



#Ex-7
#def add(a,b):
#    print(a+b)
#    return(a+b)
#def sub(a,b):
#    print(a-b)
#def mul(a,b):
#    print(a*b)



#Ex-8:
#lambda functions
#f=lambda x,y,z:x+y+z
#print(f(1,2,3))



#Ex-9:
#l1=[12,3,4,5,6]
#l2=[]
#for i in l1:
#    t=lambda a:a+1
#    l2.append(t(i))
#print(l2)



#Ex-9
#higher order functions
#map()
#print(list(map(lambda x:x+x,[1,2,3])))



#Ex-10
#def A(n):
#    return n+n
#a=(1,2,3,4)
#result=map(A,a)
#print(list(result)) #[2, 4, 6, 8]

#Ex-11
#filter()
#print(list(filter(lambda x:x%2==0,[1,2,3,4]))) #[2, 4]



#Ex-12
#ages=[11,12,13,14,15,20]
#def A(x):
#    if x<18:
#        return False
#    else:
#        return True
#k=filter(A,ages)
#print(list(k))



#Ex-13
#reduce()
#from functools import reduce
#print(reduce(lambda x,y:x+y,[1,2,3,4])) #10



'''
Task-1:Practice function and advance function.

Task-2:WAP using functions ATM, Calculator
'''
