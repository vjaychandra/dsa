
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self):
        
        self.head = None

    def insert_last(self, data):
        
        new_node = Node(data)
        if self.head:
            current_pos = self.head
            while current_pos.next:
                current_pos = current_pos.next
            current_pos.next = new_node
        else:
            self.head = new_node

        return new_node

    def insert(self, data):

        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node 

    def delete(self, data):

        if self.head and self.head.value == data:
            self.head = self.head.next
        else:
            previous, current = self.find_node(data)
            previous.next = current.next

    def reverse(self):

        prev = None
        current = self.head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def reverse_recursive(self, prev, cur):

        if cur is None:
            self.head = prev
        else:
            self.reverse_recursive(cur, cur.next)
            cur.next = prev

    def find_node(self, data):
        
        previous, current = self.head, self.head.next
        while current is not None:
            if current.value == data:
                return previous, current
            previous, current = current, current.next
        else:
            raise ValueError(f"'{data}'")
                    
    def print_list(self):
        items = []
        current_pos = self.head
        while current_pos:
            items.append(current_pos.value)
            print(current_pos.value, end=" ")
            current_pos = current_pos.next
        print()
        return items

    def mid_node(self):

        # list should be sorted list

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next            
            fast = fast.next.next
        print(f"Mid Element: {slow.value}")
        return slow

    def has_cycle(self):

        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        

if __name__ == "__main__":

    obj = LinkedList()
    obj.insert_last(3)
    temp = obj.insert_last(5)
    obj.insert_last(8)
    obj.insert_last(10)
    node = obj.insert_last(11)
    node.next = temp
    #obj.insert_last(45)
    print(obj.has_cycle())
    #l1 = obj.print_list()
    #obj.mid_node()
    
    
    
