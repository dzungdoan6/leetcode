from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    p1 = list1
    p2 = list2 
    res = None
    p = None
    while p1 is not None or p2 is not None:
        if p1 is not None and p2 is not None:
            if p1.val < p2.val:
                val = p1.val
                p1 = p1.next
            else:
                val = p2.val
                p2 = p2.next
        elif p1 is not None:
            val = p1.val
            p1 = p1.next
        else:
            val = p2.val
            p2 = p2.next
        
        
        if res is None:
            res = ListNode(val, next=None)
            p = res
        else:
            p.next = ListNode(val, next=None)
            p = p.next
    
    return res

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

res = mergeTwoLists(list1, list2)

p = res
while p is not None:
    print(p.val)
    p = p.next
