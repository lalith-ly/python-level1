print("government of tamilnadu")
print("electricity board")
print("-----------------")
no1=input("enter the eb.no:")
no2=input("enter the customer name:")
no3=int(input("Reading for previous month:"))
no4=int(input("REading for current month:"))
total=no4-no3
print("total unit consumed:",total)
paid=total*5
print("amount to be paid Rs:",paid)
