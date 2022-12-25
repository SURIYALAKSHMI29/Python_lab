Code 1:(temp)
a=int(input("a="))
b=int(input("b="))
print("Before swaping,\na=",a ,"\nb=",b)
t=a
a=b
b=t
print("After swapping,\na=",a,"\nb=",b)

Code 2:(arithmetic)
a=int(input("a="))
b=int(input("b="))
print("Before swapping,\nValue of a:",a,"\nValue of b:",b)
a=a+b
b=a-b
a=a-b
print("After swapping,\nValue of a:",a,"\nValue of b:",b)

Code 3:(XOR)
a=int(input("a="))
b=int(input("b="))
print("Before swapping,\na:",a,"\nb:",b)
a=a^b
b=a^b
a=a^b
print("After swapping,\na:",a,"\nb:",b)

Code 4:(Comma)
a=int(input("a="))
b=int(input("b="))
print("Before swapping,\na:",a,"\nb:",b)
a=a^b
b=a^b
a=a^b
print("After swapping,\na:",a,"\nb:",b)
