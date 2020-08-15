"""
if head node is given then we can start from head node
traverse and then delete the node

if head node is not given and only deleted node is given then
we just need to override the deleted node val and next pointers
with the next node from it

If you think, the delete node is pointed from previous node which refers
to its value and the next node

if we override then the previous node points to the node value and next
arguments which the next node from delete node

"""

# override the given node value with the next node value
# node.val = node.next.val

# override the given node next to the next of its next
# node.next = node.next.next
