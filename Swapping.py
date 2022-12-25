Code 1:
a=int(input("a="))
b=int(input("b="))
print("Before swaping,\na=",a ,"\nb=",b)
t=a
a=b
b=t
print("After swapping,\na=",a,"\nb=",b)

Code 2:
a=int(input("a="))
b=int(input("b="))
print("Before swaping,\na=",a ,"\nb=",b)
print("After swapping,\na=",b,"\nb=",a)

Code 3:
print("Enter a b=")
a,b=map(int,input().split())
print("Before swapping,",a,b)
print("After swapping,",b,a)
