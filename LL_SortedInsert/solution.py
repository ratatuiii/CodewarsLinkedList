def sorted_insert(head, data):
    lst = []
    if head is None:
        return Node(data)
    while True:
        lst.append(head.data)
        if head.next is None:
            break
        head = head.next
    lst.append(data)
    lst.sort()
    result = Node(lst[-1])
    for i in lst[:-1:][::-1]:
        temp = Node(i)
        temp.next = result
        result = temp
    return result