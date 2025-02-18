#Strings
#a='python'
#b="python's"
#c='''python'''
#print(type(a),type(b),type(c))#<class 'str'>   <class 'str'>   <class 'str'>



#Positive Indexing
#Ex-1:
#s='hello'
#print(s[1]) #e



#Ex-2:
#s=input()
#print(s[len(s)-1]) #python    #n



#Ex-3:
#s='hello'
#print(s['1']) #Error



#Ex-4:
#s='hello'
#print(s[6]) #Index Error



#Negative Indexing
#Ex-1:
#s='hello'
#print(s[-1]) #o



#Ex-2:
#s='hello'
#print(s[-6]) #Index Error



#Slicing
#Ex-1:
#s='hello'
#print(s[2:4]) #ll



#Ex-2:
#s='hello'
#print(s[:2]) #he



#Ex-3:
#s='hello'
#print(s[2:]) #llo
#print(s[::]) #hello



#Ex-4:
#s="hello"
#print(s[2:2]) #" "
#print(s[4:2]) #" "



#Ex-5:
#s="hello"
#print(s[-4:-2]) #el



#Ex-6:
#s='hello'
#print(s[-2:]) #lo



#Ex-7:
#s='hello'
#print(s[:-2])
#print(s[::2])
#print(s[1::2])



#Ex-8:
#s='hello'
#print(s[::-1]) #olleh



#Ex-9:
#s='welcome to python'
#print(s.split()) #['welcome','to','python']
#print(s.split(maxsplit=1)) #['welcome','to python']



#String Methods
#1.len()
#s='hello'
#print(len(s)) #5



#2.find()
#s='python is on'
#print(s.find('on')) #4



#3.index()
#s='python is on'
#print(s.index('on')) #4



#4.rfind()
#s='python is on'
#print(s.rfind('on')) #10



#5.rindex
#s='python is on'
#print(s.rindex('on')) #10



#6.count()
#s='python is on'
#print(s.count('on')) #2



#7.lstrip
#s=' hello'
#print(s.lstrip()) #hello



#8.rstrip
#s='hello '
#print(s.rstrip()) #hello



#9.strip
#s=' hello '
#print(s.strip()) #hello



#10.replace()
#s='python is difficult'
#print(s.replace('difficult','easy')) #python is easy



#11.join()
#s='python'
#l=list(s)
#l[1]=i
#print(''.join(1))



#12.upper()
#s='python'
#print(s.upper()) #PYTHON



#13.lower()
#s='PYTHON'
#print(s.lower()) #python



#14.title()
#s='python is easy'
#print(s.title()) #Python Is Easy



#15.capitalize
#s='python is easy'
#print(s.capitalize()) #Python is easy



#16.swapcase()
#s='Python Is Easy'
#print(s.swapcase()) #pYTHON iS eASY



#17.isdigit
#s='1234'
#print(s.isdigit()) #True
 


#18.isalpha()
#s='abcd'
#print(s.isalpha()) #True



#19.isalnum()
#s='123abc'
#print(s.isalnum()) #True



#20.isupper()
#s='HELLO'
#print(s.isupper()) #True



#21.islower()
#s='hello'
#print(s.islower()) #True



#22.istitle()
#s="Python Is Easy"
#print(s.istitle()) #True



#23.startswith()
#s='python'
#print(s.startswith('py')) #True



#24.endswith()
#s='python'
#print(s.endswith('on')) #True



'''
Task-1
Practice string and string methods prepare doc

Task-2
Take a string like paragraph replace is with are and the with that

Task-3
Explore slack
'''

