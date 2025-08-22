class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def add(self, val):
        t = self
        while t.next is not None:
            t = t.next
        
        t.next = ListNode(val)
        return t.next

    def print(self):
        t = self
        while t is not None:
            print(t.val)
            t = t.next

if __name__ == "__main__":
    head = ListNode(5)
    head.add(10)
    head.add(7)
    head.print()
    