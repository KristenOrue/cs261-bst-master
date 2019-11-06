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

    def is_leaf(self):
        return not (self.has_left_child() or self.has_right_child())

    def has_left_child(self):
        return not (self.left is None)

    def has_right_child(self):
        return not (self.right is None)

    def insert(self, newNode):
        if newNode.key <= self.key and not self.is_leaf():
            # self.left = None
            # self.left = newNode.key
            # self = self.left
            # self.insert(newNode.key)
            # self.left = newNode
            self.left.insert(newNode)
            
        elif newNode.key > self.key and not self.is_leaf():
            # self.right = None
            
            self.right.insert(newNode)
            
        else:
            if newNode.key<=self.key:
                self.left = newNode
                return
            elif newNode.key>self.key:
                self.right = newNode
                return
        # if self.is_leaf():
        #     self.left = newNode
        #     return
        # else:
        #     self = self.right
        #     self.insert(newNode.key)
            

    def search(self, new_key):
        if (self.key == new_key):
            return self

    def delete(self, key):
        if key < self.key:
            if self.has_left_child():
                self.left = self.left.delete(key)
            return self #return root child of each subtree back up to root
        elif key == self.key: #base case
                if self.is_leaf():
                    return None 

        if key > self.key:
            if self.has_right_child():
                self.right = self.right.delete(key)
            return self #return root child of each subtree back up to root 
        elif key == self.key: #base case 
                if self.is_leaf():
                    return None 
                elif self.has_right_child() and not self.has_right_child():
                    return self.left
                elif self.has_right_child() and not self.has_left_child():
                    return self.right 
                else:
                    new_root = self.right.minimum()
                    new_root.right = self.right.delete(new_root.key)
                    new_root.left = self.left 
                    return new_root

    # def keys(self, order):
    #     #make empty list called result for your list of keys
    #     result = []
    #     #add the self objects key to the list
    #     for nodes in self.key:
    #         result.append(nodes)
    #     return results
    #     #if self has a left child, call key again passing in 
    #     # the left child and add the returns value to the list
    #     if self.has_left_child():
    #         self.keys_preOrder(self.left)
    #         return keys
    #         result.append()

             
    #     # if self has a right child, call key again passing in 
    #     # the right child and add the returned value to the 
    #     # result list  
    #     if self.has_right_child():
    #         self.keys_preOrder(self.right)
    #     print(self.key)
    #     keys_preorder(self.left)
    #     keys_preOrder(self.right)
         
