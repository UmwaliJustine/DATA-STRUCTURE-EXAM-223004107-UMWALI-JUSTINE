class Order:
    def __init__(self, order_id, manufacturer_name, priority):
        self.order_id = order_id
        self.manufacturer_name = manufacturer_name
        self.priority = priority

    def __repr__(self):
        """Custom representation for displaying the order."""
        return f"Order(ID: {self.order_id}, Manufacturer: {self.manufacturer_name}, Priority: {self.priority})"


def insertion_sort(orders):
    """Sorts the orders based on priority using Insertion Sort."""
    for i in range(1, len(orders)):
        key = orders[i]
        j = i - 1
        
        # Move elements of orders[0..i-1] that have higher priority to one position ahead of their current position
        while j >= 0 and orders[j].priority < key.priority:
            orders[j + 1] = orders[j]
            j -= 1
        
        orders[j + 1] =

# Create some sample orders with priorities
orders = [
    Order(1, "ABC Corp", 3),  # Order ID 1, Priority 3
    Order(2, "XYZ Ltd", 5),   # Order ID 2, Priority 5
    Order(3, "LMN Inc", 2),   # Order ID 3, Priority 2
    Order(4, "PQR Enterprises", 8), # Order ID 4, Priority 8
    Order(5, "DEF Co", 1),    # Order ID 5, Priority 1
]

print("Before Sorting:")
for order in orders:
    print(order)

# Sort the orders based on priority using Insertion Sort
insertion_sort(orders)

print("\nAfter Sorting (by Priority):")
for order in orders:
    print(order)
