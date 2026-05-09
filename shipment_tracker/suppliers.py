import csv
import os

FILENAME = "suppliers.csv"
FIELDS = ["name", "wechat", "product", "reliability", "notes"]

def save_suppliers(suppliers):
	with open(FILENAME, "w", newline="") as f:
		writer = csv.DictWriter(f, fieldnames=FIELDS)
		writer.writeheader()
		writer.writerows(suppliers)

def load_suppliers():
	suppliers = []
	if os.path.exists(FILENAME):
		with open(FILENAME, "r") as f:
			reader = csv.DictReader(f)
			for row in reader:
				suppliers.append(row)
	return suppliers

def add_supplier(suppliers):
	print("\n-- Add Supplier --")
	name = input("Supplier name: ")
	wechat = input("Wechat ID: ")
	product = input("Product they sell: ")
	print("Reliability: 1=Excellent 2=Good 3=Average 4=Poor")
	r = input("Choose 1-4: ")
	ratings = {"1": "Excellent", "2": "Good", "3": "Average", "4": "Poor"}
	reliability = ratings.get(r, "Unknown")
	notes = input("Notes (e.g. fast shipping, good packaging): ")
	suppliers.append({"name": name, "wechat": wechat, "product": product, "reliability": reliability, "notes": notes})
	save_suppliers(suppliers)
	print("Supplier saved!")

def view_suppliers(suppliers):
	if len(suppliers) == 0:
		print("\nNo suppliers yet.")
	else:
		print("\n--- Supplier Contacts ---")
		print(f"{'NAME':<20}{'WECHAT':<15}{'PRODUCT':<20}{'RELIABILITY':<12}NOTES")
		print("-" * 75)
		for s in suppliers:
			print(f"{s['name']:<20}{s['wechat']:<15}{s['product']:<20}{s['reliability']:<12}{s['notes']}")

def show_menu():
	print("\n==== SUPPLIERS ====")
	print("1. View suppliers")
	print("2. Add supplier")
	print("3. Quit")
	return input("Choose: ")

def main():
	suppliers = load_suppliers()
	while True:
		choice = show_menu()
		if choice == "1":
			view_suppliers(suppliers)
		elif choice == "2":
			add_supplier(suppliers)
		elif choice == "3":
			print("Goodbye!")
			break

if __name__ == "__main__":
	main()
