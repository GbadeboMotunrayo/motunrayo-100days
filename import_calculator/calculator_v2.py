import os

def clear_screen():
	os.system('clear')

def format_naira(amount):
	return "N{:,.0f}".format(amount)

# Import Cost Calculator v2
# Motunrayo Gbadebo - Day 8
# Refactored into clean functions

# ====================
# EXCHANGE RATES
# ====================
cny_to_usd = 0.138
usd_to_ngn = 1580

# ====================
# FUNCTIONS
# ====================

def get_product_cost(price_cny, quantity):
	cost = price_cny * cny_to_usd * usd_to_ngn * quantity
	return round(cost, 2)

def get_shipping_cost(choice, weight_kg, quantity, cbm):
	if choice == "1":
		freight_usd = 14 * weight_kg
		customs_ngn = 1300 * weight_kg
		method = "Express Air"
		delivery = "3-5 days"
	elif choice == "2":
		freight_usd = 10.5 * weight_kg
		customs_ngn = 1000 * weight_kg
		method = "Normal Air Guangzhou"
		delivery = "10-14 days"
	elif choice == "3":
		freight_usd = 11.9 * weight_kg
		customs_ngn = 1000 * weight_kg
		method = "Normal Air Hong Kong"
		delivery = "2-3 weeks"
	elif choice == "4":
		print("")
		print("Gadgets Express - select type:")
		print("1 - Packaged Phone  (N18,000/unit)")
		print("2 - Naked Phone (N14,000/unit)")
		print("3 - iphone 17 (N27,000/unit)")
		gadget = input("Enter 1, 2, or 3: ")
		if gadget == "1":
			total_shipping = 18000 * quantity
		elif gadget == "2":
			total_shipping = 14000 * quantity
		elif gadget =="3":
			total_shipping = 27000 * quantity
		else:
			total_shipping = 0
		return " Gadgets Express", "3-5 days", total_shipping
	elif choice == "5":
		if cbm is None:
			print("Sea shipping requires dimensions not weight.")
			return None
		freight_usd = 135 * cbm
		freight_ngn = freight_usd * usd_to_ngn
		customs_ngn = 260000 * cbm
		method = "Sea Shipping"
		delivery = "50-60 days"
		total_shipping = round(freight_ngn + customs_ngn, 2)
		return method, delivery, total_shipping
		if gadget == "1":
			unit_cost = 18000
			gadget_name = "Packaged Phone"
		elif gadget == "2":
			unit_cost = 14000
			gadget_name = "Naked Phone"
		elif gadget == "3":
			unit_cost = 27000
			gadget_name = "iphone 17"
		else:
			print("Invalid choice.")
			return None
		method = "Gadget Express - " + gadget_name
		delivery = "Express"
		total_shipping = unit_cost * quantity
		return method, delivery, total_shipping
	else:
		print("Invalid choice.")
		return None

	freight_ngn = freight_usd * usd_to_ngn
	total_shipping = round(freight_ngn + customs_ngn, 2)
	return method, delivery, total_shipping

def show_result(name, quantity, method, delivery, product_cost, shipping_cost, cost_per_unit, selling, margin):
	total = round(product_cost + shipping_cost, 2)
	per_unit = round(total / quantity, 2)

	print("")
	print("=== RESULT ===")
	print("Product:		" + name)
	print("Units:		" + str(quantity))
	print("Shipping:	" + method + " (" + delivery + ")")
	print("Product cost:	" + format_naira(product_cost))
	print("Shipping cost	" + format_naira(shipping_cost))
	print("TOTAL LANDED:	" + format_naira(total))
	print("Cost per unit:	" + format_naira(per_unit))
	print("Sell per unit:	" + format_naira(selling_price))
	print("Profit margin:	" + str(round(margin * 100)) + "%")

# ====================
# MAIN PROGRAM
# ====================
while True:
	clear_screen()
	print("=== NAIRA IMPORT CALCULATOR v2 ===")
	print("")
	name = input("Product name: ")
	price_cny = float(input("Price per unit (CNY ¥): "))
	quantity = int(input("How many units: "))
	print("")
	print("How do you want to enter shippment size?")
	print("1 - By weight in kg (air shipping)")
	print("2 - By dimension in cm (sea shipping)")
	size_type = input("Enter 1, or 2: ")
	if size_type == "1":
		weight_per_unit = float(input("Weight per unit in kg: "))
		total_weight = weight_per_unit * quantity
		cbm = None
	elif size_type == "2":
		length = float(input("Box length in cm: "))
		width = float(input("Box width in cm: "))
		height = float(input("Box height in cm: "))
		cbm = (length * width * height) / 1000000
	if cbm is not None and cbm < 0.1:
		cbm = 0.1
		total_weight = 0
		print("CBM calculated: " + str(round(cbm, 4)))
	print("")
	print("Shipping method:")
	print("1 - Express Air (3-5 days)")
	print("2 - Normal Air Guangzhou (10-14 days)")
	print("3 - Normal Air Hong Kong (2-3 weeks)")
	print("4 - Gadget Express (phones)")
	print("5 - Sea Shipping (50-60 days)")
	choice = input("Enter 1, 2, 3, 4 or 5: ")
	product_cost = get_product_cost(price_cny, quantity)
	result = get_shipping_cost(choice, total_weight, quantity, cbm)
	if result is None:
		input("Press Enter to try again...")
		continue
	method, delivery, shipping_cost = result
	margin = float(input("Target profit margin (e.g. 0.5 for 50%): "))
	total_landed = product_cost + shipping_cost
	cost_per_unit = round(total_landed / quantity, 2)
	selling_price = round(cost_per_unit / (1 - margin), 2)
	show_result(name, quantity, method, delivery, product_cost, shipping_cost, cost_per_unit, selling_price, margin)
	again = input("\nCalculate another product? (yes/no): ")
	if again.lower() != "yes":
		print("Goodbye!")
		break
