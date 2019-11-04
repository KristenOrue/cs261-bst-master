# BinarySearchTree: A binary search tree.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_bst.py.
# YOUR NAME

class BinarySearchTree:

    def __init__(self, key = None):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, item):
        self.left = item
        self.right = item

    def search(self, new_key):
        if (self.key == new_key):
            return self
    def is_leaf(self):
        return not (self.has_left_child() or self.has_right_child())
        
    def has_left_child(self):
        return not (self.left is None)

    def has_right_child(self):
        return not (self.right is None)

    def delete(self, key):
        if key <self.key:
            if self.has_left_child():
                self.left = self.left.delete(key)
            return self #return root child of each subtree back up to root
        elif key == self.key: #base case
                if self.is_leaf():
                    return None 
        
         
