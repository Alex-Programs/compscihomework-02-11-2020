#1.	A shop is having a sale.  They’re giving 10% off when a customer spends £10 or less and a 20% discount when they spend over £10.
#Write a program that asks for the amount spent and then displays the discount to be applied and then the final price (i.e. with the discount applied).

#Get input
start = float(input("Amount: "))

#calculate
if start < 10:
    discount = start / 10
else:
    discount = start / 5

#print results
print("Discount:", discount)

print("End:", start-discount)

