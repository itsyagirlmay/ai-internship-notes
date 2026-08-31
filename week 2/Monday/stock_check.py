
# Creating a dictionary called items containing grocery names and quantities
# "bread" is given an intentional bad value ("five") to test the error handling
items = {
    "apples": 15,
    "bananas": 3,
    "milk": 8,
    "bread": "five"  # Intentional bad value
}

# For the system to know when to reorder, set a threshold value for reordering
reorder_threshold = 5

# A FOR loop to go through each item and quantity in the dictionary one by one:
for item, quantity in items.items():

    try:
        # CHECK whether the quantity is a valid number by converting it to an integer
        valid_quantity = int(quantity)

        if valid_quantity < reorder_threshold:
            print(f"{item.capitalize()} needs to be reordered (Current stock: {valid_quantity})")
        else:
            print(f"{item.capitalize()} has sufficient stock (Current stock: {valid_quantity})")

    # Except if the quantity causes an error (like trying to convert "five" to an integer)
    except ValueError as error:
        print(f"{item.capitalize()} has invalid stock data")
        print(f"   Error Message: {error}")


