# Day 3 - NGN/CNY Currency Converter
#How much does my Chinese product cost in Naira?

# ---EXCHANGE RATE ---
cny_to_usd = 0.14        # 1 Chinese Yuan = $0.14
usd_to_ngn = 1580        # 1  usd = N1,580 (update this regularly!)

# --- PRODUCT DETAILS ---
price_in_cny =0.95       # price of one Gardenia Fragrance bottle
quantity = 2             # how many units

# --- CALCULATIONS ---
price_in_usd = price_in_cny * cny_to_usd
price_in_ngn = price_in_usd * usd_to_ngn
total_cost = price_in_ngn * quantity

# --- DISPLAY RESULTS ---
print("=== NGN/CNY CONVERTER ===")
print("Product price (CNY):", price_in_cny)
print("Price in USD:", price_in_usd)
print("Price in NGN:", price_in_ngn)
print("Quantity:", quantity)
print("Total cost in NGN:", total_cost)
