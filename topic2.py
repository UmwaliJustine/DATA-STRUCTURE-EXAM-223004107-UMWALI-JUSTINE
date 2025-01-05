# --- Binary Search Tree (BST) for managing Products ---
class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, product):
        """Insert a product into the BST."""
        if self.root is None:
            self.root = product
        else:
            self._insert_recursive(self.root, product)

    def _insert_recursive(self, node, product):
        """Helper method for inserting recursively."""
        if product.product_id < node.product_id:
            if node.left is None:
                node.left = product
            else:
                self._insert_recursive(node.left, product)
        elif product.product_id > node.product_id:
            if node.right is None:
                node.right = product
            else:
                self._insert_recursive(node.right, product)

    def search(self, product_id):
        """Search for a product by its ID."""
        return self._search_recursive(self.root, product_id)

    def _search_recursive(self, node, product_id):
        """Helper method for searching recursively."""
        if node is None:
            return None
        if node.product_id == product_id:
            return node
        elif product_id < node.product_id:
            return self._search_recursive(node.left, product_id)
        else:
            return self._search_recursive(node.right, product_id)

    def inorder_traversal(self):
        """Inorder traversal to get products in sorted order."""
        products = []
        self._inorder_recursive(self.root, products)
        return products

    def _inorder_recursive(self, node, products):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, products)
            products.append(node)
            self._inorder_recursive(node.right, products)

# --- Singly Linked List (SLL) for managing Orders ---
class Order:
    def __init__(self, order_id, manufacturer_name, total_amount):
        self.order_id = order_id
        self.manufacturer_name = manufacturer_name
        self.total_amount = total_amount
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_order(self, order):
        """Add an order to the end of the list."""
        if not self.head:
            self.head = order
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = order

    def display_orders(self):
        """Display all orders."""
        current = self.head
        while current:
            print(f"Order(ID: {current.order_id}, Manufacturer: {current.manufacturer_name}, Total: {current.total_amount})")
            current = current.next

    def remove_order(self, order_id):
        """Remove an order by its ID."""
        if not self.head:
            print("No orders in the list.")
            return

        if self.head.order_id == order_id:
            self.head = self.head.next
            print(f"Order {order_id} removed.")
            return

        current = self.head
        while current.next:
            if current.next.order_id == order_id:
                current.next = current.next.next
                print(f"Order {order_id} removed.")
                return
            current = current.next

        print(f"Order {order_id} not found.")

    def search_order(self, order_id):
        """Search for an order by its ID."""
        current = self.head
        while current:
            if current.order_id == order_id:
                print(f"Order found: Order(ID: {current.order_id}, Manufacturer: {current.manufacturer_name}, Total: {current.total_amount})")
                return current
            current = current.next
        print(f"Order {order_id} not found.")
        return None

# for example usage

# --- 1. BST for Managing Products ---
print("\n--- Managing Products in BST ---")
product_bst = BST()

# Create products
product1 = Product(101, "Smartphone", 500)
product2 = Product(102, "Laptop", 1200)
product3 = Product(103, "Headphones", 150)
product4 = Product(104, "Smartwatch", 250)

# Insert products into BST
product_bst.insert(product1)
product_bst.insert(product2)
product_bst.insert(product3)
product_bst.insert(product4)

# Search for a product by ID
found_product = product_bst.search(102)
if found_product:
    print(f"Product found: {found_product.product_name} - ${found_product.price}")
else:
    print("Product not found.")

# Inorder traversal of BST to get sorted products
sorted_products = product_bst.inorder_traversal()
print("\nProducts in Sorted Order:")
for product in sorted_products:
    print(f"{product.product_name} - ${product.price}")

# --- 2. SLL for Managing Orders ---
print("\n--- Managing Orders in Singly Linked List ---")
order_list = SinglyLinkedList()

# Create orders
order1 = Order(1, "ABC Corp", 1000)
order2 = Order(2, "XYZ Ltd", 2500)
order3 = Order(3, "LMN Inc", 3000)

# Add orders to SLL
order_list.add_order(order1)
order_list.add_order(order2)
order_list.add_order(order3)

# Display all orders
print("\nAll Orders:")
order_list.display_orders()

# Remove an order
order_list.remove_order(2)  # Remove order with ID 2

# Display orders after removal
print("\nOrders after removal:")
order_list.display_orders()

# Search for a specific order
order_list.search_order(3)  # Search for order with ID 3

# Try removing a non-existing order
order_list.remove_order(4)  # Try removing order with ID 4 (not found)
