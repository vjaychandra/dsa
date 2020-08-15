from main import LinkedList


def oddEvenList(head):

    # base cases
    if head is None:
        return None
    if head.next is None:
        return head

    o = head
    e = head.next
    temp = e

    while e and e.next:
        o.next = e.next
        o = o.next
        e.next = o.next
        e = o.next

    o.next = temp

    return head



if __name__ == "__main__":

    obj = LinkedList()
    obj.insert_last(1)
    obj.insert_last(2)
    obj.insert_last(3)
    obj.insert_last(4)
    obj.insert_last(5)
    obj.insert_last(6)
    obj.insert_last(7)
    obj.insert_last(8)
    
    obj.head = oddEvenList(obj.head)
    obj.print_list()

