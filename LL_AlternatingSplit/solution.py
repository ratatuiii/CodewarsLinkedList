def alternating_split(head):
    if head is None or head.next is None:
        raise Exception
    lst = []
    while True:
        lst.append(head.data)
        if head.next is None:
            break
        head = head.next
    list_one = lst[::2]
    list_two = lst[1::2]
    
    first_list = Node(list_one[-1])
    for i in list_one[:-1:][::-1]:
        temp = Node(i)
        temp.next = first_list
        first_list = temp
        
    second_list = Node(list_two[-1])
    for i in list_two[:-1:][::-1]:
        temp = Node(i)
        temp.next = second_list
        second_list = temp
    return Context(first_list, second_list)