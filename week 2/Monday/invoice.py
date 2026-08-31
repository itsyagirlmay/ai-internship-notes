from datetime import datetime

#I set my birthdate as the specific datetime
specific_dt = datetime(2026, 9, 26, 12, 0, 0)
formatted_date = specific_dt.strftime("%Y-%m-%d")

#Grocery items with their respective prices
groceries = {
    "apples": 69.99,
    "bananas": 11.99,
    "milk": 40.99,
    "bread": 15.99
}

# Calculating the price before VAT is added (assuming quantity of 1 for each item)
subtotal = sum(groceries.values())

# Setting tax rate (e.g., 15% VAT)
tax_rate = 0.15

# Calculating tax
tax = subtotal * tax_rate

# Calculating total
total = subtotal + tax

# Print formatting for the receipt
print("=" * 40)
print(f"RECEIPT - DATE: {formatted_date}")
print("=" * 40)

# Print each line item and its price
for item, price in groceries.items():
    print(f"{item.capitalize():<15} 1 x N${price:.2f} = N${price:.2f}")

print("-" * 40)

# Print subtotal, tax, and total
print(f"{'Subtotal:':<25} N${subtotal:.2f}")
print(f"{'Tax (' + str(int(tax_rate*100)) + '%):':<25} N${tax:.2f}")
print("-" * 40)
print(f"{'Total:':<25} N${total:.2f}")
print("=" * 40)


