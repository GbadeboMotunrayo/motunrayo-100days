
import csv
import os

FILENAME = "shipments.csv"

# WRITE - save shipments to a file
def save_shipments(shipments):
	with open(FILENAME, "w", newline="") as f:
		writer = csv.DictWriter(f, fieldnames=["tracking", "courier", "status", "weight_kg"])
		writer.writeheader()
		writer.writerows(shipments)
	print("Saved to", FILENAME)

# READ - load shipments from the files
def load_shipments():
	shipments = []
	if os.path.exists(FILENAME):
		with open(FILENAME, "r") as f:
			reader = csv.DictReader(f)
			for row in reader:
				shipments.append(row)
	return shipments

# TEST IT
my_shipments = [
	{"tracking": "78984413644029", "courier": "NBC Skye", "status": "returned", "weight_kg": "2.5"},
	{"tracking": "NBC20260001", "courier": "NBC Skye", "status": "in transit", "weight_kg": "5.0"}
]

save_shipments(my_shipments)

loaded = load_shipments()
print("\nLoaded from file:")
for s in loaded:
	print(s["tracking"], "|", s["status"])
