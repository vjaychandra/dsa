class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert_node(self, root, node):

        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                self.insert_node(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                self.insert_node(root.left, node)

    def insert_node(self, node):

        curr = self.root

        while curr:
            if node.data > curr.data:
                if not curr.right:
                    curr.right = node
                    break
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = node
                    break
                curr = curr.left
        

    def min(self):
        element = self.root
        while element:
            element = element.left
        return element.data 

    def max(self):
        element = self.root
        while element:
            element = element.right
        return element.data

    def pre_order(self, root):
        if root:
            print(root.data)
            self.in_order(root.left)
            self.in_order(root.right)

    def preorder(self):
        
        stack = []
        stack.append(self.root)

        while len(stack) > 0:
            current = stack.pop()
            print(current.data)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            
    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)

    def inorder(self):

        # push -> left
        # pop -> right

        stack = []
        op = []
        current = self.root

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                op.append(current.data)
                current = current.right
            else:
                break
        print(op)

    def post_order(self, root):

        if root:
            self.in_order(root.left)
            self.in_order(root.right)
            print(root.data)

    def postorder(self):
        pass

    def max_depth(self, node=None):

        if not node:
            return 0

        return 1 + max(self.max_depth(node.left), self.max_depth(node.right))



array = [5, 2, 7, 6, 3, 8, 1, 0]

bt = BinaryTree()
bt.root = Node(array[0])

for item in array[1:]:
    node = Node(item)
    #bt.insert_node(bt.root, node)
    bt.insert_node(node)

print(bt.max_depth(bt.root))
#bt.pre_order(bt.root)
#bt.preorder()
#bt.inorder()
#bt.post_order(bt.root)
#bt.postorder()
