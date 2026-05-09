import csv
import os

def load_csv(filename):
	data = []
	if os.path.exists(filename):
		with open(filename, "r") as f:
			reader = csv.DictReader(f)
			for row in reader:
				data.append(row)
	return data

def show_dashboard():
	print("\n========================================")
	print("		MOTUNRAYO BUSINESS DASHBOARD")
	print("========================================")

	# Inventory
	inventory = load_csv("inventory.csv")
	total_units = sum(int(i["quantity"]) for i in inventory)
	total_cost = sum(float(i["cost_cny"]) * int(i["quantity"]) for i in inventory)
	print(f"\n INVENTORY")
	print(f"	Products:	{len(inventory)}")
	print(f"	Total Units:	{total_units}")
	print(f"	Total Cost:	CNY {total_cost:.2f}")

	#Sales
	sales = load_csv("sales.csv")
	total_revenue = sum(float(s["amount_ngn"]) for s in sales)
	print(f"\n SALES")
	print(f"	Total Sales:	{len(sales)}")
	print(f"	Revenue:	NGN {total_revenue:,.0f}")

	#Shipments
	shipments = load_csv("shipments.csv")
	in_transit = [s for s in shipments if s["status"] == "In Transit"]
	received = [s for s in shipments if s["status"] == "Received"]
	returned = [s for s in shipments if s["status"] == "Returned"]
	print(f"\n SHIPMENTS")
	print(f" 	Total		{len(shipments)}")
	print(f"	In Transit:	{len(in_transit)}")
	print(f"	Received:	{len(received)}")
	print(f"	Returned:	{len(returned)}")

	# Suppliers
	suppliers = load_csv("suppliers.csv")
	print(f"\n SUPPLIERS")
	print(f"	Total:		{len(suppliers)}")

	print("\n========================================\n")

if __name__ == "__main__":
	show_dashboard()
