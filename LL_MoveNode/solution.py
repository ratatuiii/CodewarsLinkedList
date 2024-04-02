def move_node(source, dest):
    ss = source.next
    dd = Node(source.data)
    dd.next =  dest
    return Context(ss, dd)