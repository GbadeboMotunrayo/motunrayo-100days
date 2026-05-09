import csv
import os
from datetime import date

FILENAME = "shipments.csv"
FIELDS = ["tracking", "courier", "method", "status", "weight_kg", "date", "description"]

def save_shipments(shipments):
	with open(FILENAME, "w", newline="") as f:
		writer = csv.DictWriter(f, fieldnames=FIELDS)
		writer.writeheader()
		writer.writerows(shipments)

def load_shipments():
	shipments =[]
	if os.path.exists(FILENAME):
		with open(FILENAME, "r") as f:
			reader = csv.DictReader(f)
			for row in reader:
				shipments.append(row)
	return shipments

def add_shipment(shipments):
	print("\n-- Add New Shipment --")
	t = input("Tracking number: ")
	c = input("Courier (e.g. NBC Skye): ")
	print("Shipping method: 1=Sea 2=Express Air 3=Normal Air GZ 4=Normal Air HK")
	m_choice = input("Choose 1-4: ")
	methods = {"1": "Sea", "2": "Express Air", "3": "Normal Air GZ", "4": "Normal Air HK"}
	m = methods.get(m_choice, "Unknown")
	print("Status: 1=In Transit 2=Received 3=Returned")
	s_choice = input("Choose 1-3: ")
	statuses = {"1": "In Transit", "2": "Received", "3": "Returned"}
	s = statuses.get(s_choice, "Unknown")
	w = input("Weight in kg (or 0 for sea): ")
	d = input("Date sent (e.g. 2026-04-28): ")
	desc = input("Description (e.g. Gardenia oils 330 units): ")
	shipments.append({
		"tracking": t,
		"courier": c,
		"method": m,
		"status": s,
		"weight_kg": w,
		"date": d,
		"description": desc
	})
	save_shipments(shipments)
	print("Shipment saved!")

def view_shipments(shipments):
	if len(shipments) == 0:
		print("\nNo shipment yet.")
	else:
		print("\n--- Your Shipments ---")
		print(f"{'DATE':<12}{'TRACKING':<16}{'METHOD':<10}{'STATUS':<12}DESCRIPTION")
		print("-" * 70)
		for s in shipments:
			print(f"{s['date']:<12}{s['tracking']:<16}{s['method']:<10}{s['status']:<12}{s['description']}")

def update_status(shipments):
	tracking = input("\nEnter tracking number to update: ")
	for s in shipments:
		if s["tracking"] == tracking:
			print("Status: 1=In Transit 2=Received 3=Returned")
			choice = input("Choose 1-3: ")
			statuses = {"1": "In Transit", "2": "Received", "3": "Returned"}
			s["status"] = statuses.get(choice, s["status"])
			save_shipments(shipments)
			print("Status updated!")
			return
	print("Tracking number not found.")

def show_menu():
	print("\n==== SHIPMENT TRACKER ====")
	print("1. View all shipments")
	print("2. Add new shipment")
	print("3. Update shipment status")
	print("4. Quit")
	return input("Choose: ")

def main():
	shipments = load_shipments()
	while True:
		choice = show_menu()
		if choice == "1":
			view_shipments(shipments)
		elif choice == "2":
			add_shipment(shipments)
		elif choice == "3":
			update_status(shipments)
		elif choice == "4":
			print("Goodbye!")
			break

if __name__ == "__main__":
	main()
