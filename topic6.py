class TreeNode:
    def __init__(self, name):
        self.name = name  # Name of the node (e.g., manufacturer name, product category)
        self.children = []  # List of child nodes (e.g., subcategories, products)

    def add_child(self, child_node):
        """Add a child node to the current node."""
        self.children.append(child_node)

    def display(self, level=0):
        """Recursively display the node and its children."""
        print("  " * level + self.name)
        for child in self.children:
            child.display(level + 1)


class Tree:
    def __init__(self, root_name):
        self.root = TreeNode(root_name)  # Root of the tree (e.g., "Manufacturers")

    def get_root(self):
        """Return the root of the tree."""
        return self.root

    def find_node(self, node_name):
        """Find and return a node by its name (recursive search)."""
        return self._find_node_recursive(self.root, node_name)

    def _find_node_recursive(self, current_node, node_name):
        """Helper method for recursive search."""
        if current_node.name == node_name:
            return current_node
        for child in current_node.children:
            found_node = self._find_node_recursive(child, node_name)
            if found_node:
                return found_node
        return None

    def add_child_to_node(self, parent_name, child_node):
        """Add a child node to a specific parent node."""
        parent_node = self.find_node(parent_name)
        if parent_node:
            parent_node.add_child(child_node)
            print(f"Child node '{child_node.name}' added under parent '{parent_name}'.")
        else:
            print(f"Parent node '{parent_name}' not found.")


# Example Usage:

# Create the tree structure for manufacturers and products
marketplace_tree = Tree("Manufacturers")

# Create nodes for manufacturers
abc_corp = TreeNode("ABC Corp")
xyz_ltd = TreeNode("XYZ Ltd")

# Add manufacturer nodes under "Manufacturers"
marketplace_tree.get_root().add_child(abc_corp)
marketplace_tree.get_root().add_child(xyz_ltd)

# Create product categories for ABC Corp
electronics = TreeNode("Electronics")
home_appliances = TreeNode("Home Appliances")

# Add product categories to ABC Corp and XYZ Ltd
abc_corp.add_child(electronics)
xyz_ltd.add_child(home_appliances)

# Add products to product categories
smartphones = TreeNode("Smartphones")
laptops = TreeNode("Laptops")
refrigerators = TreeNode("Refrigerators")
washing_machines = TreeNode("Washing Machines")

electronics.add_child(smartphones)
electronics.add_child(laptops)
home_appliances.add_child(refrigerators)
home_appliances.add_child(washing_machines)

# Display the entire hierarchical structure
print("Marketplace Hierarchical Structure:")
marketplace_tree.get_root().display()

# Search for a specific node (e.g., "Electronics")
node = marketplace_tree.find_node("Electronics")
if node:
    print(f"\nFound node: {node.name}")
else:
    print("\nNode not found.")

# Add a new category under a manufacturer (e.g., add "Clothing" under XYZ Ltd)
clothing = TreeNode("Clothing")
marketplace_tree.add_child_to_node("XYZ Ltd", clothing)

# Display the updated tree
print("\nUpdated Marketplace Hierarchical Structure:")
marketplace_tree.get_root().display()
