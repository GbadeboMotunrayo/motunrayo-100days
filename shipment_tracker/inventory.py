import csv
import os

FILENAME = "inventory.csv"
FIELDS = ["name", "quantity", "cost_cny", "sell_ngn"]

def save_inventory(items):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(items)

def load_inventory():
    items = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                items.append(row)
    return items

def add_item(items):
    print("\n-- Add Product --")
    name = input("Product name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return

    while True:
        try:
            qty = int(input("Quantity: "))
            if qty < 0:
                print("Quantity cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a whole number for quantity.")

    while True:
        try:
            cost = float(input("Cost price (CNY): "))
            if cost < 0:
                print("Cost cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a number for cost price.")

    while True:
        try:
            sell = float(input("Selling price (NGN): "))
            if sell < 0:
                print("Selling price cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a number for selling price.")

    items.append({"name": name, "quantity": qty, "cost_cny": cost, "sell_ngn": sell})
    save_inventory(items)
    print("Product saved!")

def view_inventory(items):
    if len(items) == 0:
        print("\nNo products yet.")
    else:
        print("\n--- Your Inventory ---")
        print(f"{'PRODUCT':<30}{'QTY':<8}{'COST(CNY)':<12}{'SELL(NGN)':<12}MARGIN%")
        print("-" * 70)
        for item in items:
            cost = float(item["cost_cny"])
            sell = float(item["sell_ngn"])
            margin = ((sell - cost) / sell) * 100
            print(f"{item['name']:<30}{item['quantity']:<8}{item['cost_cny']:<12}{item['sell_ngn']:<12}{margin:.1f}%")
        total_units = sum(int(i["quantity"]) for i in items)
        total_cost = sum(float(i["cost_cny"]) * int(i["quantity"]) for i in items)
        print("_" * 70)
        print(f"TOTAL UNITS: {total_units}    |    TOTAL COST: CNY {total_cost:.2f}")

def show_menu():
    print("\n==== INVENTORY ====")
    print("1. View inventory")
    print("2. Add product")
    print("3. Quit")
    return input("Choose: ")

def main():
    items = load_inventory()
    while True:
        choice = show_menu()
        if choice == "1":
            view_inventory(items)
        elif choice == "2":
            add_item(items)
        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()