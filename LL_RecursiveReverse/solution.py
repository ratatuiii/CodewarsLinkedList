def reverse(head):
    if head is None:
        return None
    last = Node(head.data)
    last.next = None
    temp = None
    if head.next is not None:
        temp = reverse(head.next)
        _temp = temp
        while True:
            if _temp.next is not None:
                _temp = _temp.next
            else:
                _temp.next = last
                break
    if temp is not None:
        return temp
    return last
