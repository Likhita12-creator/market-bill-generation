from datetime import datetime

name=input("Enter your name:")

#list of items
lists='''
Rice     Rs 20/- kg
Sugar    Rs 30/- kg
Salt     Rs 20/- kg
Oil      Rs 80/- liter
Paneer   Rs 110/- kg
Maggi    Rs 50/- kg
Boost    Rs 90/- each
Colgate  Rs 85/- each
'''

#declarations
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]
finalamount=0

#rates of items
items={'rice':20,'sugar':30,'salt':20,'oil':80,'paneer':110,'maggi':50,'boost':90,'colgate':85}

option=int(input("For list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry, Your item is not available")
    else:
        print("You entered wrong number")
    inp=input("Can I bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Likki SuperMarket",25*"=")
            print(28*" ","Tenali")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',12*" ",'Quantity',5*" ",'price')
            for i in range(len(pricelist)):
                print(i,5*' ',5*' ',ilist[i],15*' ',qlist[i],10*" ",plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)    
            print("gst amount",40*" ",'Rs',gst)    
            print(75*"-")
            print(50*" ",'FinalAmount:','Rs',finalamount)    
            print(75*"-")
            print(20*" ","Thank You, Visit Again..!!!")
            print(75*"-")



