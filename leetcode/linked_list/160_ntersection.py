from main import LinkedList

def getIntersectionNode(x, y):

    c1 = get_length(x)
    c2 = get_length(y)
    diff = abs(c1 - c2)

    if c1 > c2:
        x = _fix_pos(diff, x)
    else:
        y = _fix_pos(diff, y)

    while x != y:
        x = x.next
        y = y.next

    return x


def _fix_pos(d, head):

    for _ in range(d):
        head = head.next
    return head

def get_length(head):

    i = 0
    while head:
        i += 1
        head = head.next
    return i
    



if __name__ == "__main__":

    obj = LinkedList()
    obj.insert_last(4)
    obj.insert_last(1)
    obj.insert_last(8)
    obj.insert_last(4)
    obj.insert_last(5)

    obj2 = LinkedList()
    obj2.insert_last(5)
    obj2.insert_last(0)
    obj2.insert_last(1)
    obj2.insert_last(8)
    obj2.insert_last(4)
    obj2.insert_last(5)

    print(getIntersectionNode(obj.head, obj2.head))
