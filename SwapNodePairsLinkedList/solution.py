def swap_pairs(head):
    if head is None:
        return None
    if head.next is None:
        return head
    if head.next.next is None:
        B = head.next
        A = head
        B.next = A
        A.next = None
        return B
    temp = swap_pairs(head.next.next)
    First = head.next
    Second = head
    First.next = Second
    Second.next = temp
    return First
