from main import LinkedList


def addTwoNumbers(x, y):

    n, m = 0, 0

    ptr = 0
    while x:
        n += (10**ptr) * x.value
        x = x.next_node
        ptr += 1

    ptr = 0
    while y:
        m += (10**ptr) * y.value
        y = y.next_node
        ptr += 1

    op = n+m
    while op > 0:
        print(op%10)
        op = int(op/10)



if __name__ == "__main__":

    l1 = LinkedList()
    l1.insert_last(2)
    l1.insert_last(4)
    l1.insert_last(3)

    l2 = LinkedList()
    l2.insert_last(5)
    l2.insert_last(6)
    l2.insert_last(4)

    print(addTwoNumbers(l1.head, l2.head))
