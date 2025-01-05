import heapq

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

    def __lt__(self, other):
        """Defines how to compare two orders for heap ordering."""
        return self.total_price < other.total_price

    def __repr__(self):
        """Custom representation for printing the order."""
        return f"Order({self.order_id}, {self.manufacturer_name}, {self.total_price})"


class MarketplaceHeap:
    def __init__(self):
        self.heap = []  # This will store the orders in the heap

    def add_order(self, order):
        """Adds an order to the heap."""
        heapq.heappush(self.heap, order)
        print(f"Order {order.order_id} added to the heap.")

    def remove_order(self):
        """Removes and returns the order with the lowest price (min-heap)."""
        if self.heap:
            order = heapq.heappop(self.heap)
            print(f"Order {order.order_id} removed from the heap.")
            return order
        else:
            print("No orders in the heap.")
            return None

    def get_top_order(self):
        """Returns the order with the lowest price (min-heap)."""
        if self.heap:
            return self.heap[0]
        else:
            print("No orders in the heap.")
            return None

    def display_orders(self):
        """Displays all orders in the heap."""
        if self.heap:
            print("Orders in the heap:")
            for order in self.heap:
                print(order)
        else:
            print("No orders in the heap.")


# Example Usage:

# Create the MarketplaceHeap (min-heap)
marketplace_heap = MarketplaceHeap()

# Create orders
order1 = Order(1, "ABC Corp", ["Product1", "Product2"], [10, 5], [100, 150])
order2 = Order(2, "XYZ Ltd", ["Product3", "Product4"], [20, 10], [200, 250])
order3 = Order(3, "LMN Inc", ["Product5"], [30], [300])

# Add orders to the heap
marketplace_heap.add_order(order1)
marketplace_heap.add_order(order2)
marketplace_heap.add_order(order3)

# Display all orders in the heap
marketplace_heap.display_orders()

# Get and display the order with the lowest price
top_order = marketplace_heap.get_top_order()
if top_order:
    print(f"The top order is: {top_order}")

# Remove the top order (the one with the lowest price)
removed_order = marketplace_heap.remove_order()
if removed_order:
    print(f"Removed order: {removed_order}")

# Display remaining orders
marketplace_heap.display_orders()

