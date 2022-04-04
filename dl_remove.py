import dlist_node

def dl_remove(head, node_to_remove):
    cur = head
    if head is None or node_to_remove is None:
        return
    while cur is not None:
        if cur == node_to_remove and cur == head:
            # consider if list only has one node
            if cur.get_next() is None:
                cur = None
                head = None
                return head
            # consider if node_to_remove is the head of the list
            else:
                next_node = cur.get_next()
                cur.set_next(None)
                next_node.set_prev(None)
                cur = None
                head = next_node
                return head
        elif cur == node_to_remove:
            # consider if cur.next is not none
            if cur.get_next() is not None:
                next_node = cur.get_next()
                prev_node = cur.get_prev()
                prev_node.set_next(next_node)
                next_node.set_prev(prev_node)
                cur.set_next(None)
                cur.set_prev(None)
                cur = None
                return head
            # consider if cur.next is none
            else:
                prev_node = cur.get_prev()
                prev_node.set_next(None)
                cur.set_prev(None)
                cur = None
                return head
        cur = cur.get_next()
    return head
