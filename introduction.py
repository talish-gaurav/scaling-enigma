amt = int(input("Write the amount of money you would like to calculate: "))
note500=amt//500
print("The amount of 500 notes required: ", note500)
amt = amt%500
note100 =amt//100
print("Number of 100 notes" ,note100)
amt= amt%100
note50 =amt//50
print("Number of 50 notes" ,note50)
amt= amt%50
note10 = amt//10
print("Number of 10 notes" ,note10)