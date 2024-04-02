def stringify(node):
    if not isinstance(node, Node):
        return 'None'
    result = ''
    trigger = True
    current_node = node
    while trigger:
        if current_node.next is None:
            current_node.next = 'None'
            trigger = False
        result += f'{current_node.data} -> '
        current_node = current_node.next
    result += 'None'
    return result