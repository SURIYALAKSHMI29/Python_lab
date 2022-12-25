p1=int(input('Price of Book1='))
p2=int(input('Price of Book2='))
p3=int(input('Price of Book3='))
p4=int(input('Price of Book4='))
p5=int(input('Price of Book5='))
total=p1+p2+p3+p4+p5
discount=total*0.05
Net_price=total-discount
print('Total=',total,'\n','Discount=',discount,'\n','Net price',Net_price,'\n')
