# remove the nth node from last

"""
idea is to use the two pointers slow, fast
both starts at head
fast is ahead from slow with nth

base case:
    return head.next if fast is None

do a while on fast.next
    increment both slow and fast

when fast reaches the end of the linked list,
the slow next node is exactly at nth distance from end
so simple we can override the slow.next node to next of its next

after while loop completes - nth node is slow.next
slow.next = slow.next.next

"""
