class Order:
    def __init__(self, order_id, manufacturer_name, product_list, quantity_list, price_list):
        self.order_id = order_id
        self.manufacturer_name = manufacturer_name
        self.product_list = product_list
        self.quantity_list = quantity_list
        self.price_list = price_list
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        """Calculates the total price for the order."""
        total = 0
        for qty, price in zip(self.quantity_list, self.price_list):
            total += qty * price
        return total

    def display_order(self):
        """Displays order details."""
        print(f"Order ID: {self.order_id}")
        print(f"Manufacturer: {self.manufacturer_name}")
        print(f"Products: {self.product_list}")
        print(f"Quantities: {self.quantity_list}")
        print(f"Prices: {self.price_list}")
        print(f"Total Price: {self.total_price}")
        print("-" * 40)


class OrderArrayManager:
    def __init__(self, max_orders):
        """Initializes the order array with a fixed size."""
        self.max_orders = max_orders
        self.orders = [None] * max_orders  # Initialize a fixed-size array
        self.current_index = 0

    def add_order(self, order_id, manufacturer_name, product_list, quantity_list, price_list):
        """Adds an order to the array if there is space."""
        if self.current_index < self.max_orders:
            order = Order(order_id, manufacturer_name, product_list, quantity_list, price_list)
            self.orders[self.current_index] = order
            self.current_index += 1
            print(f"Order {order_id} added successfully.")
        else:
            print("Order array is full, cannot add more orders.")

    def get_order(self, order_id):
        """Finds and returns an order by its ID."""
        for order in self.orders:
            if order and order.order_id == order_id:
                return order
        return None

    def remove_order(self, order_id):
        """Removes an order by its ID."""
        for i in range(self.max_orders):
            if self.orders[i] and self.orders[i].order_id == order_id:
                self.orders[i] = None
                print(f"Order {order_id} removed successfully.")
                return
        print(f"Order {order_id} not found.")

    def display_orders(self):
        """Displays all orders in the array."""
        for order in self.orders:
            if order:
                order.display_order()
            else:
                print("Empty slot.")
                print("-" * 40)


# Example Usage:

# Create the OrderArrayManager with a capacity of 3 orders
order_manager = OrderArrayManager(3)

# Add orders
order_manager.add_order(1, "ABC Corp", ["Product1", "Product2"], [10, 5], [100, 150])
order_manager.add_order(2, "XYZ Ltd", ["Product3", "Product4"], [20, 10], [200, 250])
order_manager.add_order(3, "LMN Inc", ["Product5"], [30], [300])

# Attempt to add a 4th order (should fail as the array is full)
order_manager.add_order(4, "DEF Co", ["Product6"], [15], [400])

# Display all orders
order_manager.display_orders()

# Get and display a specific order
order = order_manager.get_order(2)
if order:
    order.display_order()
else:
    print("Order not found.")

# Remove an order
order_manager.remove_order(2)
order_manager.display_orders()
