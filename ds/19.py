from linked_list import Node, LinkedList

obj = LinkedList()
obj.insert_last(1)
obj.insert_last(2)
obj.insert_last(3)
obj.insert_last(4)
obj.insert_last(5)    
#obj.insert_last(45)
l1 = obj.print_list()


def remove_node_last(root, n):

    first = root.head
    second = root.head

    for _ in range(n):
        second = second.next_node

    while second.next_node:
        second = second.next_node
        first = first.next_node
            
    first.next_node = first.next_node.next_node

    return root

    
remove_node_last(obj, n=2)
l1 = obj.print_list()    
