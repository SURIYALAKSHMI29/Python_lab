Code(1):
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

Code(2):
def rotate(str,d):
   for i in range(0,n):
       Lfirst = str[0 : d]
       Lsecond = str[d :]
       print ("After Rotation : ",(Lsecond+Lfirst))
       str=Lsecond+Lfirst
if __name__ == "__main__":
      str = input("Enter String :")
n=int(input("No.of elements in a string="))
d=int(input("Enter d:"))
rotate(str,d)
