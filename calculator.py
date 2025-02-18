def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error! Division by zero."
    else:
        return x/y
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=input("Enter choice(1/2/3/4):")
if choice in('1','2','3','4'):
    x=float(input("Enter First number:"))
    y=float(input("Enter Second number:"))
    if choice=='1':
        print(add(x,y))
    elif choice=='2':
        print(subtract(x,y))
    elif choice=='3':
        print(multiply(x,y))
    elif choice=='4':
        print(divide(x,y))
else:
    print("Invalid Input")
add(x,y)
subtract(x,y)
multiply(x,y)
divide(x,y)





