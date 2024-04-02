def linked_list_from_string(s):
    if '->' not in s:
        return None
    data = s.split(' -> ')[:-1:]
    node = None
    for i in data[::-1]:
        try:
            i = int(i)
        except:
            pass
        node = Node(i, node)
    return node