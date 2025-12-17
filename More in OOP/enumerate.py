class Inventory:

    def __init__(self, items):

        self.items = items

    def display_inventory_list(self):

        print("Current Inventory:")

# Use enumerate to get both the index (i) and the item (product)

# The 'start=1' parameter makes the count user-friendly, starting from 1

        for i, product in enumerate(self.items, start=1):

            print(f"{i}. {product}")

# Create an object (instance) of the Inventory class

groceries = Inventory(['apples', 'bananas', 'cherries'])

# Call the method that uses enumerate()

groceries.display_inventory_list()