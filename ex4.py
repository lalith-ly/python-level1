print("Bharathi Supermarket")
print("No.44,Nehru street,puducherry")
print("-----------------------------")
print("Bill receipt")
print("------------")
str1=input("Enter the serial number:")
str2=input("Enter the particulars:")
rate=int(input("Enter the rate:"))
quantity=int(input("Enter the quantity:"))
total=rate*quantity
print("total amount Rs:",total)
GST=total*10/100
print("GST(10 per):",GST)
paid=total+GST
print("amount to be paid Rs:",total)
         
