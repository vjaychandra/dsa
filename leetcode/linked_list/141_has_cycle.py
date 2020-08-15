# idea is to use slow and fast pointers
"""
Floyd loop detection

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        return True
return False
"""

def has_cycle(head):

    slow = fast = head

    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
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
    node.next_node = temp
    #obj.insert_last(45)
    print(obj.has_cycle(obj.head))
