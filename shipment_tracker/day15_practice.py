# DAY 15 - List and Dictionaries
# Motunrayo's real business data as Python structures

# A LIST - ordered collection of items
shipping_methods = ["Express Air", "Normal Air GZ", "Normal Air HK", "Sea"]

print("My shipping options:")
for method in shipping_methods:
	print("-", method)

# A DICTIONARY - stores labeled data (like a record/row)
shipment = {
	"tracking": "78984413644029",
	"courier": "NBC Skye",
	"status": "returned",
	"weight_kg": 2.5
}

print("\nShipment details:")
for key, value in shipment.items():
	print(key, ":", value)

# A LIST OF DICTIONARIES - multiple shipment records
all_shipments = [
	{
		"tracking": "78984413644029",
		"courier": "NBC Skye",
		"status": "returned",
		"weight_kg": 2.5
	},
	{
		"tracking": "NBC20260001",
		"courier": "NBC Skye",
		"status": "in transit",
		"weight_kg": 5.0
	},
	{
		"tracking": "NBC20260002",
		"courier": "NBC Skye",
		"status": "received",
		"weight_kg": 3.2
	}
]

print("\nAll shipments:")
for s in all_shipments:
	print(s["tracking"], "|", s["status"])
