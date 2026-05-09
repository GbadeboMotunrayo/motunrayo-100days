import os

def clear_screen():
	os.system('clear')

def format_naira(amount):
	return "N{:,.0f}".format(amount)

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
		freight_usd = 135 * cbm
		customs_ngn = 260000 * cbm
		method = "Sea Shipping"
		delivery = "50-60 days"
	freight_ngn = freight_usd * usd_to_ngn
	total_shipping = round(freight_ngn + customs_ngn)
	return method, delivery, total_shipping

def get_gadget_cost(choice, quantity):
	if choice == "1":
		total_shipping = 18000 * quantity
	elif choice == "2":
		total_shipping =14000 * quantity
	elif choice == "3":
		total_shipping = 27000 * quantity
	else:
		total_shipping = 0
	return "Gadgets Express", "3-5 days", total_shipping

def show_result(name, quantity, method, delivery, product_cost, shipping_cost, per_unit, selling_price, margin):
	print("")
	print(" === RESULT ===")
	print("Product:		" + name)
	print("Units:		" + str(quantity))
	print("Shipping:	" + method + " (" + delivery + ")")
	print("Product cost:	" + format_naira(product_cost))
	print("Shipping cost:	" + format_naira(shipping_cost))
	print("TOTAL LANDED:	" + format_naira(product_cost + shipping_cost))
	print("Cost per unit:	" + format_naira(per_unit))
	print("Sell per unit:	" + format_naira(selling_price))
	print("Profit margin:	" + str(round(margin * 100)) + "%")

# ====================
# MAIN PROGRAM
# ====================

while True:
	clear_screen()
	print("=== NAIRA IMPORT CALCULATOR V2.1 ===")
	print("")

	# STEP 1 - Product catigory
	print("What are you importing?")
	print("1 - Aromatheraphy products")
	print("2 - Gadgets (phones)")
	print("3 - Other products")
	category = input("Enter 1, 2, of 3: ")

	print("")
	name = input("Product name: ")
	price_cny = float(input("Price per unit (CNY Y): "))
	quantity = int(input("How many units: "))
	print("")

	product_cost = get_product_cost(price_cny, quantity)

	# STEP 2 - Gadgets go straight to gadget shipping
	if category == "2":
		print("Gadgets Express - select type:")
		print("1 - Packaged Phone	(N18,000/unit)")
		print("2 - Naked Phone		(N14,000/unit)")
		print("3 - iphone 17		(N27,000/unit)")
		gadget_type = input("Enter 1, 2, or 3: ")
		method, delivery, shipping_cost = get_gadget_cost(gadget_type, quantity)

	# STEP 3 - Everything else chooses air or sea
	else:
		print("How do you want to ship?")
		print("1 - Air shipping (by weight in kg)")
		print("2 - Sea shipping (by dimension in cm)")
		ship_type = input("Enter 1 or 2: ")
		print("")

		if ship_type == "1":
			weight_per_unit = float(input("Weight per unit in kg: "))
			total_weight = weight_per_unit * quantity
			print("")
			print("Air shipping method:")
			print("1 - Express Air (3-5 days)")
			print("2 - Normal Air Guangzhou (10-14 days)")
			print("3 - Normal Air Hong Kong (2-3 weeks)")
			choice = input("Enter 1, 2, or 3: ")
			method, delivery, shipping_cost = get_shipping_cost(choice, total_weight, quantity, None)
		else:
			lenght = float(input("Box lenght in cm: "))
			width = float(input("Box width in cm: "))
			height = float(input("Box height in cm: "))
			cbm = round((lenght * width * height) / 1000000, 4)
			print("CBM calculated: " + str(cbm))
			print("")
			method, delivery, shipping_cost = get_shipping_cost("4", 0, quantity, cbm)

	# STEP 4 - Profit margin and result
	print("")
	margin = float(input("Target profit margin (e.g. 0.5 for 50%): "))
	total_landed = product_cost + shipping_cost
	cost_per_unit = round(total_landed / quantity, 2)
	selling_price = round(cost_per_unit / (1 - margin), 2)

	show_result(name, quantity, method, delivery, product_cost, shipping_cost, cost_per_unit, selling_price, margin)

	again = input("\nCalculate another product? (yes/no): ")
	if again.lower() != "yes":
		print("Goodbye!")
		break
