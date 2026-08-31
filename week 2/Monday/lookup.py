# Import pandas to confirm it is correctly accessible in this virtual environment
import pandas as pd
from datetime import datetime

print(f"--- Pandas Version: {pd.__version__} successfully imported! ---\n")

#Defining the function()lookup_item(items_dictionary, item_name):
def lookup_item(items_dictionary, item_name):
    try:
        #Map the value associated with item_name from items_dictionary; this will raise a KeyError if item_name is missing
        value = items_dictionary[item_name]

        #Checks that the retrieved value is valid;to ensure it can be converted to an integer and isn't a bad string/None
        if value is None:
            raise ValueError("Stock value cannot be None")
        
        valid_value = int(value)

        #Returns the item's value
        return valid_value

    # Except error if item_name does not exist in the dictionary:
    except KeyError:
        print("Error: Item not found")
        return None

    # Except the errors if the input/value is invalid:
    except (ValueError, TypeError):
        print("Error: Invalid input/stock data")
        return None


#the stock items dictionary (using our grocery example)
grocery_stock = {
    "apples": 15,
    "bananas": 3,
    "milk": "Corrupted Data",  # Invalid value to trigger the second exception
    "bread": 8
}

#looking up a valid item
print("--- Looking up 'apples' ---")
result_1 = lookup_item(grocery_stock, "apples")
print(f"Returned Result: {result_1}\n")

#looking up an item that does not exist in the dictionary
print("--- Looking up 'oranges' ---")
result_2 = lookup_item(grocery_stock, "oranges")
print(f"Returned Result: {result_2}\n")

#looking up an item with invalid stock data
print("--- Looking up 'milk' ---")
result_3 = lookup_item(grocery_stock, "milk")
print(f"Returned Result: {result_3}\n")
