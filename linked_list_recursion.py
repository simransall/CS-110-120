def is_sorted_recursive(head):
    cur = head
    if cur is None:
        return True
    elif cur.next is None:
        return True
    elif cur.val > cur.next.val:
        return False
    else:
        return is_sorted_recursive(cur.next)

def accordion_recursive(head):
    if head is None:
        return None
    if head.next != None:
        next_head = head.next
        next_head.next = accordion_recursive(next_head.next)
        return next_head
    else:
        return None
