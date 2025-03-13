n=input("enter a number") 
if int(n)%2==0:
    print("the number is an even number")
else:
    print("the givrn number is an odd number")
    
    
n=input("enter a nunmber")
if int(n)%2==0:
    print("the given number is an even number")
    
a=input("enter first value")
b=input("enter second value")
if int(a)>int(b):
   print(a,"is greater")
elif int(b)>int(a):
    print(b,"is greater")
else:
    print("both are equal value")
    
a=input("enter first value")
b=input("enter second value")
if int(a)>int(b):
    print(a,"is greater")
else:
    if int(b)>int(a):
        print(b,"is greater")
    else:
        print("both are equal value")
        


marks=float(input("enter student marks"))
if marks>=91:
    print("Grade: A")
elif marks>=81:
    print("Grade: B")
elif marks>=71:
    print("Grade: C")
elif marks>=61:
    print("Grade: D")
elif marks>50:
    print("Grade: E")
else:
    marks<50
    print("Grade: F")
              
              
    
