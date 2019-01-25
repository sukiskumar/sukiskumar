n1=float(input("enter 1st numbr:"))
n2=float(input("enter 2nd numbr:"))
n3=float(input("enter 3rd numbr:"))
if(n1>n2)and(n1>n3):
    largest=n1
elif(n2>n1)and(n2>n3):
    largest=n2
else:
    largest=n3
print("largest num is",largest)
