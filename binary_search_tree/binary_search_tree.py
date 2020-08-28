"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left: BSTNode = None
        self.right: BSTNode = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            value >= self.value
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        # # if single element
        # # compare target value to node.value
        # # if value > node.value
        # if value > self.value:
        #     # Go right
        #     # if node.right is None:
        #     if self.right is None:
        #         # Create the new node there
        #         self.right = BSTNode(value)
        #     else:  # self.right is a BSTNode
        #         # Do the same thing
        #         # Insert value into node.right
        #         right_child = self.right
        #         right_child.insert(value)
        # #           - Compare value value to node value
        # #               - If value > node.value : go right
        # #               - If value < node.value : go left
        # if value < self.value:
        #     # else if value < node.value
        #     # Go left
        #     # if node.left is None:
        #     if self.left is None:
        #         # Create the new node there
        #         self.left = BSTNode(value)
        #     else:
        #         left_child = self.left
        #         left_child.insert(value)
        # #       - Compare value value to node value
        # #               - If value > node.value : go right
        # #               - If value < node.value : go left

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Contains:
        # Compare target value to node.value
        if target == self.value:
            return True
        else:
            if target > self.value:
                # Go right
                if self.right is None:
                    # We've traversed the tree and haven't found it
                    return False
                else:
                    return self.right.contains(target)
            else:
                # Do same as above
                # Else if target < node.value
                if target < self.value:
                    # Go left
                    # if node.left is None:
                    if self.left is None:
                        # return False
                        return False
                    else:
                        # return node.left.contains(target)
                        return self.left.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
