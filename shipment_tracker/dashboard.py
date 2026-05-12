import csv
import os
from colorama import init, Fore, Style

init(autoreset=True)

def load_csv(filename):
    data = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    return data

def show_dashboard():
    print("\n" + Fore.YELLOW + "=" * 40)
    print(Fore.YELLOW + "   MOTUNRAYO BUSINESS DASHBOARD")
    print(Fore.YELLOW + "=" * 40)

    # Inventory
    inventory = load_csv("inventory.csv")
    total_units = sum(int(i["quantity"]) for i in inventory)
    total_cost = sum(float(i["cost_cny"]) * int(i["quantity"]) for i in inventory)
    print(Fore.CYAN + "\n INVENTORY")
    print(f"   Products:    {Fore.WHITE}{len(inventory)}")
    print(f"   Total Units: {Fore.WHITE}{total_units}")
    print(f"   Total Cost:  {Fore.WHITE}CNY {total_cost:.2f}")

    # Sales
    sales = load_csv("sales.csv")
    total_revenue = sum(float(s["amount_ngn"]) for s in sales)
    print(Fore.CYAN + "\n SALES")
    print(f"   Total Sales: {Fore.WHITE}{len(sales)}")
    print(f"   Revenue:     {Fore.GREEN}NGN {total_revenue:,.0f}")

    # Shipments
    shipments = load_csv("shipments.csv")
    in_transit = [s for s in shipments if s["status"] == "In Transit"]
    received = [s for s in shipments if s["status"] == "Received"]
    returned = [s for s in shipments if s["status"] == "Returned"]
    print(Fore.CYAN + "\n SHIPMENTS")
    print(f"   Total:       {Fore.WHITE}{len(shipments)}")
    print(f"   In Transit:  {Fore.YELLOW}{len(in_transit)}")
    print(f"   Received:    {Fore.GREEN}{len(received)}")
    print(f"   Returned:    {Fore.RED}{len(returned)}")

    # Suppliers
    suppliers = load_csv("suppliers.csv")
    print(Fore.CYAN + "\n SUPPLIERS")
    print(f"   Total:       {Fore.WHITE}{len(suppliers)}")

    print("\n" + Fore.YELLOW + "=" * 40 + "\n")

if __name__ == "__main__":
    show_dashboard()