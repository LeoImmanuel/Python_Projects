
class TreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.value)
        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.value)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.value)

    def find_element(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find_element(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find_element(value)

    def find_min(self):
        if self.left:
            self.left.find_min()
        else:
            print(self.value)

    def find_max(self):
        if self.right:
            self.right.find_max()
        else:
            print(self.value)

    def Kth_smallest(self,k):
        # Helper function to perform in-order traversal
        def in_order_tra(node, result):
            if node is None or len(result) >= k:
                return
            in_order_tra(node.left, result)
            if len(result) < k:
                result.append(node.value)
            in_order_tra(node.right, result)

        result = []
        in_order_tra(self, result)

        if len(result) < k:
            return None  # Not enough elements for a Kth element
        return result[k-1]  # Return the Kth Kth element

    def unquiekelement(self,k):
        def in_ordertraversalhelper(node,result_unique):
            if node is None or len(result_unique) >= k:
                return
            in_ordertraversalhelper(node.left,result_unique)
            if node.value not in result_unique:
                result_unique.append(node.value)
            in_ordertraversalhelper(node.right,result_unique)

        result_unique = []
        in_ordertraversalhelper(self,result_unique)

        if len(result_unique) < k:
            return None
        return result_unique[k-1]






tree = TreeNode(6)
tree.insert(5)
tree.insert(13)
tree.insert(7)
tree.insert(4)
tree.insert(3)
tree.insert(2)
tree.insert(29)
tree.insert(11)
tree.insert(2)
tree.insert(2)
tree.insert(1)


k=4
print("Kth smallest value in the BST:", tree.Kth_smallest(k))
print()
print("Kth Unique smallest value in the BST:", tree.unquiekelement(k))

"""

print("In-Order traversal of BST: ")
tree.in_order_traversal()

print("Pre-Order traversal of BST: ")
tree.pre_order_traversal()

print("Post-Order traversal of BST: ")
tree.post_order_traversal()

n = 3
print(f"The element to be searched in BST is: {n}")

if tree.find_element(n):
    print("Element is found")
else:
    print("Not found")
    
"""

"""

class TreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.content = None

    def insert(self, value, content=None):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
                self.left.content = content
            else:
                self.left.insert(value, content)
        else:
            if self.right is None:
                self.right = TreeNode(value)
                self.right.content = content
            else:
                self.right.insert(value, content)

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.value)
        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.value)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.value)

    def find_element(self, value):
        if value == self.value:
            return self
        elif value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find_element(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find_element(value)



tree = TreeNode(6)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(19,{"data":"Leo"})
tree.insert(29)
tree.insert(11)
tree.insert(4)
tree.insert(2)

print(tree.find_element(19).content['data'])


"""