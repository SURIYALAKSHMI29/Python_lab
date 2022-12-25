x=int(input("Enter the number:"))
count=0
for i in range(1,x):
    if x%i==0:
        count+=1        
if count==1:
    print(x,"is a prime")
else:
    print(x,"is not a prime")
