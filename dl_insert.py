# Write your code here :-)

import dlist_node

def dl_insert_before(head, node_in_list, node_to_insert):
    cur = head
    while cur is not None:
        if cur.get_prev() is None and cur == node_in_list:
            cur.set_prev(node_to_insert)
            node_to_insert.set_next(cur)
            return node_to_insert
        elif cur == node_in_list:
            new_node = node_to_insert
            old = cur.get_prev()
            old.set_next(new_node)
            cur.set_prev(new_node)
            new_node.set_next(cur)
            new_node.set_prev(old)
            return head
        cur = cur.get_next()
    return head

def dl_insert_after(head, node_in_list, node_to_insert):
    cur = head
    while cur is not None:
        if cur.get_next() is None and cur == node_in_list:
            cur.set_next(node_to_insert)
            node_to_insert.set_prev(cur)
            return head
        elif cur == node_in_list:
            new_node = node_to_insert
            old = cur.get_next()
            old.set_prev(new_node)
            cur.set_next(new_node)
            new_node.set_next(old)
            new_node.set_prev(cur)
            return head
        cur = cur.get_next()
    return head


