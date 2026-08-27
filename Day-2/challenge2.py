#SIMPLE BILL CALCULATOR
print("==============================")
print("     SIMPLE BILL CALCULATOR           ")
print("==============================")
print()

price = int(input("What is the price of the meal?"))
quantity = int(input("How many meals?"))
tax_percent = int(input("What percentage is the tax?"))

print("Price: ₹",price)
print("Quantity:", quantity)
print("Tax:", tax_percent,"%")

subtotal = price*quantity
tax = subtotal*5/100
total_amount = subtotal+tax

print("Subtotal: ₹",subtotal)
print(f"Tax: {tax:.2f}")
print(f"Total: ₹ {total_amount:.2f}")
print("=====================================")