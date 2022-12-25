n=int(input("Enter list size="))
list=[]
for i in range(0,n):
    x=int(input('enter list element='))
    list.append(x)
print(list)
print("Circulating the values,")
for i in range(0,n):
    n_del=list.pop(0)
    list.append(n_del)
    print("The circulated list after",i+1,"rotation,\n",list)
