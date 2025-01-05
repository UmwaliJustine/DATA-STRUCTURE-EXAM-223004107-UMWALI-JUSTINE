class ManufacturerNode:
    def __init__(self, name, product_catalog, price_list):
        self.name = name
        self.product_catalog = product_catalog
        self.price_list = price_list
        self.next = None  # Points to the next node (manufacturer) in the list

class ManufacturerLinkedList:
    def __init__(self):
        self.head = None

    def insert_manufacturer(self, name, product_catalog, price_list):
        """Inserts a manufacturer at the end of the list."""
        new_node = ManufacturerNode(name, product_catalog, price_list)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_manufacturer(self, name):
        """Deletes a manufacturer by name."""
        current = self.head
        if current and current.name == name:
            self.head = current.next  # Move head to next node
            current = None
            return
        prev = None
        while current and current.name != name:
            prev = current
            current = current.next
        if not current:
            print(f"Manufacturer with name {name} not found.")
            return
        prev.next = current.next
        current = None

    def search_manufacturer(self, name):
        """Search for a manufacturer by name."""
        current = self.head
        while current:
            if current.name == name:
                return current
            current = current.next
        return None

    def traverse(self):
        """Traverses the list and prints all manufacturers."""
        current = self.head
        if not current:
            print("No manufacturers in the list.")
            return
        while current:
            print(f"Manufacturer: {current.name}")
            print(f"Products: {current.product_catalog}")
            print(f"Prices: {current.price_list}")
            print("-" * 40)
            current = current.next

# Example usage:

# Create the Linked List for Manufacturers
marketplace = ManufacturerLinkedList()

# Insert manufacturers with their product catalog and prices
marketplace.insert_manufacturer("ABC Corp", ["Product1", "Product2"], [100, 150])
marketplace.insert_manufacturer("XYZ Ltd", ["Product3", "Product4"], [200, 250])

# Search for a manufacturer
manufacturer = marketplace.search_manufacturer("ABC Corp")
if manufacturer:
    print(f"Found Manufacturer: {manufacturer.name}")
    print(f"Product Catalog: {manufacturer.product_catalog}")
    print(f"Price List: {manufacturer.price_list}")
else:
    print("Manufacturer not found.")

# Display all manufacturers
marketplace.traverse()

# Delete a manufacturer
marketplace.delete_manufacturer("XYZ Ltd")
marketplace.traverse()
