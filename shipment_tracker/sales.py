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
    d = input(f"Date (press Enter for today {today}): ").strip()
    if d == "":
        d = today

    product = input("Product sold: ").strip()
    if not product:
        print("Product name cannot be empty.")
        return

    while True:
        try:
            qty = int(input("Quantity sold: "))
            if qty <= 0:
                print("Quantity must be greater than zero.")
            else:
                break
        except ValueError:
            print("Please enter a whole number for quantity.")

    while True:
        try:
            amount = float(input("Amount received (NGN): "))
            if amount < 0:
                print("Amount cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a number for amount.")

    sales.append({"date": d, "product": product, "quantity": qty, "amount_ngn": amount})
    save_sales(sales)
    print("Sale recorded!")

def view_sales(sales):
    if len(sales) == 0:
        print("\nNo sales yet.")
    else:
        print("\n--- Sales Log ---")
        print(f"{'DATE':<12}{'PRODUCT':<30}{'QTY':<6}AMOUNT(NGN)")
        print("-" * 65)
        for s in sales:
            print(f"{s['date']:<12}{s['product']:<30}{s['quantity']:<6}{s['amount_ngn']}")