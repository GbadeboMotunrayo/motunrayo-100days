# Day 4 - Shipping Method Choice with if/else
# NBC Skye Logistics rates

# --- EXCHANGE RATE ---
usd_to_ngn = 1580

# --- NBC SKYE RATES (per kg) ---
express_air_usd = 14
express_air_customs = 1300

normal_air_gz_usd = 10.5
normal_air_customs = 1000

normal_air_hk_usd = 11.9
normal_air_hk_customs =1000

# --- USER INPUTS ---
weight = float(input("Enter shipment weight in kg: "))

print("")
print("1 - Express Air ($14/kg, 3-5 days)")
print("2 - Normal Air Guangzhou ($10.5/kg, 10-14 days)")
print("3 - Normal Air Hong Kong ($11.9/kg, 2-3 weeks)")
print("")

choice = input("Enter 1, 2 or 3: ")

# --- CALCULATE BASED ON CHOICE ---
if choice == "1":
	freight = weight * express_air_usd * usd_to_ngn
	customs = weight * express_air_customs
	method = "Express Air"
	days = "3-5 days"
elif choice == "2":
	freight = weight * normal_air_gz_usd * usd_to_ngn
	customs = weight * normal_air_gz_customs
	method = "Normal Air Guangzhou"
	days = "10-14 days"
elif choice == "3":
	freight = weight * normal_air_hk_usd * usd_to_ngn
	customs = weight * normal_air_hk_customs
	method = "Normal Air Hong Kong"
	days = "2-3 weeks"
else:
	print("Invalid choice. Please enter 1, 2 or 3.")

# --- DISPLAY RESULTS ---
print("")
print("=== SHIPPING COST ESTIMATE ===")
print("Method:", method)
print("Weight:", weight, "kg")
print("Freight cost (NGN):", freight)
print("Customs clearing (NGN):", customs)
print("Total shipping (NGN):", freight + customs)
print("Estimated delivery:", days)
