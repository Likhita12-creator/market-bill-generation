#Ex-1:
#t=(1,2,3)
#print(t) #(1,2,3)
#print(type(t)) #<class 'tuple'>



#Paranthesis are optional, heterogeneous and duplicates
#t=1,2,3
#t1=(1,'hi',3.14)
#t2=(1,2,3,1,2)
#print(t) #(1, 2, 3)
#print(t1) #(1, 'hi', 3.14)        
#print(t2) #(1, 2, 3, 1, 2)        



#immutable
#t=(1,2,3)
#t[1]=10
#print(t) #Type Error



#creating tuple
#first way:
#t=()
#print(t) #()



#second way
#t=('0')*5
#print(t) #00000



#third way
#t= (i for i in range(10))
#print(t) #<generator object <genexpr> at 0x000002585CF24940>



#fourth way
#t=tuple(map(int,input().split()))
#print(t) #1 2 3    (1,2,3)



#fifth way
#t=(10,)
#print(t) #(10,)



#index
#t=(1,2,3,3)
#print(t[3]) 



#operations:-
#concatenation
#t=(1,2,3)
#t1=(4,5,6)
#print(t+t1) #(1, 2, 3, 4, 5, 6)



#repitition
#t=('oh')*3
#print(t) #ohohoh



##membership
#l=('a','an','the')
#if 'the' in l:
    #print("True") #True



#iteration
#l=(i for i in range(1,2,3)) 
#print(l) #<generator object <genexpr> at 0x000001E2A75B4940>



#Ex-2:
#t=(1,2,3)
#t1=(4,5,6)
#print(t+t1) #(1, 2, 3, 4, 5, 6)
#s=zip(t,t1)
#print(tuple(s)) #((1, 4), (2, 5), (3, 6))
#for i,j in zip(t,t1):
    #print(i+j) #5 7 9



#Ex-3:
#t=(1,2,3)
#t1=(4,5,6)
#new=[]
#for i,j in zip(t,t1):
    #new.append(i+j)
    #print(tuple(new)) #(5,)      (5, 7)      (5, 7, 9)



#Ex-4:- ATM
#s='''
#
#      1.credit
#      2.debit
#      3.mini stmt
#       4.exit
#      '''
#name='likki'
#password="123"
#user_name=input("Enter name:")
#pass_word=input("Enter password:")
#if name==user_name and password==pass_word:
    #print(s)
#else:
    #print("incorrect")



#Ex-5: ATM
#name="likki"
#password="123"
#user_name=input("Enter name:")
#pass_word=input("Enter password:")
#s='''
#1.credit
#2.debit
#3.mini stmt
#4.exit
#'''
#amount=10000
#if name==user_name and password==pass_word:
    #while True:
        #print(s)
        #option=int(input("Enter the option:"))
        #if option==1:
            #credit_amount=float(input("Enter amount:"))
            #print("Amount after credited:",amount+credit_amount)
        #elif option==2:
            #debit_amount=float(input("Enter amount:"))
            #print("Amount after debited:",amount-debit_amount)
        #elif option==3:
            #print("Amount:",amount)
        #elif option==4:
            #break
#else:
    #print("incorrect")



'''
Task-1
practice tuple and ATM program

Task-2
Prepare a doc on tuple

Task-3
Learn interview questtions
 '''
