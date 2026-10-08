# CHristopher Monarrez M3P4

#variables
make = input("Enter Make of Vehicle: ")
model = input("Enter model of Vehicle: ")
msrp_amount = float(input("Enter The MSRP: "))
discount_percent = float(input("Enter The Discount Percentage (in .xx format): "))

#calculations
amount_off = msrp_amount * discount_percent
discounted_final_price = msrp_amount - amount_off

print("Make: ",make)
print("model: ",model)
print("MSRP: ",msrp_amount)
print("Discount Percent: ",discount_percent)
print("Amount Off: ",amount_off)
print("Discounted Price: ",discounted_final_price)