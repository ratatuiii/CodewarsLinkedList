def push(head, data):
    result_node = Node(data)
    result_node.next = head
    return result_node

def build_one_two_three():
    node3 = Node(3)
    node2 = Node(2)
    node1 = Node(1)
    node1.next = node2
    node2.next = node3
    return node1