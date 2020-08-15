
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:

    def __init__(self):
        
        self.head = None

    def insert_last(self, data):
        
        new_node = Node(data)
        if self.head:
            current_pos = self.head
            while current_pos.next_node:
                current_pos = current_pos.next_node
            current_pos.next_node = new_node
        else:
            self.head = new_node

    def insert(self, data):

        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next_node = self.head
            self.head = node 

    def delete(self, data):

        if self.head and self.head.value == data:
            self.head = self.head.next_node
        else:
            previous, current = self.find_node(data)
            previous.next_node = current.next_node

    def reverse(self):

        prev = None
        current = self.head
        while current is not None:
            temp = current.next_node
            current.next_node = prev
            prev = current
            current = temp
        self.head = prev

    def reverse_recursive(self, prev, cur):

        if cur is None:
            self.head = prev
        else:
            self.reverse_recursive(cur, cur.next_node)
            cur.next_node = prev

    def find_node(self, data):
        
        previous, current = self.head, self.head.next_node
        while current is not None:
            if current.value == data:
                return previous, current
            previous, current = current, current.next_node
        else:
            raise ValueError(f"'{data}'")
                    
    def print_list(self):
        items = []
        current_pos = self.head
        while current_pos:
            items.append(current_pos.value)
            print(current_pos.value, end=" ")
            current_pos = current_pos.next_node
        print()
        return items

    def mid_node(self):

        # list should be sorted list

        slow = self.head
        fast = self.head

        while fast and fast.next_node:
            slow = slow.next_node            
            fast = fast.next_node.next_node
        print(f"Mid Element: {slow.value}")
        

if __name__ == "__main__":

    obj = LinkedList()
    obj.insert_last(3)
    obj.insert_last(5)
    obj.insert_last(8)
    obj.insert_last(10)
    obj.insert_last(11)    
    obj.insert_last(45)
    l1 = obj.print_list()
    obj.mid_node()
    
    
    
