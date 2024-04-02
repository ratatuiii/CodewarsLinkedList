def get_nth(node, index):
    counter = 0
    if index < 0 or not isinstance(node, Node):
        raise Exception
    while counter != index:
        if node.next is not None:
            node = node.next
        else:
            raise Exception
        counter += 1
    return node
