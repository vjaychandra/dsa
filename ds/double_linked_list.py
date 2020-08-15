
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.next = None
        self.previous = None

    def insert(self, data):
        
        new_node = Node(data)
        pointer = self.head

        if self.head is None:
            self.head = new_node
        else:
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node
            new_node.previous = pointer


    def delete(self, data):

        if self.head and self.head.value == data:
            self.head = self.head.next
            self.head.previous = None
        else:
            previous, current = self.find_node(data)
            if current.next:
                current.next.previous = current.previous
            current.previous.next = current.next


    def find_node(self, data):
        
        previous, current = self.head.previous, self.head.next
        while current is not None:
            if current.value == data:
                previous = current.previous
                return previous, current
            current = current.next            
        else:
            raise ValueError(f"'{data}'")
                    
    def print_list(self):
        pointer = self.head
        while pointer:
            print(pointer.value, end=",")
            pointer = pointer.next
        print()

if __name__ == "__main__":

    obj = DoubleLinkedList()
    obj.insert(3)
    obj.insert(5)
    obj.insert(10)
    obj.insert(8)
    obj.insert(45)
    obj.insert(11)
    obj.print_list()
    obj.delete(8)
    obj.print_list()
    
