#Import Cost Calculator v1
#Motunrayo Gbadebo - Day 5
#CNY price + shipping method = NGN landed cost

# ====================
# EXCHANGE RATES
# ====================
cny_to_usd = 0.138
usd_to_ngn = 1580

# ====================
# USER INPUTS
# ====================
print("=== NAIRA IMPORT CALCULATOR ===")
print("")

product_name = input("Product name: ")
price_in_cny = float(input("Price per unity (CNY ¥): "))
quantity = int(input("How many units: "))
weight_per_unit  = float(input("Weight per unit in kg: "))

print("")
print("Shipping method:")
print("1 - Express Air (3-5 days)")
print("2 - Normal Air Guangzhou (10-14 days)")
print("3 - Normal Air Hong Knog (2-3 weeks)")

choice = input("Enter 1,2 or 3: ")

# ====================
# SHIPPING CALCULATION
# ====================
total_weight = weight_per_unit * quantity

if choice == "1":
	method = "Express Air"
	freight_usd = 14 * total_weight
	customs_ngn = 1300 * total_weight
	delivery = "3-5 days"
elif choice == "2":
	method = "Normal Air Guangzhou"
	freight_usd = 10.5 * total_weight
	customs_ngn = 1000 * total_weight
	delivery = "10-14 days"
elif choice =="3":
	method = "Normal Air Hong Kong"
	freight_usd = 11.9 * total_weight
	customs_ngn = 1000 * total_weight
	delivery = "2-3 weeks"
else:
	print("Invalid choice. Please enter 1,2 or 3.")

# ====================
# COST CALCULATION
# ====================
freight_ngn = freight_usd * usd_to_ngn
total_shipping_ngn = freight_ngn + customs_ngn

product_cost_ngn = price_in_cny * cny_to_usd * usd_to_ngn * quantity

total_landed_cost = product_cost_ngn + total_shipping_ngn
cost_per_unit = total_landed_cost / quantity

# ====================
# OUTPUT
# ====================
print("")
print("=== RESULT ===")
print("Product:		" + product_name)
print("Units:		" + str(quantity))
print("Shipping:	" + method + " (" + delivery + ")")
print("Product cost:	N" + str(round(product_cost_ngn, 2)))
print("Shipping cost:	N" + str(round(total_shipping_ngn, 2)))
print("TOTAL LANDED:	N" + str(round(total_landed_cost, 2)))
print("Cost per unit:	N" + str(round(cost_per_unit, 2)))
