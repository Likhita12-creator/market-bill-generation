#Ex-1:
#Modes of file
#file=open("sample.txt",mode='r')
#v=file.read()
#print(v)
#v=file.read(4)
#print(v)
#file.close()



#Ex-2:
#file=open("sample.txt",'r')
#v=file.readline()
#print(v)
#v=file.readline(4)
#print(v)
#file.close()



#Ex-3:
#file=open("sample.txt",'r')
#v=file.readlines()
#print(v)
#v=file.readline(4)
#print(v)
#file.close()



#Ex-4
#file=open('sample.txt','w')
#v=file.write('welcome to python')
#print(v)
#file.close()



#Ex-5:
#file=open('sample.txt','w')
#v=file.writelines(['welcome to python\n','pyhton is interpreted'])
#print(v)
#file.close()

     

#Ex-6:
#append mode
#file=open('sample.txt','a')
#v=file.write('\npython is easy')
#print(v)
#file.close()



#Ex-7:
#file=open('sample.txt')
#print(file.read())
#file.close()



#Ex-8:
#file=open('sample.txt')
#print(file.read())
#file.seek(0)
#print(file.read(2))
#print(file.tell())
#file.seek(11)
#print(file.read())
#print(file.tell())
#file.close()



#Ex-9:
#Exception
#try:
#    a,b=map(int,input().split())
#    c=a/b
#    print(c)
#except:
#    print("cant divide by zero")



#Ex-10:
#try:
#    a,b=map(int,input().split())
#    c=a/b
#except:
#    print("cant divide by zero")
#else:
#    print(c)



#Ex-11:
#try:
#    f=open("sample.txt")
#except:
#    print("something went wrong while opening the file")
#finally:
#    f.close()



'''
Task-1: Practice Error handling and file handling.

Task-2: Prepare document on file and error handling.

task-3: Python solving questions.