import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

    # Insert the given value into the tree
    def insert(self, value):
        # compare root node
        # if lesser go left child
        # if greater go right child
        # BEGS FOR RECURSION
        if self.value is None:
            BinarySearchTree(value)
        ## If the value is greater than or equal to self.value, go to the right
        # old way
        # elif value >= self.value and self.right is None:
        #     self.right = BinarySearchTree(value)
        # new way
        if value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        ## If the value is less than self.value, go to the left
        # old way
        # elif value < self.value and self.left is None:
        #     self.left = BinarySearchTree(value)
        # new way
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        ## If the value is none, set self.value to value

    # Return True if the tree contains the value
    # False if it does not
    # YOU MUST RETURN THE RECURSIVE FUNCTION
    def contains(self, target):
        if target is self.value:
            return True
        elif target >= self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        ## recursive version
        # if not self.right:
        #     return self.value
        # else:
        #     return self.right.get_max()

        # iteration version
        max_value = self.value
        current_value = self
        while current_value:
            if current_value.value > max_value:
                max_value = current_value.value
            current_value = current_value.right
        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        print(self.value)
        if self.left:
            self.left.in_order_print(node)
        if self.right:
            self.right.in_order_print(node)
        

    # QUEUE
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # STACK
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
