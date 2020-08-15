from queue import Queue

class BinaryTree(object):

    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None

    def insert_left(self, data):

        if self.root is None:
            self.root = BinaryTree(data)
        else:
            node = BinaryTree(data)
            node.left = self.left
            self.left = node

    def insert_right(self, data):

        if self.root is None:
            self.root = BinaryTree(data)
        else:
            node = BinaryTree(data)
            node.right = self.right
            self.right = node

    def bfs(self):

        queue = Queue()
        queue.put(self)

        while not queue.empty():
            node = queue.get()
            print(f"Value: {node.root}")            
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)


    def leaf_nodes(self):

        op = []
        count = 0
        max_level = 0

        queue = Queue()
        queue.put((self, count))
        
        while not queue.empty():

            node, count = queue.get()
            print(f"{count-1} Value: {node.root}")
            count += 1

            if node.left:
                queue.put((node.left, count))
            if node.right:
                queue.put((node.right, count))
                

    def pre_order(self):
        print(self.root)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.root)

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.root)
        if self.right:
            self.right.in_order()


    def is_balanced(self, root):

        if not root:
            return True

        if not root.left and not root.right:
            return False

        return self.is_balanced(root.left) or self.is_balanced(root.right)



if __name__ == "__main__":
    a_node = BinaryTree('a')
    a_node.insert_left('b')
    a_node.insert_right('c')

    b_node = a_node.left
    b_node.insert_left('d')
    b_node.insert_right('h')

    c_node = a_node.right
    c_node.insert_left('e')
    c_node.insert_right('f')

    #d_node = b_node.right
    #e_node = c_node.left
    #f_node = c_node.right

    a_node.bfs()
