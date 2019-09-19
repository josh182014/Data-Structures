# Questions:
# Only ints?
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent


class BinarySearchTree:
    def __init__(self, value):  # We're just using value, so key is value
        self.value = value
        self.left = None
        self.right = None

    # * `insert` adds the input value to the binary
    # search tree, adhering to the
    # rules of the ordering of elements in a binary search tree.
    # Need to traverse to find spot to insert
    def insert(self, value):
        if self.value is None:
            self.value = BinarySearchTree(value)
        else:
            if value >= self.value:
                if self.right is not None:
                    self.right.insert(value)
                else:
                    self.right = BinarySearchTree(value)
            elif value < self.value:
                if self.left is not None:
                    self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)
            else:
                return "Check usage."

    # * `contains` searches the binary search tree for the input value,
    # returning a boolean indicating whether the value
    # exists in the tree or not.
    # Start from root and traverse the tree
    # We can stop at the first instance of a value
    # We know it's not found if we get to a node that doesn't have children

    def contains(self, target):
        if self.value == target:
            return True
        if target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False

    # * `get_max` returns the maximum value in the binary search tree.
    def get_max(self):
        if self.value and self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # * `for_each` performs a traversal of _every_ node in the tree, executing
    # the passed-in callback function on each tree node value. There is a
    # myriad of ways to
    # perform tree traversal; in this case any of them should work.
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

# DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_dft(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
