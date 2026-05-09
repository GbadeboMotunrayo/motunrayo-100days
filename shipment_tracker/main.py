
from shipment_tracker import add_shipment, view_shipments, update_status, load_shipments
from inventory import add_item, view_inventory, load_inventory
from sales import log_sale, view_sales, load_sales
from suppliers import add_supplier, view_suppliers, load_suppliers
from dashboard import show_dashboard

def shipments_menu():
	shipments = load_shipments()
	while True:
		print("\n-- SHIPMENTS --")
		print("1. View shipments")
		print("2. Add shipment")
		print("3. Update status")
		print("4. Back to main menu")
		c = input("Choose: ")
		if c == "1":
			view_shipments(shipments)
		elif c == "2":
			add_shipment(shipments)
		elif c == "3":
			update_status(shipments)
		elif c == "4":
			break

def inventory_menu():
	items = load_inventory()
	while True:
		print("\n-- INVENTORY --")
		print("1. View inventory")
		print("2. Add product")
		print("3. Back to main menu")
		c = input("Choose: ")
		if c == "1":
			view_inventory(items)
		elif c == "2":
			add_item(items)
		elif c == "3":
			break

def sales_menu():
	sales = load_sales()
	while True:
		print("\n-- SALES --")
		print("1. View sales")
		print("2. Log a sale")
		print("3. Back to main menu")
		c = input("Choose: ")
		if c == "1":
			view_sales(sales)
		elif c == "2":
			log_sale(sales)
		elif c == "3":
			break

def suppliers_menu():
	suppliers = load_suppliers()
	while True:
		print("\n-- SUPPLIERS --")
		print("1. View suppliers")
		print("2. Add supplier")
		print("3. Back to main menu")
		c = input("Choose: ")
		if c == "1":
			view_suppliers(suppliers)
		elif c == "2":
			add_supplier(suppliers)
		elif c == "3":
			break

def main():
	while True:
		print("\n==== MOTUNRAYO BUSINESS TRACKER ====")
		print("1. Dashboard")
		print("2. Shipments")
		print("3. Inventory")
		print("4. Sales")
		print("5. Suppliers")
		print("6. Quit")
		choice = input("Choose: ")
		if choice == "1":
			show_dashboard()
		elif choice == "2":
			shipments_menu()
		elif choice == "3":
			inventory_menu()
		elif choice == "4":
			sales_menu()
		elif choice == "5":
			suppliers_menu()
		elif choice == "6":
			print("Goodbye!")
			break

main()
