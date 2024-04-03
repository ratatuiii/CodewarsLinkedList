def loop_size(node):
    slow = node
    fast = node

    while fast!=None and fast.next!=None:
         slow = slow.next
         fast = fast.next.next

         if slow==fast:
             slow = node

             while fast!=slow:
                 slow = slow.next
                 fast = fast.next
             break
    counter = 1
    starting_node = slow.next
    while starting_node != slow:
        counter += 1
        starting_node= starting_node.next
    return counter