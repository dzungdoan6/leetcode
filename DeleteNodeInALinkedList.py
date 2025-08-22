from ListNode import ListNode
def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    while node.next is not None:
        node.val = node.next.val
        if node.next.next is None:
            node.next = None
        else:
            node = node.next

head = ListNode(4)
head.add(5)
del_node = head.add(1)
head.add(9)

deleteNode(del_node)
head.print()
