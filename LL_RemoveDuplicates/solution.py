def remove_duplicates(head):
    if head is None or head.next is None:
        return head
    lst = []
    while True:
        lst.append(head.data)
        if head.next is None:
            break
        head = head.next
    ss = set(lst)
    ss = list(ss)
    ss.sort()
    lst = ss
    result = Node(lst[-1])
    for i in lst[:-1:][::-1]:
        temp = Node(i)
        temp.next = result
        result = temp
    return result