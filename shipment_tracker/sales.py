import csv
import os
from datetime import date

FILENAME = "sales.csv"
FIELDS = ["date", "product", "quantity", "amount_ngn"]

def save_sales(sales):
	with open(FILENAME, "w", newline="") as f:
		writer = csv.DictWriter(f, fieldnames=FIELDS)
		writer.writeheader()
		writer.writerows(sales)

def load_sales():
	sales = []
	if os.path.exists(FILENAME):
		with open(FILENAME, "r") as f:
			reader = csv.DictReader(f)
			for row in reader:
				sales.append(row)
	return sales

def log_sale(sales):
	print("\n-- Log a Sale --")
	today = str(date.today())
	d = input(f"Date (press Enter for today {today}): ")
	if d == "":
		d = today
	product = input("Product sold: ")
	qty = input("Quantity sold: ")
	amount = input("Amount received (NGN): ")
	sales.append({"date": d, "product": product, "quantity": qty, "amount_ngn": amount})
	save_sales(sales)
	print("Sale recorded!")

def view_sales(sales):
	if len(sales) == 0:
		print("\nNo sales yet.")
	else:
		print("\n--- Sales log ---")
		print(f"{'DATE':<12}{'PRODUCT':<30}{'QTY':<6}AMOUNT(NGN)")
		print("-" * 65)
		for s in sales:
			print(f"{s['date']:<12}{s['product']:<30}{s['quantity']:<6}{s['amount_ngn']}")
		total = sum(float(s["amount_ngn"]) for s in sales)
		print("-" * 65)
		print(f"TOTAL REVENUE: NGN { total:,.0f}")

def show_menu():
	print("\n====SALES LOG ====")
	print("1. View all sales")
	print("2. Log a sale")
	print("3. Quit")
	return input("Choose: ")

def main():
	sales = load_sales()
	while True:
		choice = show_menu()
		if choice == "1":
			view_sales(sales)
		elif choice == "2":
			log_sale(sales)
		elif choice == "3":
			print("Goodbye!")
			break

if __name__ == "__main__":
	main()
