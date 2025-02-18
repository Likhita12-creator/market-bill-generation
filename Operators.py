#Arithmetic Operators
#a=4
#b=2
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)
#print(a%b)
#print(a**b)
#print(a//b)



#Relational Operators
#a=5
#b=2
#print(a<b)
#print(a>b)
#print(a<=b)
#print(a>=b)
#print(a==b)
#print(a!=b)



#Assignment Operator- =
#a=1
#a+=2
#print(a)



#Logical Operators
#a=5
#b=4
#c=3
##print(a>b and a>c)
#print(b>a and c>a)
#print(b>c or c>a)
##print(b>a or c>a)
#print(not a>0)
#print(not a<0)



#Membership Operators
#arr=[1,2,3]
#print(1 in arr)
#print(4 in arr)
#print(4 not in arr)



#Identity Operators
#a=2
#b=2
#print(a is b)
#b=b+1
#print(a is b)
#print(a is not b)



#Bitwise Operators
#print(~3)
#print(3<<1)
#print(4>>1)
#print(3&4)
#print(3^4)
#print(3|4)



#conditional stmts/decision making stmts/selection stmts
#if stmts
#Ex-1
#if(2>1):
    #print("This is if")



#It is not required to keep double quotes for True or False in print stmt
#EX-2
#if(2>1):
    #print(True)



#if else stmt
#n=int(input())
#if n%2==0:
    #print('Even')
#else:
    #print('Odd')



#if elif stmt
#elif stmt can execute when if stmt is false
#Ex-1
#if(2<1):
    #print('This is if')
#elif(2>1):
    #print('This is elif')



#Ex-2
#else stmt can execute when if and elif conditions are false 
#a,b,c=map(int,input().split())
#if a>b and a>c:
    #print(a,'is max')
#elif b>a and b>c:
    #print(b,'is max')
#else:
    #print(c,'is max')



#nested if stmts
#Ex-1
#a,b=map(int,input().split())
#if a>=b:
    #if a==b:
        #print('a and b are equal')
    #else:
        #print(a,'is greater than',b)
#else:
    #print(a,'is smaller than',b)
     

#Ex-2
#if(2<1):
    #print('This is outer if')
    #if(2>0):
        #print('This is inner if')
    #else:
        #print('This is inner else')
#else:
    #print('This is outer else')



#Short hand if
#if 5>2:print('this is if')



#Short hand if else
#a=1
#b=2
#print('This is if')if a<b else print('This is else')



#Looping stmts/iterative stmts
#while loop
#n=int(input())
#i=1
#while i<=n:
    #print(i)
    #i=i+1



#for loop
#Ex-1
#for i in range(0,10,1):
    #print(i)



#Ex-2
#for i in range(10):
    #print(i,end=' ')



#Ex-3
#for i in "likkki":
    #print(i,end=' ')



#Ex-3
#for j in "python":
    #if j=="t":
        #break
    #print(j,end=' ') 



#Ex-4
#for j in "python":
    #if j=="t":
        #continue
    #print(j,end=' ')



#pass stmt
#if True:
    #pass



#Nested for
#for i in range(1,1001):
    #for j in range(1,11):
        #print(i*j,end=' ')
    #print()



#Another Example
#user="likki"
#password="likki2005"
#user_name=input("Enter username")
#pass_word=input("Enter password")
#if user==user_name and password==pass_word:
    #print("Success")
#else:
    #print("Try again")



'''
Task-1:practice operators ,conditional stmts and looping stmts

Task-2:Prepare a doc on python topics

Task-3:Explore stack over flow
'''






