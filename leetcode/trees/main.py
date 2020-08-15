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

    def level_order(self):

        op = []
        queue = [self]
        while len(queue) > 0:
            temp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.root)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            op.append(temp)
                    
        print(f"Height: {len(op)}", op)


    def height(self, root):

        if root is None:
            return 0
        
        return 1 + max(self.height(root.left), self.height(root.right))


    def is_balanced(self, root):

        if not root:
            return True

        if not root.left and not root.right:
            return False

        return self.is_balanced(root.left) or self.is_balanced(root.right)
                


if __name__ == "__main__":
    a_node = BinaryTree('3')
    a_node.insert_left('9')
    a_node.insert_right('20')

    b_node = a_node.left
    b_node.insert_left('12')
    b_node.insert_right('11')

    c_node = a_node.right
    c_node.insert_left('15')
    c_node.insert_right('7')

    #d_node = b_node.right
    #e_node = c_node.left
    #f_node = c_node.right

    #a_node.pre_order()
    #a_node.in_order()
    a_node.level_order()
    #print(a_node.height(a_node))

    #print(a_node.is_balanced(a_node))
