import csv
import datetime
from colorama import init, Fore, Style
from shipment_tracker import add_shipment, view_shipments, update_status, load_shipments
from inventory import add_item, view_inventory, load_inventory
from sales import log_sale, view_sales, load_sales
from suppliers import add_supplier, view_suppliers, load_suppliers
from dashboard import show_dashboard

init(autoreset=True)


def search_menu():
    print(Fore.YELLOW + "\n=== SEARCH ===")
    term = input("Enter tracking number or product name: ").strip().lower()

    print(Fore.CYAN + "\n--- Shipment Results ---")
    found = False
    try:
        with open("shipments.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if term in row["tracking"].lower() or term in row["description"].lower():
                    print(f"  {Fore.WHITE}{row['tracking']} | {row['method']} | {Fore.GREEN}{row['status']}{Fore.WHITE} | {row['date']}")
                    found = True
        if not found:
            print(Fore.RED + "  No shipments found.")
    except FileNotFoundError:
        print(Fore.RED + "  No shipment data yet.")

    print(Fore.CYAN + "\n--- Inventory Results ---")
    found = False
    try:
        with open("inventory.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if term in row["name"].lower():
                    print(f"  {Fore.WHITE}{row['name']} | Qty: {Fore.YELLOW}{row['quantity']}{Fore.WHITE} | Cost: ¥{row['cost_cny']} | Sell: ₦{row['sell_ngn']}")
                    found = True
        if not found:
            print(Fore.RED + "  No inventory items found.")
    except FileNotFoundError:
        print(Fore.RED + "  No inventory data yet.")


def export_report():
    today = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"report_{today}.txt"
    lines = []
    lines.append("=" * 40)
    lines.append(f"BUSINESS REPORT — {today}")
    lines.append("=" * 40)

    lines.append("\n--- SHIPMENTS ---")
    try:
        with open("shipments.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                lines.append(f"  {row['tracking']} | {row['method']} | {row['status']} | {row['date']}")
    except FileNotFoundError:
        lines.append("  No shipment data.")

    lines.append("\n--- INVENTORY ---")
    total_units = 0
    try:
        with open("inventory.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                lines.append(f"  {row['name']} | Qty: {row['quantity']} | Sell: ₦{row['sell_ngn']}")
                total_units += int(row["quantity"])
        lines.append(f"  TOTAL UNITS: {total_units}")
    except FileNotFoundError:
        lines.append("  No inventory data.")

    lines.append("\n--- SALES ---")
    total_revenue = 0.0
    try:
        with open("sales.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                lines.append(f"  {row['date']} | {row['product']} | Qty: {row['quantity']} | ₦{row['amount']}")
                total_revenue += float(row["amount"])
        lines.append(f"  TOTAL REVENUE: ₦{total_revenue:,.2f}")
    except FileNotFoundError:
        lines.append("  No sales data.")

    lines.append("\n" + "=" * 40)

    with open(filename, "w") as f:
        f.write("\n".join(lines))

    print(Fore.GREEN + f"\nReport saved as: {filename}")


def shipments_menu():
    shipments = load_shipments()
    while True:
        print(Fore.YELLOW + "\n-- SHIPMENTS --")
        print(Fore.WHITE + "1. View shipments")
        print("2. Add shipment")
        print("3. Update status")
        print("4. Back to main menu")
        c = input("Choose: ").strip()
        if c == "1":
            view_shipments(shipments)
        elif c == "2":
            add_shipment(shipments)
        elif c == "3":
            update_status(shipments)
        elif c == "4":
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter 1, 2, 3 or 4.")


def inventory_menu():
    items = load_inventory()
    while True:
        print(Fore.YELLOW + "\n-- INVENTORY --")
        print(Fore.WHITE + "1. View inventory")
        print("2. Add product")
        print("3. Back to main menu")
        c = input("Choose: ").strip()
        if c == "1":
            view_inventory(items)
        elif c == "2":
            add_item(items)
        elif c == "3":
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter 1, 2 or 3.")


def sales_menu():
    sales = load_sales()
    while True:
        print(Fore.YELLOW + "\n-- SALES --")
        print(Fore.WHITE + "1. View sales")
        print("2. Log a sale")
        print("3. Back to main menu")
        c = input("Choose: ").strip()
        if c == "1":
            view_sales(sales)
        elif c == "2":
            log_sale(sales)
        elif c == "3":
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter 1, 2 or 3.")


def suppliers_menu():
    suppliers = load_suppliers()
    while True:
        print(Fore.YELLOW + "\n-- SUPPLIERS --")
        print(Fore.WHITE + "1. View suppliers")
        print("2. Add supplier")
        print("3. Back to main menu")
        c = input("Choose: ").strip()
        if c == "1":
            view_suppliers(suppliers)
        elif c == "2":
            add_supplier(suppliers)
        elif c == "3":
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter 1, 2 or 3.")


def main():
    while True:
        print(Fore.YELLOW + "\n==== MOTUNRAYO BUSINESS TRACKER ====")
        print(Fore.WHITE + "1. Dashboard")
        print("2. Shipments")
        print("3. Inventory")
        print("4. Sales")
        print("5. Suppliers")
        print("6. Search")
        print("7. Export daily report")
        print(Fore.RED + "8. Quit")
        choice = input(Fore.WHITE + "Choose: ").strip()
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
            search_menu()
        elif choice == "7":
            export_report()
        elif choice == "8":
            print(Fore.GREEN + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 8.")


main()