# WAP to use the map() function to apply a user-defined function to every element of a list and store the processed results in a new list.




# Function to process a single item
def grind_bean(bean_name):
    return f"{bean_name} Powder ☕"

# Input list containing raw items
raw_beans = ["Arabica", "Robusta", "Liberica"]

# Using map() to apply the function to the entire list without a loop
processed_coffee = list(map(grind_bean, raw_beans))

# Displaying the final result
print("Processed Items:", processed_coffee)