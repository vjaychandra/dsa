from main import LinkedList

def is_palindrome(head):

    op = []
    start = head

    while start:
        op.append(start.value)
        start = start.next_node

    return op == op[::-1]



if __name__ == "__main__":
    obj = LinkedList()
    obj.insert_last(3)
    obj.insert_last(5)
    obj.insert_last(8)
    obj.insert_last(8)
    obj.insert_last(5)    
    obj.insert_last(3)
    print(is_palindrome(obj.head))
